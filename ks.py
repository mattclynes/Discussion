
import pygame
import sys
import random
from pygame.sprite import Sprite

pygame.init()

white = (255,255,255)
purple = (160,32,240)
blue = (0,191,255)

display_width = 800
display_height = 600
screen=pygame.display.set_mode((display_width,display_height))

guy = pygame.image.load("guy.png")
burger = pygame.image.load("burg.jpg")

batman = pygame.mixer.Sound("batman.wav")
buzz = pygame.mixer.Sound("dead.wav")

guythick = 50
burgthick = 20

direction = "up"
smallfont = pygame.font.SysFont("comicsansms",30)

def introscreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    intro = False
        screen.fill(white)
        message("Welcome to Flavortown!!",blue,-50)
        message("Guy Fieri wants burgers, can you deliver for him??",blue,0)
        message("Press the UP arrow to begin",blue,50)
        pygame.display.update()
        
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
BackGround = Background('mcd.jpg', [135,75])

def score(score):
    text = smallfont.render("Score= " + str(score),True,blue)
    return screen.blit(text,[0,0])

def BurgerCooker():
    BurgX = round(random.randrange(0,display_width-guythick))
    BurgY = round(random.randrange(0,display_height-guythick))
    return BurgX,BurgY

def tail(burgthick,chain):
    if direction == "up":
        go = guy
    if direction == "right":
        go = pygame.transform.rotate(guy,270)
    if direction == "left":
        go = pygame.transform.rotate(guy,90)
    if direction == "down":
        go = pygame.transform.rotate(guy,180)

    screen.blit(go,(chain[-1][0],chain[-1][1]))

    for coordinate in chain[:-1]:
        pygame.draw.rect(screen,purple, (coordinate[0],coordinate[1],burgthick,burgthick))

def text(text,color,size):
    textSurface = smallfont.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message(message,color,yshift = 0,size="small"):
    textSurf,textRect = text(message,color,size)
    textRect.center = (display_width/2),(display_height/2) + yshift
    screen.blit(textSurf,textRect)
    
def gameLoop():
    batman.play()
    gameExit = False
    gameOver = False

    x = display_width/2
    y = display_height/2

    deltaX = 0
    deltaY = 0

    chain =[]
    length = 1

    BurgX = round(random.randrange(0,display_width-burgthick))/10.0
    BurgY = round(random.randrange(0,display_height-burgthick))/10.0
    
    while not gameExit:
      while gameOver == True:
           screen.fill([255, 255, 255])
           score(0)

           pygame.display.update()

           for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   gameOver=False 
                   gameExit=True
               if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_q:
                    gameExit = True
                    gameOver = False
                 if event.key == pygame.K_a:
                   gameLoop()
   
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False
            gameExit = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              deltaX -= burgthick
              deltaY = 0
          if event.key ==  pygame.K_RIGHT:
               deltaX +=burgthick
               deltaY = 0
          if event.key == pygame.K_UP:
             deltaY -= burgthick
             deltaX = 0
          if event.key == pygame.K_DOWN:
              deltaY += burgthick
              deltaX = 0
              
            
      if x >= display_width or x < 0 or y >= display_height or y < 0 :
          gameOver=True
          buzz.play()
      
      x += deltaX
      y += deltaY
      
      screen.fill(white)
      screen.blit(BackGround.image, BackGround.rect)
      guythick = 30
      pygame.draw.rect(screen,white,[BurgX,BurgY,guythick,guythick])
      screen.blit(burger,(BurgX,BurgY))
      
      counter=[]
      counter.append(x)
      counter.append(y)
      chain.append(counter)

      if len(chain) > length:
          del chain[0]

      for piece in chain [: -1]:
          if piece == counter:
              gameOver = True
              buzz.play()

      score(length-1)

      tail(burgthick,chain)
      pygame.display.update()

      if (x > BurgX and x < BurgX + guythick) or (burgthick + x > BurgX and  x + burgthick < guythick + BurgX):           
           if y > BurgY and y < BurgY + guythick:             
             BurgX = round(random.randrange(0,display_width-burgthick)*10.0/10.0)
             BurgY = round(random.randrange(0,display_height-burgthick)*10.0/10.0)
             length += 1
           if burgthick + y > BurgY and y + burgthick < BurgY + guythick:                
                BurgX = round(random.randrange(0,display_width-burgthick))
                BurgY = round(random.randrange(0,display_height-burgthick))
                length += 1
    
    pygame.quit()
    quit()
introscreen()
gameLoop()
# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')

soupstr = str(soup)
soupstr = soupstr.replace("student", "AMAZING student")
soupstr = soupstr.replace("https://www.youtube.com/embed/mimp_3gquc4?feature=oembed", "ski.jpg")

soupstr = BeautifulSoup(soupstr, "html.parser")

for picture in soupstr.find_all(class_ = "logo"):
	if picture.img:
		picture.img['src'] = "media/logo.png"
for picture in soupstr.find_all(class_ = "footer-logo"):
	if picture.img:
		picture.img['src'] = "media/logo.png"

t = open("bshw3.html", "w")
t.write(soupstr.prettify())
t.close()
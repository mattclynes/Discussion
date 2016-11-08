# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.


from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'T69Vy6xI7KQ0y5CdTA7YBWYbQ'
CONSUMER_SECRET = '7OVvdTfWjkXe4anDrQUbPN7JCVy9oNnuYaTPZa6dQ882KVqffm'
ACCESS_TOKEN_KEY = '795987936382697472-Ay57eZoZKiOL6bqVTYmMMUYCEJZD1yi'
ACCESS_TOKEN_SECRET = 'MwU6qqYGVlA9TNAt5yBBgYfPckUxzLYAsbLCIBTNDwAJy'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
file = open('watson.jpg', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'This is my doggo #UMSI-206 #Proj3'}, {'media[]':data})






# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "795987936382697472-Ay57eZoZKiOL6bqVTYmMMUYCEJZD1yi"
access_token_secret = "MwU6qqYGVlA9TNAt5yBBgYfPckUxzLYAsbLCIBTNDwAJy"
consumer_key = "T69Vy6xI7KQ0y5CdTA7YBWYbQ"
consumer_secret = "7OVvdTfWjkXe4anDrQUbPN7JCVy9oNnuYaTPZa6dQ882KVqffm"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

inp = input("What do you want to search for?")
public_tweets = api.search(inp)

s = 0
p = 0 
c = 0 

print("\n", "Here are the tweets:", '\n')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	s += analysis.subjectivity
	p += analysis.polarity
	c += 1 

avs = s/c
avp = p/c 

print("\n", "---------------------------------------------","\n")

print("Average subjectivity is", avs)
print("\n", "---------------------------------------------","\n")
print("Average polarity is", avp)
print("\n", "---------------------------------------------","\n")

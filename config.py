import tweepy
from tweepy import OAuthHandler

#Obtain these from the TwitterAPI by making an account and registering with them.

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = ' access_token'
access_secret = ' access_secret'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

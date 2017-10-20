import tweepy
import config

#Program to follow every follower for your account.

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
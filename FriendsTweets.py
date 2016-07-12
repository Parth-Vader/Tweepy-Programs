#!/usr/bin/env python
import tweepy
import json
import config

#Program to display your friend's tweets
def process_or_store(tweet):
    print(json.dumps(tweet))



for friend in tweepy.Cursor(api.friends).items(25):
    process_or_store(friend._json)   
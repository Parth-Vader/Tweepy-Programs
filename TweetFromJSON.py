#!/usr/bin/env python
import tweepy
import config
import json
 
#Program to print tweets from .json file
 
with open('python.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print
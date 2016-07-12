#!/usr/bin/env python
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import config

#Program to track all the tweets containing a specific word
#Can be used to keep track of events

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#Put the word/hastag here.
twitter_stream.filter(track=['#India'])

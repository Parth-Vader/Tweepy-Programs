#!/usr/bin/env python
import tweepy
import config
#Program to show the user's details
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
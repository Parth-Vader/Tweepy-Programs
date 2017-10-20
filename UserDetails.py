#!/usr/bin/env python
import tweepy
import config
#Program to show the user's details
user = api.me()
 
print('Name: %s ' % (user.name))
print('Location: %s ' % (user.location))
print('Friends: %s ' % (str(user.friends_count)))
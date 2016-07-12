#!/usr/bin/env python
import tweepy
import config

#Program to search for tweets in a range around the latitude and longitude provided.

#Change geocode and the radius here.
results = api.search(geocode='22.3073,73.1811,10mi') 

for result in results:
    print result.text
    print result.location if hasattr(result, 'location') else "Undefined location"


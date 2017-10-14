
import tweepy
import config

#Prints the location as well as description of each of your friends on Twitter.
def process_or_store(sta):
	print("%s %s %s" % (sta["location"], sta["description"], "\n"))

#for status in tweepy.Cursor(api.user_timeline).items(200):
#    process_status(status)

for friend in tweepy.Cursor(api.friends).items(25):
    process_or_store(friend._json)   
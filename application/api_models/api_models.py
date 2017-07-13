#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json


# Variables that contains the user credentials to access Twitter API 
access_token = "2902033948-GUoceoyNVxjhklAsNxy6GIL6iGoo6YrR3PzhjN1"
access_token_secret = "0ePHIbLO1S4gsIXPot1vMxx8PmFkiOTAjTq0rxr6134Kq"
consumer_key = "oHSQXvTpsJ9oEL6pL1DAkOOxt"
consumer_secret = "f7B110Wq8bVPeADMdf9DwNHcBT3tbqOjMvZsM67eFCIdfNE724"

# Virustotal Credentials
apikey = 'a4b128f4b05396d094ea6e08ddf37b895b05ccbe5d6f24389a197dfdd1f5aaa3' 

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, tweet_limit):
        self.tweet_limit = tweet_limit
        self.current_tweet_number = 1
        self.urls = {}
        self.username = ''
        self.created_at = ''
        self.text = ''
        self.followers_count = 0

    def allocate_urls(self, data):
        current_tweet_urls = []
        # self.urls[self.current_tweet_number] = 
        current_tweet_urls.append(data["user"]["url"])
        
        if "retweeted_status" in data:
            current_tweet_urls.append(data["retweeted_status"]["entities"]["urls"][0]["expanded_url"])
        self.urls[self.current_tweet_number] = current_tweet_urls
        return self.urls

    def allocate_username(self,data):
        self.username = data["user"]["screen_name"]
        return self.username

    def allocate_created_time(self,data):
        self.created_at = data["created_at"]
        return self.created_at

    def allocate_tweet_text(self,data):
        self.text = data["text"]
        return self.text

    def allocate_followers_count(self,data):
        self.followers_count = data["user"]["followers_count"]
        return str(self.followers_count)

    # This method acts as our interface/duck type
    def on_data(self, data):
        d = json.loads(data)
        # print data
        print "\n" + str(self.current_tweet_number) + "\n"
        print self.allocate_urls(d)
        print self.allocate_username(d)
        print self.allocate_created_time(d)
        print self.allocate_tweet_text(d)
        print self.allocate_followers_count(d)

        if self.current_tweet_number == self.tweet_limit:
            return False
        
        self.current_tweet_number += 1
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(3) 
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This filters Twitter Streams to capture data by the keywords from a config file (config.json)
    
    with open('config.json') as data_file:
        data = json.load(data_file)
        stream.filter(track=data["hashtags"])
        

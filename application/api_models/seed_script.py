from api_models import *

#This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener(3) 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

#This filters Twitter Streams to capture data by the keywords from a config file (config.json)
    
with open('config.json') as data_file:
    data = json.load(data_file)
    stream.filter(track=data["hashtags"])
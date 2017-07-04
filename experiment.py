#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2902033948-GUoceoyNVxjhklAsNxy6GIL6iGoo6YrR3PzhjN1"
access_token_secret = "0ePHIbLO1S4gsIXPot1vMxx8PmFkiOTAjTq0rxr6134Kq"
consumer_key = "oHSQXvTpsJ9oEL6pL1DAkOOxt"
consumer_secret = "f7B110Wq8bVPeADMdf9DwNHcBT3tbqOjMvZsM67eFCIdfNE724"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
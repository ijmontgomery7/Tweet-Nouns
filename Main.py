from pymongo import MongoClient
import json
from tweepy import Stream, OAuthHandler, streaming


with open('auth.json') as f:
    auth_info = json.load(f)

mongoInfo = auth_info['mongo']
twitterInfo = auth_info['twitter']


client = MongoClient('mongodb+srv://' + mongoInfo['username'] + ':' + mongoInfo['password'] + mongoInfo['server'] + '/tweets')

db = client.tweets


class StdOutListener(streaming.StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        data = json.loads(data)
        insert = {'text': data['text'], 'created_at': data['created_at']}


        print(insert)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(twitterInfo['consumer_key'], twitterInfo['consumer_secret'])
auth.set_access_token(twitterInfo['access_token'], twitterInfo['access_token_secret'])

l = StdOutListener()

stream = Stream(auth, l)
stream.filter(track=['New York'])


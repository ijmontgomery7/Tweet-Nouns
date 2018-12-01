from pymongo import MongoClient
import json
from tweepy import Stream, OAuthHandler, streaming
import nltk
import re

with open('auth.json') as f:
    auth_info = json.load(f)

mongoInfo = auth_info['mongo']
twitterInfo = auth_info['twitter']


client = MongoClient('mongodb+srv://' + mongoInfo['username'] + ':' + mongoInfo['password'] + mongoInfo['server'] + '/tweets')

db = client['tweets']


class StdOutListener(streaming.StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        data = json.loads(data)

        if 'retweeted_status' not in data and data['lang'] == 'en':
            nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(data['text'])) if pos[0] == 'N']
            for i in range(len(nouns)):
                nouns[i] = re.sub('[^\x00-\x7F]', '', nouns[i])
                nouns[i] = nouns[i].replace('@', '')
                nouns[i] = nouns[i].replace('http', '')
                nouns[i] = nouns[i].replace('https', '')
            nouns = list(filter(None, nouns))

            data = {'_id': str(data['id']), 'nouns': nouns}
            db['tweets'].insert_one(data)

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(twitterInfo['consumer_key'], twitterInfo['consumer_secret'])
auth.set_access_token(twitterInfo['access_token'], twitterInfo['access_token_secret'])

l = StdOutListener()

stream = Stream(auth, l)
stream.filter(track=['New York'])


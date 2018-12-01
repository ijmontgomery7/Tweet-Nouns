from pymongo import MongoClient
import json


with open('auth.json') as f:
    auth_info = json.load(f)

mongoInfo = auth_info['mongo']



client = MongoClient('mongodb+srv://' + mongoInfo['username'] + ':' + mongoInfo['password'] + mongoInfo['server'] + '/tweets')

new= open("input.txt", "w+")


db = client['tweets']
cursor = db['tweets'].find({})
for document in cursor:
    for item in document['nouns']:
        new.write(item + '\n')



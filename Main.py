from pymongo import MongoClient
import json


with open('auth.json') as f:
    auth_info = json.load(f)

mongoInfo = auth_info['mongo']

client = MongoClient('mongodb+srv://' + mongoInfo['username'] + ':' + mongoInfo['password'] + mongoInfo['server'] + '/tweets')

db = client.tweets




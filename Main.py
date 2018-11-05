
import json


with open('auth.json') as f:
    auth_info = json.load(f)

mongoInfo = auth_info['mongo']

clientURL = 'mongodb+srv://' + mongoInfo['username'] + ':' + mongoInfo['password'] + mongoInfo['server']





# Tweet-Nouns
Find most common nouns of tweets

to start make sure you have mongo python drivers
`pip install pymongo[gssapi,srv,tls]`


add json file with authentication details named `auth.json`
```
{
  "mongo":{
    "username": "USERNAME",
    "password": "PASSWORD",
    "server": "SERVER"
  },
  "twitter":{
    "consumer_key": "KEY",
    "consumer_secret": "SECRET",
    "access_token": "TOKEN",
    "access_token_secret":"TOKEN_SECRET"
  }

}
```

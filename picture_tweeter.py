# Script that takes a picture path as an argument, and then tweets it
import twitter
import json
import os

def pic_tweet(pic_path, credentials_path):
    credentials = json.loads(open(credentials_path).read())
    
    api = twitter.Api(consumer_key=credentials["key"],
            consumer_secret=credentials["secret"],
            access_token_key=credentials["access_token"],
            access_token_secret=credentials["access_token_secret"])
    
    
    print('posting picture ' + pic_path + ' ...')
    status = api.PostUpdate(status='', media=pic_path)
    

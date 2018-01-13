# Script that takes a picture path as an argument, and then tweets it
import twitter
import json
import sys, os

pic_path = sys.argv[1]

credentials = json.loads(open("credentials.json").read())

try:
    api = twitter.Api(consumer_key=credentials["key"],
            consumer_secret=credentials["secret"],
            access_token_key=credentials["access_token"],
            access_token_secret=credentials["access_token_secret"])

except twitter.TwitterHTTPError as twittererror:
    print('authentication failed :-\(')

print('posting picture ' + pic_path + ' ...')
try:
    status = api.PostUpdate(status='', media=pic_path)
except twitter.TwitterHTTPError as twittererror:
    print('Failure !!!')


# Script that should tweet one of the picture of the folder that has not been tweeted yet
import os, sys
import json
import re
import random
from picture_tweeter import pic_tweet

path = sys.argv[1]
credentials = sys.argv[2]

# managing the .already_tweeted.json file, that keeps track of what's have been tweeted so far
if not(os.path.isfile("./.already_tweeted.json")):
    # if there's no such file, let's create an empty one
    already_tweeted = {}
    already_tweeted['data'] = []
    already_tweeted['folder_path'] = path
else:
    # if there's one, we just have to open it
    with open(".already_tweeted.json", 'r') as f:
        already_tweeted = json.load(f)
        
        # the opened .already_tweeted.json folder sould correspond to to the folder we are working with
        # the program should fail if they do not correspond
        # TODO : make it so several .already_tweeted.json files can be handled
        assert path == already_tweeted['folder_path']     

# building a list of all the picture files that are in the specified folder
all_pics = [ filename for filename in os.listdir(path) if re.match(r"(.)+.(png|jpg|JPG|PNG)$", filename) ]
not_tweeted_yet_pics = [ filename for filename in all_pics if filename not in already_tweeted['data'] ] # it reads just like natural language, ain't that beautiful ?

if len(not_tweeted_yet_pics) == 0:
    print('Nothing left to tweet !')
else:
    chosen =  random.choice(not_tweeted_yet_pics)
    
    pic_tweet(path + chosen, credentials)
    # if it fails to send a tweet for some reason, the previous line should throw an error.
    # Therefore, the line under here would not be executed and the picture would not be added
    # to the .already_tweeted.json file.
    already_tweeted['data'].append(chosen)
    
# updates the .already_tweeted.json file
with open(".already_tweeted.json", 'w') as f:
    json.dump(already_tweeted, f)


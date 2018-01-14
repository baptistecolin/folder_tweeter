# Script that should tweet one of the picture of the folder that has not been tweeted yet
import os, sys
import json
import re

path = sys.argv[1]

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

with open(".already_tweeted.json", 'w') as f:
    json.dump(already_tweeted, f)


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

else:
    # if there's one, we just have to open it
    with open(".already_tweeted.json", 'r') as f:
        already_tweeted = json.load(f)
    print(already_tweeted)

# building a list of all the picture files that are in the specified folder
all_pics = [ filename for filename in os.listdir(path) if re.match(r"(.)+.(png|jpg|JPG|PNG)$", filename) ]

with open(".already_tweeted.json", 'w') as f:
    json.dump(already_tweeted, f)


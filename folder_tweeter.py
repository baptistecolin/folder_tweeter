# Script that should tweet one of the picture of the folder that has not been tweeted yet
import os, sys
import json
import re

if not(os.path.isfile("./.already_tweeted.json")):
    already_tweeted = {}
    already_tweeted['data'] = []

else:
    with open(".already_tweeted.json", 'r') as f:
        already_tweeted = json.load(f)
    print(already_tweeted)

all_pics = [ filename for filename in os.listdir(path) if re.match(r"(.)+.(png|jpg|JPG|PNG)$", filename) ]

with open(".already_tweeted.json", 'w') as f:
    json.dump(already_tweeted, f)


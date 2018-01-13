# Script that should tweet one of the picture of the folder that has not been tweeted yet
import os
import json

if not(os.path.isfile("./.already_tweeted.json")):
    already_tweeted = {}
    already_tweeted['data'] = []

else:
    with open(".already_tweeted.json", 'r') as f:
        already_tweeted = json.load(f)
    print(already_tweeted)

with open(".already_tweeted.json", 'w') as f:
    json.dump(already_tweeted, f)


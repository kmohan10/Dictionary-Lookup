# Read a json file into python

import json

data = json.load(open("dictionary_data.json","r"))

type(data)


from difflib import SequenceMatcher
from difflib import get_close_matches

def translate(w):
    w = w.lower()
    
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(), cutoff=0.8)) > 0:
        response = input("Did you mean %s instead? If yes, type Y - if no, type N: " % get_close_matches(w,data.keys(), cutoff=0.6)[0])
        if response == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif response == 'N':
            return "Please double check the re-enter the word"
        else:
            return "Invalid Request - Please enter Y or N"   
    else:
        return "Word not found in Dictionary"

word = input("Enter word to lookup: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



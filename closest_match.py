from difflib import get_close_matches
import json

data = json.load(open('data.json'))

def meaning(word):
    word = word.lower()
    suggestion = get_close_matches(word,data.keys())
    
    if word in data:
        return data[word]
    
    elif len(suggestion)>0:
        
        for i in suggestion:
            response = input("Did you mean {} :".format(i))
            if response == 'y':
                return data[i]

        return 'Not found'
    
    else:
        return "You word is not from this planet"

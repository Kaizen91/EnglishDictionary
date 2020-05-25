#take a user input 
#find that input in the dictionary
#load the dictionary
#print the output

import json 
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif len(get_close_matches(word, data.keys())) > 0:
        yn =  input('Did you mean %s? \nEnter Y for Yes or N for No.\n' % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return 'Your word is not in the dictionary. Please try again.'
        else:
            return 'We didn\'t understand your query'
    else:
        return 'Your word is not in the dictionary. Please try again.'
        
word = input('Please input a word: ')
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
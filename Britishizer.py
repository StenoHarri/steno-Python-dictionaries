



input_file = 'lapwing-base'
output_file = 'output'


import requests
import re

def britishize(string):
    url ="https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/american_spellings.json"
    american_to_british_dict = requests.get(url).json()    

    for american_spelling, british_spelling in american_to_british_dict.items():
        string = re.sub(f'(?<![a-zA-Z]){american_spelling}(?![a-z-Z])', british_spelling, string)
  
    return string


with open(input_file + '.json', 'r', encoding="utf-8") as file:
    file_contents = file.read()
    #print(str(file_contents))
    print("Contents load in, now I need to make it British")
    British_contents=(britishize(str(file_contents)))
    #print(British_contents)
    print("it is now British")

with open(output_file + '.json', 'w', encoding="utf-8") as file:
    file.write(British_contents)
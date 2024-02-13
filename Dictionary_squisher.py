"""
Squish multiple dictionaries together, maybe convert ^ into #
"""
import re
import json





#The last dictionary, overwrites the previous dictionary
#I need to replace this with just reading the plover.cfg file
list_of_dictionaries = [#"collapsed_all_before_python"
                        "Harri_phrasing",
                        #"collapsed_all_after_python"
                        ] #Highest priority











LONGEST_KEY = 4


import os
cwd = os.getcwd()

numbers_to_letters = {
    "1": "S",
    "2": "T",
    "3": "P",
    "4": "H",
    "5": "A",
    "6": "F",
    "7": "P",
    "8": "L",
    "9": "T",
    "0": "O"
    }

def aericks_denumberizer(old_outline):

    old_strokes = old_outline.split("/")
    new_strokes = []

    for stroke in old_strokes:

        new_strokes.append(stroke)

        for match in numbers_to_letters.keys():

            if match in stroke:

                if new_strokes[-1][0] != "#":
                    new_strokes[-1] = "#" + new_strokes[-1]

                new_strokes[-1] = new_strokes[-1].replace(match, numbers_to_letters[match])

        if new_strokes == []:
            new_strokes = old_strokes

    return "/".join(new_strokes)

left_hand_letters_to_numbers = {
    "S": "1",
    "T": "2",
    "P": "3",
    "H": "4",
    "A": "5",
    "O": "0"
    }

right_hand_letters_to_numbers = {
    "F": "6",
    "P": "7",
    "L": "8",
    "T": "9"
    }



def renumberer(hashed_outline):
    hashed_strokes = hashed_outline.split("/")
    numbered_strokes = []
    try:
        for stroke in hashed_strokes:
            match = re.fullmatch(r'(#?)(S?T?K?P?W?H?R?A?O?\*?)(-?E?U?F?R?P?B?L?G?T?S?D?Z?)', stroke)
            if not match[1] == '#':
                numbered_strokes.append(match[2]+match[3])
            else:
                numbered_stroke = (match[2].replace(
                    'S','1').replace(
                        'T','2').replace(
                            'P','3').replace(
                                'H','4').replace(
                                    'A','5').replace(
                                        'O','0') + 
                                match[3].replace(
                                    'F','6').replace(
                                        'P','7').replace(
                                            'L','8').replace(
                                                'T','9'))
                if bool(re.search(r'\d', numbered_stroke)):
                    numbered_strokes.append(numbered_stroke)
                else:
                    numbered_strokes.append(match[1]+numbered_stroke)
        return "/".join(numbered_strokes)
    except TypeError:
        return hashed_outline


def collapse_outlines(dictionary_file, collapsed_dictionary = {}, force_cap=False):
    #The latest addition overwrites the previous entry at that location
    with (open(dictionary_file, "r", encoding="utf-8")) as temp_dictionary:                                        #debug
    #with (open('C:\\Users\\harrry\\AppData\\Local\\plover\\plover\\' + dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Windows
    #with (open("Library/Application Support/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Macintosh
    #with (open(".config/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary:                      #Linux
        temp_dictionary = json.load(temp_dictionary)
        for outline in temp_dictionary:


            #Do you want just a #? Better legibility
            #new_outline = aericks_denumberizer(outline).replace('^','#')


            #Do you want numbers? I do cause #STPB is not valid, it's 1234
            new_outline = str(outline).replace('^','#')






            if not '##' in new_outline:
                collapsed_dictionary[renumberer(new_outline)] = temp_dictionary[outline]

    return collapsed_dictionary




collapsed_dictionary = {}
reverse_lookup_dictionary = {}

#Send everything through normally
for dictionary in list_of_dictionaries:
    collapsed_dictionary = collapse_outlines(dictionary + ".json", collapsed_dictionary)




#reverse_dictionary = {translated_phrase:outline for outline,translated_phrase in collapsed_dictionary.items()} 

#collapsed_dictionary['-PG'] = str(len(collapsed_dictionary))


def lookup(strokes):

    outline = "/".join(strokes)
    outline = aericks_denumberizer(outline)

    return collapsed_dictionary[outline]

with open("harri_phrasing_numbered.json", "w") as outfile:
    json.dump(collapsed_dictionary, outfile, indent=0)




"""
#def reverse_lookup(translated_phrase):

    This don't work cause you can't alter what goes in, only what comes out
    outline = "/".join(strokes)

    return {key for key,value in collapsed_dictionary.items() if value==outline }
    
    #return reverse_dictionary
"""


#print(lookup(("^PHAOE","TPHOE")))
#print(lookup(("#TPHOS","KOEPL","KWRAL")))
#print(lookup("^SKWRABGS")) Nos comb amino acid

#print(reverse_lookup(("reverse"))) okay huh

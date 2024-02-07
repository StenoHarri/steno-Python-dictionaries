import re
import json




#The last dictionary, overwrites the previous dictionary
list_of_dictionaries = ["Plover/no_compounds",                   #Least priority
                        "Lapwing/uk",
                        "Lapwing/base",
                        "Lapwing/additions",
                        "Josiah/base",
                        "Josiah/additions",
                        "Lapwing/conflict",
                        "Harri/personal"]  #Most priority









LONGEST_KEY = 4


def convert_steno_numbers_to_steno_keys(stroke):
    return stroke.replace(
            "0", "O").replace(
                "1", "S").replace(
                    "2", "T").replace(
                        "3", "P").replace(
                            "4", "H").replace(
                                "5", "A").replace(
                                    "6", "F").replace(
                                        "7", "P").replace(
                                            "8", "L").replace(
                                                "9", "T")



def fold_dictationary(dictionary_file, folded_dictionary = {}, force_cap=False):
    #The latest addition overwrites the previous entry at that location
    
    with (open(dictionary_file)) as temp_dictionary:                                        #debug
    #with (open("%USERPROFILE%\\AppData\\Local\\plover\\"+ dictionary_file)) as temp_dictionary: #Windows
    #with (open("Library/Application Support/plover/"+ dictionary_file)) as temp_dictionary: #Macintosh
    #with (open(".config/plover/"+ dictionary_file)) as temp_dictionary:                      #Linux
        temp_dictionary = json.load(temp_dictionary)
        for stroke in temp_dictionary:
            outline = temp_dictionary[stroke]
            if force_cap:
                if outline[0] == "{":
                    outline = "{" + outline[1].upper() + outline[2:]
                else:
                    outline = outline[0].upper() + outline[1:]
            if any(single_digit_number in "0123456789" for single_digit_number in stroke):            
                stroke = "#" + convert_steno_numbers_to_steno_keys(stroke)



            """
            
            Here, it's these following 'if' statements you want to change
            Stroke is something like "A/PHAEUZ"
            Outline is something like "amaze"
            """

            if stroke[0] == "#":
                folded_dictionary["#+" + stroke[1:]] = '{^}"\n\n' + outline + ':\n- "{^}{-|}'

    return folded_dictionary

#The last dictionary, overwrites the previous dictionary
list_of_dictionaries = ["Plover/no_compounds",                   #Least priority
                        "Lapwing/uk",
                        "Lapwing/base",
                        "Lapwing/additions",
                        "Josiah/base",
                        "Josiah/additions",
                        "Lapwing/conflict",
                        "Harri/personal"]  #Most priority

folded_dictionary = {}

#Send everything through normally
for dictionary in list_of_dictionaries:
    folded_dictionary = fold_dictationary(dictionary + ".json", folded_dictionary)




def lookup(strokes):

    strokes = "/".join(strokes)
    if any(single_digit_number in "0123456789" for single_digit_number in strokes):
        strokes = "#" + convert_steno_numbers_to_steno_keys(strokes)


    return folded_dictionary[strokes]

with open("speech_formatting.json", "w") as outfile:
    json.dump(folded_dictionary, outfile)
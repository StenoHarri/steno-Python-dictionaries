"""
Combine multiple dictionaries together
"""

import json




#The last dictionary, overwrites the previous dictionary
list_of_dictionaries = [#"collapsed_dictionaries_that_go_before_python_no_autocaps",
                        "Josiahsuser",
                        "Josiah_additions"
                        ] #Highest priority



def collapse_outlines(dictionary_file, combined_dictionary = {}):

    with (open(dictionary_file, "r", encoding="utf-8")) as temp_dictionary:

        temp_dictionary = json.load(temp_dictionary)
        for outline in temp_dictionary:

            combined_dictionary[outline] = temp_dictionary[outline]

    return combined_dictionary



combined_dictionary = {}

#Send everything through normally
for dictionary in list_of_dictionaries:
    combined_dictionary = collapse_outlines(dictionary + ".json", combined_dictionary)




with open("combined.json", "w") as outfile:
    json.dump(combined_dictionary, outfile, indent=0)


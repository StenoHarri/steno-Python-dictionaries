"""
@Jalexu on discord had an idea for fingerspelling using the whole keyboard, not just one letter at a time
Key considerations were that it wasn't tailored for English, as this is mostly for foreign words/names
"""

entry_strokes={
    "starter normal"  :['PN'],        #shrimple with normal formatting
    "starter attached":[],            #shrimple with not space at the start
    "starter cap"     :[],            #shrimple but capped the first letter
    "starter acronyms":[],            #shrimple but all caps
    "starter cap attached":[],
    "starter acronyms attached":[]
}




make_starter_letters_have_left_to_right_priority = True
user_definitions={
    "" : "",
    
    "F": "f",
    "FC": "h",

    "S" : "s",

    "C": "c",

    "Z": "z",

    "P": "p",

    "N" : "n",

    "R" : "r",

    "X" : "x",

    "I": "i",

    "U":"u",

    "u":"u",

    "i": "i",

    "e": "e",

    "a":"a",

    "n":"n",

    "p":"p",

    "z":"z",

    "c":"c",

    "s":"s",

    "f":"f"
}



strokes_you_can_use_to_exit_shrimple_with=[

    "FCf"

]




#dedicated key settings:
dedicated_key = '+'             #Instead of a starter stroke
make_words_done_with_dedicated_key_exit_immediately = True
#joiner_strokes={ #If Shrimple automatically exits, maybe you wanna use KWR to stay in Shrimple
#    "left-hand joiner" : "^SKWR",
#    "right-hand joiner" : "FPL"
#}

































































import re

LONGEST_KEY = 40


def construct_every_combination(part_of_the_keyboard):
    """
    Given a set of options, left or right, up or down.
    Will return all combinations:
    left+up, left+down, right+up, right+down, etc.
    """
    
    path_direction=(part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys())
    every_combination_dictionary={}
    every_combination = [[]]  # Initialize with empty list
    for length_of_combination in range(len(path_direction)):
        current_options = path_direction[length_of_combination]
        new_combinations = []  # Temporary list to store updated combinations

        for option in current_options:
            for existing_combination in every_combination:
                new_combination = existing_combination + [option]
                if re.fullmatch(r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)',"".join(new_combination)):
                    new_combinations.append(new_combination)

        every_combination.extend(new_combinations)  # Add new combinations

    for combination in every_combination:
        the_combination = "".join(combination)
        if the_combination.count("*")>1:
            continue


        translation=""
        for chord in combination:
            translation += part_of_the_keyboard[chord]
        if "[delete me]" in translation:
            continue
        if not the_combination in every_combination_dictionary:
            every_combination_dictionary[the_combination] = translation


    return every_combination_dictionary

#FSCZPNRXIUuieanpzcsf
generated_definitions = construct_every_combination(user_definitions)



def lookup(strokes):
    output_string=""

    for stroke_number, stroke in enumerate(strokes):

        if stroke_number == 0:
            if not dedicated_key in stroke:
                stroke_valid = False
                for entry_stroke_category in entry_strokes.values():
                    if stroke in entry_stroke_category or strokes in entry_stroke_category:
                        stroke_valid = True
                if not stroke_valid:
                    raise KeyError
                if len(strokes)==1:
                    return '{Entered Shrimple}'
        else:
            if not dedicated_key in stroke:
                stroke_valid = False
                for entry_stroke_category in entry_strokes.values():
                    if stroke in entry_stroke_category:
                        stroke_valid = True
                if stroke_valid:
                    raise KeyError
        
        if stroke==dedicated_key:
            raise KeyError


        if stroke in strokes_you_can_use_to_exit_shrimple_with:
            raise KeyError



        if make_words_done_with_dedicated_key_exit_immediately and dedicated_key in strokes[0]:
            match = re.fullmatch(r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)', stroke.replace(dedicated_key,""))
            if stroke_number == 0 and not dedicated_key in stroke:
                raise KeyError
            elif not stroke_number == 0:
                raise KeyError
            
        #output_string+="hi "


    if (len(strokes)) == 1 and dedicated_key not in strokes[0]:
        if strokes[0]==entry_strokes['starterattached']:
            return ("{^}")
        else:
            return("{^ ^}")
        

    for stroke_number, stroke in enumerate(strokes):

        if ((not stroke_number == 0 and stroke in entry_strokes.values())
             or dedicated_key in stroke):
            raise KeyError
        
        match= re.fullmatch(
            r'(F?S?C?Z?P?N?R?X?I?U?u?i?e?a?n?p?z?c?s?f?)',

            #this string:
            stroke.replace(dedicated_key,""))

        if not match:
            raise KeyError
        
        stroke_output=generated_definitions[match[1]]

        #do whatever checks you want here

        
        
        
        
        if not stroke_number==0 or (dedicated_key in strokes[0]):
            output_string+=stroke_output


    if strokes[0] in entry_strokes['starter cap']:
        return output_string.capitalize()
    if strokes[0] in entry_strokes["starter acronyms"]:
        return output_string.upper()
    if strokes[0] in entry_strokes['starter attached']:
        return "{^^}"+output_string
    if strokes[0] in entry_strokes['starter cap attached']:
        return "{^^}"+output_string.capitalize()
    if strokes[0] in entry_strokes['starter acronyms attached']:
        return "{^^}"+output_string.upper()
    return output_string



#lookup(("+KAPZ","KWROU"))
#lookup(("KAPS","KWROU"))
#print(lookup(("PN", "PNen")))
#print(lookup(("KAPS", "WA*TD", "KWRAL")))
#print(lookup(("KAPS", "WA*TD", "KWRAL", "PAL")))


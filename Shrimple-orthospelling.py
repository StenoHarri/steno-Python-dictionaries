"""
@Jalexu on discord had an idea for fingerspelling using the whole keyboard, not just one letter at a time
Key considerations were that it wasn't tailored for English, as this is mostly for foreign words/names
"""


entry_strokes={
    "starter normal"  :['KWR*', 'SP*', 'SHREUFRPL', 'SHR*EUFRPL'],           #shrimple with normal formatting
    "starter attached":['KWR', 'SW*'],      #shrimple with not space at the start
    "starter cap"     :['TPH*'],            #shrimple but capped the first letter
    "starter acronyms":['KAPS'],            #shrimple but all caps
    "starter cap attached":['TPH*FPLT'],
    "starter acronyms attached":['TPH*FPLTS']
}


#dedicated key settings:
dedicated_key = '+'             #Instead of a starter stroke
make_words_done_with_dedicated_key_exit_immediately = True
joiner_strokes={ #If Shrimple automatically exits, maybe you wanna use KWR to stay in Shrimple
    "left-hand joiner" : "^SKWR",
    "right-hand joiner" : "FPL"
}


make_starter_letters_have_left_to_right_priority = True
starter_letter={
    "" : "",

    "^":"{^^}",

    "S" : "s",
    "STKPW": "z",
    "SKWR": "j",
    "SKHR": "shr", #Josiah theory
    "SH" : "sh",
    "SHR" : "sl", #Josiah theory
    "SR" : "v",

    "T" : "t",
    "TK": "d",
    "TKPW":"g",
    "TP": "f",
    "TPH": "n",

    "K":"k",
    "KP":"x",
    "KW":"q",
    "KWH":"y",
    "KWR":"",
    "KH":"ch",
    "KR":"c",

    "P":"p",
    "PW":"b",
    "PH":"m",
    "PHR":"pl", #conflict with mr

    "W":"w",

    "H":"h",
    "HR":"l",

    "R":"r"
}



vowels={
    "-":"",
    
    "":"",

    "*":"",
    "A*":"u",
    "AO*":"i",
    "O*":"e",
    "A*EU":"ay",
    "O*EU":"oy",
    "*EU":"y",


    "A"   :"a",
    "AO"  :"oo",
    "AOE" :"ee",
    "AOEU":"i[e]",
    "AOU" :"u[e]",
    "AE"  :"ea",
    "AEU" :"a[e]",
    "AU"  :"au",

    "O"   :"o",
    "OE"  :"o[e]",
    "OEU" :"oi",
    "OU"  :"ou",

    "E"   :"e",
    "EU"  :"i",

    "U"   :"u"
}

make_ender_letters_have_left_to_right_priority = True
ender_letter={
    "":"",
    "*":"", #asterisk on its own is invalid

    "*FT":"st",
    "*FTD":"sted",
    "*PBG":"nk",
    "*PZ":"h",
    "*BG":"ck",
    "*BGD":"cked",
    "*LG":"lk",
    "*T":"th",
    "*TD":"thed",
    "*S":"st",
    "*SZ":"c",
    "*D":"[y]",
    "*Z":"z",

    "F":"f",
    "FRP":"mp",
    "FRPB":"rch",
    "FRPBG":"nk",
    "FRPL":"mpl",
    "FRB":"mb",
    "FRL":"ml",
    "FRBL":"mbl",
    "FP":"ch",
    "FPL":"",
    "FB":"v",
    "FT":"ft",

    "R":"r", 
    "RB":"sh", #unless AU to make it rb carb barb
    "RBGT":"rket",
    "RBGTS":"rkets",

    "P":"p",
    "PB":"n",
    "PBLG":"j",
    "PBG":"ng",
    "PL":"m",

    "B":"b",
    "BG":"k",
    "BGT":"cket",
    "BGTS":"ckets",
    "BGS":"x",

    "L":"l",

    "G":"g",
    "GT":"ght",
    "GTS":"ghts",

    "T":"t",
    "TD":"ted",

    "S":"s", #might be some logic here for c? Realtime uses `SZ` for c
    "SZ":"ss",

    "D":"d",

    "Z":"s",

}



strokes_you_can_use_to_exit_shrimple_with=[

    #punctuation
    "TK-LS",    #no space
    "S-P",      #space
    "KPA",      #caps
    "KPA*",     #caps no space
    "R-R",      #enter
    "TP-PL",    #.
    "TA*B",     #can't remember
    "TPWA*",    #left hand tab
    #"R*",       #left hand return
    "KW-PL",    #?
    "TP-BG",    #o
    "KW-BG",    #,
    "AEZ",      #'s
    "A*ES",     #s'
    "AES",      #'s
    "HAERB",    ##
    "KWRA*T",   #@
    "P-P",      #.
    "H-N",      #-
    "H*N",      #-
    "TPHO*FRL", #normal
    "*",        #delete
    "PW*FP",    #control backspace
    "EFBG",     #escape
    "^*",
    "^S",
    "TKUPT",
    
    #navigation
    "STPH-R",
    "STPH-RB",
    "STPH-P",
    "STPH-B",
    "STPH-BG",
    "STPH-G",
    "STPH-FR",
    "STPH-LG",
    "PW-FP",
    
]

left_finger_chords_you_can_use_to_exit_shrimple_with={

    #Emily's stuff (might also have to do this for my phrasing too?)
    "SKWH",

    #Jeff's full phrasing
    "SWR",  #I
    "TWR",  #we
    "KPWR", #you
    "KWHR", #he
    "SKWHR",#she
    "KPWH", #it
    "TWH",  #they
    "STKH", #this
    "STKWH",#these
    "STWH", #that
    "STHR", #there
    "STPHR",#there
    #"STKPWHR",#null
    "STWR", #null

}

left_hand_chords_you_can_use_to_exit_shrimple_with={

    #Jeff's full phrasing
    "SWR",  #I
    "TWR",  #we
    "KPWR", #you
    "KWHR", #he
    "SKWHR",#she
    "KPWH", #it
    "TWH",  #they
    "STKH", #this
    "STKWH",#these
    "STWH", #that
    "STHR", #there
    "STPHR",#there
    "STKPWHR",#null
    "STWR", #null

    #Jeff's simple starters
    "STPA", #if
    "STHA", #that
    "SWH",  #when
    "SWHR", #where
    "SWHA", #what
    "SWHO", #who
    "SWHAO",#why
    "SWHRAO",#how
    "SPWH", #but
    "SKP",  #and
    "SKPR", #or

}


right_finger_chords_you_can_use_to_exit_shrimple_with={

    #Emily's stuff (might also have to do this for my phrasing too?)
    "LTZ"
}

left_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with=[
    #"KWR"
]

right_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with=[
    #"TZ"
]





































































import re

LONGEST_KEY = 40


def construct_every_combination(part_of_the_keyboard):
    """
    Given a set of options, left or right, up or down.
    Will return all combinations:
    left+up, left+down, right+up, right+down, etc.
    """
    
    path_direction=(part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys(),part_of_the_keyboard.keys())
    every_combination_dictionary={}
    every_combination = [[]]  # Initialize with empty list
    for length_of_combination in range(len(path_direction)):
        current_options = path_direction[length_of_combination]
        new_combinations = []  # Temporary list to store updated combinations

        for option in current_options:
            for existing_combination in every_combination:
                new_combination = existing_combination + [option]
                if re.fullmatch(r'(\^?S?T?K?P?W?H?R?)|(\*?F?\*?R?\*?P?\*?B?\*?L?\*?G?\*?T?\*?S?\*?D?\*?Z?)',"".join(new_combination)):
                    new_combinations.append(new_combination)

        every_combination.extend(new_combinations)  # Add new combinations

    for combination in every_combination:
        the_combination = "".join(combination)
        if the_combination.count("*")>1:
            continue

        if "*" in the_combination:
            the_combination= "*"+the_combination.replace("*","")
        translation=""
        for chord in combination:
            translation += part_of_the_keyboard[chord]
        if "[delete me]" in translation:
            continue
        if not the_combination in every_combination_dictionary:
            every_combination_dictionary[the_combination] = translation


    return every_combination_dictionary


if make_starter_letters_have_left_to_right_priority:
    reversed_starter_letters = {}
    for entry in starter_letter:
        reversed_starter_letters = dict({entry:starter_letter[entry]}, **reversed_starter_letters)
    starter_letter = reversed_starter_letters
starter_letter=(construct_every_combination(starter_letter))

if make_ender_letters_have_left_to_right_priority:
    reversed_ender_letters = {}
    for entry in ender_letter:
        reversed_ender_letters = dict({entry:ender_letter[entry]}, **reversed_ender_letters)
    ender_letter = reversed_ender_letters
ender_letter=(construct_every_combination(ender_letter))



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




def lookup(strokes):

    output_string= ""





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
                    return '{}'
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


        match = re.fullmatch(r'(#?\^?S?T?K?P?W?H?R?)(A?O?)(\*?\-?E?U?)(F?R?P?B?L?G?T?S?D?Z?)', stroke.replace(dedicated_key,""))
        if match:

            if match[1] in left_finger_chords_you_can_use_to_exit_shrimple_with:
                raise KeyError
            if match[1]+match[2] in left_hand_chords_you_can_use_to_exit_shrimple_with:
                raise KeyError
            if match[4] in right_finger_chords_you_can_use_to_exit_shrimple_with:
                raise KeyError

            print (match[1])
            if ((match[1] in left_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with) or (match[4] in right_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with)) and not stroke_number+1 == len(strokes):
                futurematch = re.fullmatch(r'(#?\^?S?T?K?P?W?H?R?)(A?O?)(\*?\-?E?U?)(F?R?P?B?L?G?T?S?D?Z?)', strokes[stroke_number+1].replace(dedicated_key,""))
                if not (futurematch[1] in left_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with or futurematch[4] in right_finger_chords_you_can_use_during_the_final_stroke_to_exit_shrimple_with):
                    raise KeyError


        if make_words_done_with_dedicated_key_exit_immediately and dedicated_key in strokes[0]:# and not "^" in strokes[0]:
            if stroke_number == 0 and not dedicated_key in stroke:
                raise KeyError
            elif not stroke_number == 0 and not (match[1] == joiner_strokes['left-hand joiner'] or match[4] == joiner_strokes["right-hand joiner"]):
                raise KeyError
            





    if (len(strokes)) == 1 and dedicated_key not in strokes[0]:
        if strokes[0]==entry_strokes['starterattached']:
            return ("{^}")
        else:
            return("{^ ^}")

    for stroke_number in range(len(strokes)):



        if not stroke_number == 0 and (strokes[stroke_number] in entry_strokes.values() or dedicated_key in strokes[stroke_number]):
            raise KeyError

        #match the strokes
        match= re.fullmatch(
            #dissect the string to starter_letters, vowels and ender_letters
            r'\+?(#?)(\^?S?T?K?P?W?H?R?)(A?O?\*?\-?E?U?)(F?R?P?B?L?G?T?S?D?Z?)',

            #this string:
            aericks_denumberizer(strokes[stroke_number].replace(dedicated_key,"")))

        if not match:
            raise KeyError



        start_thing=starter_letter[match[2]]
        if "*" in match[3]:
            end_thing=ender_letter["*"+match[4]]
            if end_thing == "":
                middle_thing=vowels[match[3]]
            else:
                middle_thing=vowels[match[3].replace("*","")]


        else:
            end_thing=ender_letter[match[4]]
            middle_thing=vowels[match[3].replace("*","")]

        #now do stuff with like [e]:
        if '[e]' in middle_thing:
            end_thing+="e"
            middle_thing=middle_thing.replace("[e]","")

        if '[y]' in end_thing:
            end_thing+="{^y}"
            end_thing=end_thing.replace("[y]","")


        if not stroke_number==0 or (dedicated_key in strokes[0]):
            if "#" in match[1]:
                output_string+=(
                    (start_thing+
                    middle_thing+
                    end_thing
                    ).capitalize())

            else:
                output_string+=(
                    start_thing+
                    middle_thing+
                    end_thing
                    )




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
#print(lookup(("KAPS", "WA*TD")))
#print(lookup(("KAPS", "WA*TD", "KWRAL")))
#print(lookup(("KAPS", "WA*TD", "KWRAL", "PAL")))


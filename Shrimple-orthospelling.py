"""
@Jalexu on discord had an idea for fingerspelling using the whole keyboard, not just one letter at a time
Key considerations were that it wasn't tailored for English, as this is mostly for foreign words/names


"""

starternormal = 'SP*'           #shrimple with normal formatting
starterattached='SW*'           #shrimple with not space at the start
startercap    = 'SHR*EUFRPL'    #shrimple but capped the first letter
acronyms      = 'KAPS'          #shrimple but all caps
dedicated_key = '+'             #Instead of a starter stroke



starter_letter={
    "" : "",

    "S" : "s",
    "STKPW": "z",
    "SKWR": "j",
    "SKHR": "shr",
    "SH" : "sh",
    "SR" : "v",

    "T" : "t",
    "TK": "d",
    "TKPW":"g",
    "TKR":"dr", #conflict with tc
    "TP": "f",
    "TPH": "n",

    "K":"k",
    "KP":"x",
    "KW":"q",
    "KWR":"y",
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


    "A"   :"a",
    "AO"  :"oo",
    "AOE" :"ee",
    "AOEU":"ie",
    "AOU" :"ue",
    "AE"  :"ea",
    "AEU" :"ai",
    "AU"  :"au",

    "O"   :"o",
    "OE"  :"oe",
    "OEU" :"oi",
    "OU"  :"ou",

    "E"   :"e",
    "EU"  :"i",

    "U"   :"u"
}


ender_letter={
    "":"",
    "*":"", #asterisk on its own is invalid
    "*FRPB":"nch",
    "*FT":"ft",
    "*PBG":"nk",
    "*PZ":"h",
    "PS":"h",
    "*BG":"ck",
    "*LG":"lk",
    "*T":"th",
    "*S":"st",
    "*SZ":"c",
    "*D":"y",
    "*DZ":"e",
    "*Z":"z",

    "F":"f",
    "FRP":"mp",
    "FRPB":"rch",
    "FRPL":"mpl",
    "FRB":"mb",
    "FRL":"ml",
    "FRBL":"mbl",
    "FP":"ch",
    "FB":"v",
    "FT":"st",

    "R":"r", 
    "RB":"sh", #unless AU to make it rb carb barb

    "P":"p",
    "PB":"n",
    "PBLG":"j",
    "PBG":"ng",
    "PL":"m",
    #PZ for h?

    "B":"b",
    "BG":"k",
    "BGS":"x",

    "L":"l",

    "G":"g",
    "GT":"xt",
    "GS":"tion", #Pretty English biased

    "T":"t",
    "TS":"ts",
    "TZ":"se",

    "S":"s", #might be some logic here for c? Realtime uses `SZ` for c
    "SD":"e",

    "D":"d",

    "Z":"e"

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
    "R*",       #left hand return
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
    
    #navigation
    "STPH-R",
    "STPH-RB",
    "STPH-P",
    "STPH-B",
    "STPH-BG",
    "STPH-G",
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
    "STKPWHR",#null
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







































































import re

LONGEST_KEY = 20


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

starter_letter=(construct_every_combination(starter_letter))
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

    if ((not strokes[0] == starternormal) and
        (not strokes[0] == startercap) and
        (not strokes[0] == starterattached) and
        (not strokes[0] == acronyms) and
        (not dedicated_key in strokes[0])):
        raise KeyError
    
    output_string=""

    for stroke in strokes:
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
        



    if (len(strokes)) == 1 and dedicated_key not in strokes[0]:
        if strokes[0]==starterattached:
            return ("{^}")
        else:
            return("{^ ^}")

    for stroke_number in range(len(strokes)):

        if ((not stroke_number ==0 and strokes[stroke_number] == starternormal) or
            (not stroke_number ==0 and strokes[stroke_number] == starterattached) or
            (not stroke_number ==0 and strokes[stroke_number] == startercap) or
            (not stroke_number ==0 and strokes[stroke_number] == acronyms) or
            (not stroke_number ==0 and dedicated_key in strokes[stroke_number])):
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




    if strokes[0] == startercap:
        return output_string.capitalize()
    if strokes[0] == acronyms:
        return output_string.upper()
    if strokes[0] == starterattached:
        return "{^^}"+output_string
    return output_string



"""
@Jalexu on discord had an idea for fingerspelling using the whole keyboard, not just one letter at a time
Key considerations were that it wasn't tailored for English, as this is mostly for foreign words/names


"""

starterstroke = 'SHREUFRPL'   #if you don't have Lapwing's plug-in, #T will have to be 2
startercap = 'SHR*EUFRPL'
acronyms = 'KAPS'



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
    #"TKR":"dr",
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
    "PHR":"pl", #I've decided not mr

    "W":"w",

    "H":"h",
    "HR":"l",

    "R":"r"
}



vowels={
    "-":"",
    
    "":"",

    "*":"",

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
    "*BGS":"ction",
    "*T":"th",
    "*S":"c",
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
    "RBT":"tial",
    "RBS":"tious",

    "P":"p",
    "PB":"n",
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

    if ((not strokes[0] == starterstroke) and
        (not strokes[0] == startercap) and
        (not strokes[0] == acronyms)):
        raise KeyError
    
    output_string=""

    for stroke in strokes:
        if stroke=="+":
            raise KeyError

        #punctuation
        if stroke=="TK-LS":
            raise KeyError
        if stroke=="S-P":
            raise KeyError
        if stroke=="KPA":
            raise KeyError
        if stroke=="KPA*":
            raise KeyError
        if stroke=="R-R":
            raise KeyError
        if stroke=="TP-PL":
            raise KeyError
        if stroke=="KW-PL":
            raise KeyError
        if stroke=="TP-BG":
            raise KeyError
        if stroke=="KW-BG":
            raise KeyError
        if stroke=="AEZ":
            raise KeyError
        if stroke=="A*ES":
            raise KeyError
        if stroke=="AES":
            raise KeyError
        if stroke=="HAESH":
            raise KeyError
        if stroke=="KWRA*T":
            raise KeyError
        if stroke=="P-P":
            raise KeyError
        if stroke=="H-N":
            raise KeyError
        if stroke=="H*N":
            raise KeyError
        if stroke=="TPHO*FRL":
            raise KeyError
        
        #navigation
        if stroke=="STPH-R":
            raise KeyError
        if stroke=="STPH-RB":
            raise KeyError
        if stroke=="STPH-P":
            raise KeyError
        if stroke=="STPH-B":
            raise KeyError
        if stroke=="STPH-BG":
            raise KeyError
        if stroke=="STPH-G":
            raise KeyError
        if stroke=="PW-FP":
            raise KeyError
        
        #Emily's stuff (might also have to do this for my phrasing too?)
        if "SKWH"in stroke:
            raise KeyError
        if "LTZ" in stroke:
            raise KeyError

    if (len(strokes)) == 1:
        return(" ")

    for stroke_number in range(len(strokes)):

        if ((not stroke_number ==0 and strokes[stroke_number] == starterstroke) and
            (not stroke_number ==0 and strokes[stroke_number] == startercap) and
            (not stroke_number ==0 and strokes[stroke_number] == acronyms)):
            raise KeyError

        #match the strokes
        match= re.fullmatch(
            #dissect the string to starter_letters, vowels and ender_letters
            r'(#?)(\^?S?T?K?P?W?H?R?)(A?O?\*?\-?E?U?)(F?R?P?B?L?G?T?S?D?Z?)',

            #this string:
            aericks_denumberizer(strokes[stroke_number]))

        if not match:
            raise KeyError

        start_thing=starter_letter[match[2]]
        if "*" in match[3]:
            end_thing=ender_letter["*"+match[4]]
            #if not end_thing:
            #    raise KeyError
        else:
            end_thing=ender_letter[match[4]]
        middle_thing=vowels[match[3].replace("*","")]

        if not stroke_number==0:
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
    return output_string




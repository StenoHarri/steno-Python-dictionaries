import re
import json





#The last dictionary, overwrites the previous dictionary
list_of_dictionaries = ["Plover_main_without_compound_words", #Lowest priority
                        "Lapwing",
                        "Lapwing_UK",
                        "Harri_additions_with_Lapwing_logic",
                        "Jos+Mir-Plover",
                        "Harri_additions_with_Josiah_logic",
                        "Harri_additions_with_Lapwing&Josiah_logic",
                        "Harri_additions_with_Jeff_logic",
                        "Harri_personal_titles",
                        "Harri_personal_biology",
                        "Harri_personal_one_handed_fingerspelling",
                        "Harri_personal_subscript",
                        "st_ft_switching",
                        "make_z_use_asterisk-Z",
                        "Harri_personal_user"] #Highest priority











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




def collapse_outlines(dictionary_file, collapsed_dictionary = {}, force_cap=False):
    #The latest addition overwrites the previous entry at that location
    with (open(dictionary_file, "r", encoding="utf-8")) as temp_dictionary:                                        #debug
    #with (open('C:\\Users\\harrry\\AppData\\Local\\plover\\plover\\' + dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Windows
    #with (open("Library/Application Support/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Macintosh
    #with (open(".config/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary:                      #Linux
        temp_dictionary = json.load(temp_dictionary)
        for outline in temp_dictionary:
            translated_phrase = temp_dictionary[outline]
            if force_cap:
                if translated_phrase[0] == "{":
                    translated_phrase = "{" + translated_phrase[1].upper() + translated_phrase[2:]
                else:
                    translated_phrase = translated_phrase[0].upper() + translated_phrase[1:]
            
            outline = aericks_denumberizer(outline)


            """
            
            Here, it's these following 'if' statements you want to change
            Stroke is something like "A/PHAEUZ"
            Outline is something like "amaze"


            v stands for vowel, X stands for start/end of string
            Fold (Must start)(Will replace)(Must be followed with)
            This replaces that
            #  =                          ([^STKPWHRAO[\*]EU-].*)
            v stands for vowel
            Rv/   → +   = (.*[/X]#?)      (R[AOEU]+\/)   (.*)
            vL/   → +   = (.*[/X]#?)      ([AOEU]+L\/)   (.*)
            [removed] EBGS/ → 😦  = (.*[/X]#?\+?)   (EBGS\/)       (.*)
            v/    → ^   = (.*[/X]#?\+?)   ([AOEU]+\/)    ([STKPWHRAO\*EU-].*)
            v/    → ^   = (.*[/X]#?\+?)   ([AOEU]+\/)    ([STKPWHRAO\*EU-].*)
            vS/   → ^S  = (.*[/X]#?\+?)   ([AOEU]+S\/)   ([TKPWHRAO\*EU-].*)
            EFT/  → ^ST = (.*[/X]#?\+?)   ([AOEU]+BGS\/) ([KPWHRAO\*EU-].*)
            vBGS/ → ^SK = (.*[/X]#?\+?)   ([AOEU]+S\/)   ([TKPWHRAO\*EU-].*)
            vBGS/K→ ^SK = (.*[/X]#?\+?)   ([AOEU]+S\/)   ([TKPWHRAO\*EU-].*)
            vT/   → ^T  = (.*[/X]#?\+?)   ([AOEU]+T\/)   ([KPWHRAO\*EU-].*)
            vD/   → ^TK = (.*[/X]#?\+?)   ([AOEU]+D\/)   ([PWHRAO\*EU-].*)
            vPB/K → ^TKP= (.*[/X]#?\+?)   ([AOEU]+PB\/K) ([WHRAO\*EU-].*)
            vF/   → ^TP = (.*[/X]#?\+?)   ([AOEU]+F\/)   ([WHRAO\*EU-].*)
            vBG/  → ^K  = (.*[/X]#?\+?)   ([AOEU]+BG\/)  ([PWHRAO\*EU-].*)
            vP/   → ^P  = (.*[/X]#?\+?)   ([AOEU]+P\/)   ([WHRAO\*EU-].*)
            vB/   → ^PW = (.*[/X]#?\+?)   ([AOEU]+B\/)   ([HRAO\*EU-].*)
            TKEUS/→ STK = (.*[/X]#?\+?\^?)(TKEUS\/)      ([PWHRAO\*EU-].*)
            ee/   → SK  = (.*[/X]#?\+?\^?)(AOE|E)\/      ([PWHRAO\*EU-].*)

            Interfixes
            S* → STKPW =(.*)  S([HRAO]*)\*      (.*)
            TP*→ TP    =(.*)  TP([WHRAO]*)\*    (.*)
            F  → FB    =(.*)  ([AOEU*-]+)F      ([LGTSDZ/X].*)
            



            Suffixes:
            /KWREU     → *D    = (.*[/X])([#+^STKPWHRAO]+)([EU\-FRPBLGTS]+)\/KWREU([/X].*)
            PL/TPHAEUT → FRPBT = (.*[/X])([#+^STKPWHRAOEU\-]+)(PL)\/TPHAEUT([/X].*)
            PL/TPHAEUBGS→FRPBGS= (.*[/X])([#+^STKPWHRAOEU\-]+)(PL)\/TPHAEUBGS([/X].*)
            /PHEUBG    → FRBG  = (.*[/X])([#+^STKPWHRAOEU\-]+)(\/PHEUBG)([/X].*)
            /SKWRO(*)  → ^     = (.*[/X]#?\+?)([STKPWHRAO\-*EUFRPBLGTSDZ]*/)(SKWRO[\*]?)([/X].*)
            /KWRO(E)   → ^     = (.*[/X]#?\+?)([STKPWHRAO\-*EUFRPBLGTSDZ]*/)(KWRO[E]?)([/X].*)
            /RO(E)     → ^R    = (.*[/X]#?\+?)([STKPWHRAO\-*EUFPBLGTSDZ]*/)(RO[E]?)([/X].*)
            /HRAEUGS   → LGS   = (.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?F?R?P?B?)(/HRAEUGS)([/X].*)

            /KHUR      → FRP   = (.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?)(/KHUR)([/X].*)
            BG/KHUR    → *FRP  = (.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?)(BG/KHUR)([/X].*)
            #PL/vPB     →FRPB


            Not added
            #^STKP=(.*[/X]#?\+?)  ([AOEU]+PB\/SKWR)([AO\*EU-].*)            ^STKPW → Vng- (*BLT)
            #^STKPW=(.*[/X]#?\+?)  ([AOEU]+PBG\/)([AO\*EU-].*)
            #EBG/S→+  = (.*\/#?)      (EBG\/S)       ([TKPWHRAO\*EU-].*) #only Lapwing really does this... this overfitting for sure

            """

            unchecked_outlines_to_add = ['X' + str(outline) + 'X']
            checked_outlines_to_add = []
            while unchecked_outlines_to_add:
                working_outline =  unchecked_outlines_to_add.pop()

                ## this is adding a # to words that are capped (Lapwing theory)
                if len(translated_phrase) > 1:
                    if translated_phrase[0].isupper():
                        match = re.fullmatch(r'X?([\+\^STKPWHRAO\*EU-].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append("X#" + match[1])
                    elif translated_phrase[1].isupper():
                        match = re.fullmatch(r'X?\{([\+\^STKPWHRAO\*EU-].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append("X{#" + match[1])

                #Rv/   → +
                #match = re.fullmatch(r'(.*[/X]#?)(R[AOEU]+\/)(.*)', working_outline)
                #if match:
                #    unchecked_outlines_to_add.append(match[1] + "+" + match[3])
                #vL/   → +
                #match = re.fullmatch(r'(.*[/X]#?)([AOEU]+L\/)(.*)', working_outline)
                #if match:
                #    unchecked_outlines_to_add.append(match[1] + "+" + match[3])
                #EBGS/ → +
                #match = re.fullmatch(r'(.*[/X]#?\+?)(EBGS\/)(.*)', working_outline)
                #if match:
                #    unchecked_outlines_to_add.append(match[1] + "+" + match[3])
                #v/    → ^
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+\/)([STKPWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^" + match[3])
                #vS/   → ^S
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+S\/)([TKPWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^S" + match[3])
                #vFT/  → ^ST
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+FT\/)([KPWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^ST" + match[3])
                #vBGS/  → ^SK
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BGS\/)([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^SK" + match[3])
                #vBGS/K → ^SK
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BGS\/K)([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^SK" + match[3])
                #vT/   → ^T
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+T\/)([KPWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^T" + match[3])
                #vD/   → ^TK
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+D\/)([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^TK" + match[3])
                #vPB/K → ^TKP
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+PB\/K)([WHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^TKP" + match[3])
                #vF/   → ^TP
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+F\/)([WHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^TP" + match[3])
                #vBG/  → ^K
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BG\/)([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^K" + match[3])
                #vP/   → ^P
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+P\/)([WHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^P" + match[3])
                #vB/   → ^PW
                match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+B\/)([HRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^PW" + match[3])
                #TKEUS/→ STK
                match = re.fullmatch(r'(.*[/X]#?\+?\^?)(TKEUS\/)([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "STK" + match[3])
                #ee/   → SK
                match = re.fullmatch(r'(.*[/X]#?\+?\^?)(AOE|E|EU)\/([PWHRAO\*EU-].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "SK" + match[3])

                #Infixes
                #S* → STKPW
                #if "z" in translated_phrase.lower():
                #    match = re.fullmatch(r'(.*[\/X])S([HRAO]*)\*(.*)', working_outline)
                #    if match:
                #        unchecked_outlines_to_add.append(match[1] + "STKPW" + match[2] + match[3])
                #TP*→ TP
                if "ph" in translated_phrase.lower():
                    match = re.fullmatch(r'(.*[\/X])TP([WHRAO]*)\*(.*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "TP" + match[2] + match[3])
                #F  → FB
                if "v" in translated_phrase.lower() and not "rv" in translated_phrase.lower():
                    match = re.fullmatch(r'(.*[\/X])([AOEU*-]+)F([LGTSDZ\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + match[2] + "FB"  + match[3])

                #S(*)/KP(*)/SK(*)/SP(*) → ^SK
                if "ex" in translated_phrase.lower():
                    #S
                    match = re.fullmatch(r'(.*[\/X])S(P?W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                        #S*
                        match = re.fullmatch(r'(.*[\/X])S(P?W?H?R?A?O?)\*([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                    #KP
                    match = re.fullmatch(r'(.*[\/X])KP(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                        #KP*
                        match = re.fullmatch(r'(.*[\/X])KP(W?H?R?A?O?)\*([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                    #SK
                    match = re.fullmatch(r'(.*[\/X])SK(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                        #SK*
                        match = re.fullmatch(r'(.*[\/X])SK(W?H?R?A?O?)\*([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                    #SP
                    match = re.fullmatch(r'(.*[\/X])SP(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                        #SP*
                        match = re.fullmatch(r'(.*[\/X])SP(W?H?R?A?O?)\*([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])


                #Suffixes
                #/KWREU     → *D
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAO]+)([EU\-FRPBLGTS]+)\/KWREU([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "D" + match[3])
                #/HREU      → *LD
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAO]+)([EU\-FRPB]+)\/HREU([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "LD" + match[3])
                #/HRAOEU    → *LD
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAO]+)([EU\-FRPB]+)\/HRAOEU([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "LD" + match[3])
                #PL/TPHAEUT → FRPBT
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAOEU\-]+)(PL)\/TPHAEUT([/X].*)', working_outline)
                if match: #^HRAOUPL/TPHAEUT
                    unchecked_outlines_to_add.append(match[1] + "FRPBT" + match[3])
                #PL/TPHAEUBGS→FRPBGS
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAOEU\-]+)(PL)\/TPHAEUGS([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "FRPBGS" + match[3])
                #/PHEUBG    → FRBG
                match = re.fullmatch(r'(.*[/X][#\+\^STKPWHRAOEU\-]+)(\/PHEUBG)([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "FRBG" + match[3])
                #/SKWRO(*)  → ^
                match = re.fullmatch(r'(.*[/X][#+]*)([STKPWHRAO\-*EUFRPBLGTSDZ]*)/SKWRO[*]?([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^" + match[2] + match[3])
                #/KWRO(E)   → ^
                match = re.fullmatch(r'(.*[/X][#+]*)([STKPWHRAO\-*EUFRPBLGTSDZ]*)/KWRO[E]?([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^" + match[2] + match[3])
                #/RO(E)     → ^R
                match = re.fullmatch(r'(.*[/X]#?\+?)([STKPWHRAO\-*EUF]*)([PBLGTSDZ]*/)(RO[E]?)([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "R" + match[3] + match[4])
                #^HR
                match = re.fullmatch(r'(.*[/X]#?\+?)(S?T?K?P?W?H?R?A?O?\-?\*?E?U?F?R?P?B?)/HRO[E]?([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "L" + match[3])
                #/HRAEUGS   → LGS
                match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?F?R?P?B?)/HRAEUGS([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "LGS" + match[2])
                #LT
                match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?F?R?P?B?)/KWRALT([/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "LT" + match[2])
                #/KHUR      → FRP
                match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?A?O?\-?\*?E?U?)/KHUR([T?S?D?Z?/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "LT" + match[2])
                #BG/KHUR    → *FRP
                match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?A?O?)\-?(E?U?)BG/KHUR([T?S?D?Z?/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "FRP" + match[3])
                checked_outlines_to_add.append(working_outline)
                ###########check for duplicates
                unchecked_outlines_to_add =  list(set(unchecked_outlines_to_add) - set(checked_outlines_to_add))
                #PL/vPB     →FRPB
                match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?A?O?E?U?)PL/[AOEU]+PB([L?G?T?S?D?Z?/X].*)', working_outline)
                if match:
                    unchecked_outlines_to_add.append(match[1] + "FRPB" + match[2])
                checked_outlines_to_add.append(working_outline)
                ###########check for duplicates
                unchecked_outlines_to_add =  list(set(unchecked_outlines_to_add) - set(checked_outlines_to_add))

            checked_outlines_to_add.pop(0) #The original outline is valid but like, obviously I've already got it
            length = 0
            for um_outline in checked_outlines_to_add:
                collapsed_dictionary[str(um_outline.replace("X",''))] = translated_phrase
            
    return collapsed_dictionary




collapsed_dictionary = {}
reverse_lookup_dictionary = {}
#I need to replace this with just reading the plover.cfg file

#Send everything through capped and add #
for dictionary in list_of_dictionaries:
    collapsed_dictionary = collapse_outlines(dictionary + ".json", collapsed_dictionary, True)
#Send everything through normally
for dictionary in list_of_dictionaries:
    collapsed_dictionary = collapse_outlines(dictionary + ".json", collapsed_dictionary)




#reverse_dictionary = {translated_phrase:outline for outline,translated_phrase in collapsed_dictionary.items()} 

#collapsed_dictionary['-PG'] = str(len(collapsed_dictionary))


def lookup(strokes):

    outline = "/".join(strokes)
    if any(single_digit_number in "0123456789" for single_digit_number in outline):
        outline = "#" + convert_steno_numbers_to_steno_keys(outline)

    return collapsed_dictionary[outline]

with open("collapsed_dictionaries.json", "w") as outfile:
    json.dump(collapsed_dictionary, outfile)

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

"""
Autobriefer
Read your current dictionary outlines and apply regex rules and output an autobriefed dictionary.json
"""

#1 is read them all, 500 is read one in every 500. Purely visual so you have something to watch while running, as requested by @Field
stare_mode = 500


make_schwa_use_the_number_key_actually = False

folding_rules = {
    #Not theory specific
    'drop linking vowels': False,

    #Lapwing
    'numberkey_capping' : False,
    'dis/ → STK-'       : False,
    '/-lation → -LGS'   : False,
    'y → KWH-'          : False,

    #Plover
    '-m/ → -FR (when PL is taken)'     : False,
    'ph → TP-'          : False, #Lapwing uses TP*

    #Josiah
    'vowel/ → ^-'       : False,
    '/-y → *D'          : False,

    #Grahp
    '/-dy → *D'         : False,

    #Harri
    'ex/ → ^SK-'        : False,
    'v  → -FB'          : False,    #Josiah uses this for conflicts
    'z → STKPW-'        : False,
    '/-chure → -FRP'    : False,
    '/-ckchure → *FRP'  : False,
    '^ for words ending in o' : False, #Breaks steno order but I love it
    'inter → EURPBT'    : False,
    'KHUR → KHAOUR'     : False,

    #HelloChap
    '/-ddle → -BL'      : False
}

include_input_dictionaries = False


#The last dictionary, overwrites the previous dictionary
list_of_dictionaries = [#"2/autobriefed",
                        "1/Plover_main(made Lapwing friendly)", #Lowest priority
                        "4/lapwing-base",
                        "4/Lapwing_commands",
                        "4/lapwing-uk-additions",
                        "4/lapwing-proper-nouns",
                        "1/Lapwing_additions",
                        "4/Josiah",
                        "1/Josiah_additions",
                        "1/Josiah&Lapwing_additions",
                        #"2/Harri_phrasing",
                        "2/Just",
                        "1/Jeff_additions",
                        "2/Harri_titles",
                        "1/Harri_doubles",
                        "1/Harri_biology",
                        "2/dinosaurs",
                        "2/Harri_one_handed_fingerspelling",
                        "2/inconsistencies/Harri_asteris-S for ss",
                        "2/inconsistencies/Harri_asterisk-Z for z",
                        "2/inconsistencies/Harri_GT for ght",
                        "2/inconsistencies/Harri_st and ft",
                        "2/inconsistencies/dle using -lgdz",
                        "2/inconsistencies/interintroflipping",
                        "Harri_starters",
                        "2/Harri_user",
                        #"Harri_numbers_for_Javelin",
                        #"+",
                        #"2/Harri_raw"
                        ] #Highest priority



#You don't have to look any further






















LONGEST_KEY = 4

import re
import json
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




def dictionary_briefer(dictionary_file, briefed_dictionary = {}, folding_rules ={}, comparison_dictionary = {}, stare_mode=False, force_cap=False):
    #The latest addition overwrites the previous entry at that location
    with (open(dictionary_file, "r", encoding="utf-8")) as temp_dictionary_name:                                        #debug
    #with (open('C:\\Users\\harrry\\AppData\\Local\\plover\\plover\\' + dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Windows
    #with (open("Library/Application Support/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary: #Macintosh
    #with (open(".config/plover/"+ dictionary_file, "r", encoding="utf-8")) as temp_dictionary:                      #Linux
        temp_dictionary = json.load(temp_dictionary_name)
        stare_number=0
        for outline in temp_dictionary:
            translated_phrase = temp_dictionary[outline]

            
            #This caps stuff if force_cap is on
            if force_cap and (not translated_phrase == ''):
                if translated_phrase[0] == "{":
                    translated_phrase = "{" + translated_phrase[1].upper() + translated_phrase[2:]
                else:
                    translated_phrase = translated_phrase[0].upper() + translated_phrase[1:]

            outline = aericks_denumberizer(outline)

            


            """
            Here, it's these following 'if' statements you want to change
            Stroke is something like "A/PHAEUZ"
            Outline is something like "amaze"
            """

            unchecked_outlines_to_add = ['X' + str(outline) + 'X']
            checked_outlines_to_add = []
            while unchecked_outlines_to_add:
                working_outline =  unchecked_outlines_to_add.pop()

                # this is adding a # to words that are capped (Lapwing theory)
                if folding_rules['numberkey_capping']:
                    if len(translated_phrase) > 1:
                        if translated_phrase[0].isupper():
                            match = re.fullmatch(r'X?([\+\^STKPWHRAO\*EU-].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append("X#" + match[1])
                        elif translated_phrase[1].isupper():
                            match = re.fullmatch(r'X?\{([\+\^STKPWHRAO\*EU-].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append("X{#" + match[1])
                if folding_rules['dis/ → STK-']:
                    #TKEUS/→ STK
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?)(TKEUS\/)([PWHRAO\*EU-].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "STK" + match[3])
                    #TKES/→ STK
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?)(TKES\/)([PWHRAO\*EU-].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "STK" + match[3])
                if folding_rules['/-lation → -LGS']:
                    #Suffixes
                    #/HRAEUGS   → -LGS
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?B?)/HRAEUGS([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "LGS" + match[2])
                    #/KWRALT    → -LT
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?B?)/KWRALT([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "LT" + match[2])

                if folding_rules['y → KWH-']:
                    #
                    if "y" in translated_phrase.lower():
                        if "y" in translated_phrase[0]:
                            match = re.fullmatch(r'(X#?\+?\^?)KWR(A?O?)\*?(E?U?F?R?P?B?L?G?T?S?D?Z?[/X].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append(match[1] + "KWH" + match[2] + match[3])

                        else:
                            if re.fullmatch(r'(.*y[aeiou].*)', translated_phrase.lower()):
                                match = re.fullmatch(r'(.*[/X]#?\+?\^?)KWR(A?O?)\*(E?U?F?R?P?B?L?G?T?S?D?Z?[/X].*)', working_outline)
                                if match:
                                    unchecked_outlines_to_add.append(match[1] + "KWH" + match[2] + match[3])



                if folding_rules['-m/ → -FR (when PL is taken)']:
                    #PL/TPHAEUT → -FRPBT
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(PL)\/TPHAEUT([/X].*)', working_outline)
                    if match: #^HRAOUPL/TPHAEUT
                        unchecked_outlines_to_add.append(match[1] + "FRPBT" + match[3])
                    #PL/TPHAEUBGS→-FRPBGS
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(PL)\/TPHAEUGS([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRPBGS" + match[3])

                    #PL/KWREUBG → -FRBG
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(PL)\/[KWR]*[AOEU]+BG([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRBG" + match[3])

                    #PL/KWRAL → -FRL
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(PL)\/[KWRAOEU]*L([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRL" + match[3])

                    #PL/KWRAPBLG → -FRPBLG
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(PL)\/[KWR]*[AOEU]+PBLG([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRPBLG" + match[3])

                    #/PHEUBG    → -FRBG
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)(\/PHEUBG)([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRBG" + match[3])
                    
                    #Suffixes
                    #PL/vPB     → -FRPB
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?E?U?)PL/[AOEU\*\-]+PB([L?G?T?S?D?Z?/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRPB" + match[2])
                if folding_rules['ph → TP-']:
                    #TP*→ TP
                    if "ph" in translated_phrase.lower():
                        match = re.fullmatch(r'(.*[\/X]#?\+?\^?S?)TP([WHRAO]*)\*(.*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "TP" + match[2] + match[3])
                if folding_rules['vowel/ → ^-']:
                    #Prefixes
                    #v/   → ^
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+\/)([STKPWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[3])
                    #vS/   → ^S
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+S\/)([TKPWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^S" + match[3])
                    #vFT/  → ^ST
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+FT\/)([KPWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^ST" + match[3])
                    #vBGS/  → ^SK
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BGS\/)([PWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[3])
                    #vBGS/T → ^SK
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BGS\/T)([PWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[3])
                    #vBGS/K → ^SK
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BGS\/K)([PWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^SK" + match[3])
                    #vT/   → ^T
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+T\/)([KPWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^T" + match[3])
                    #vD/   → ^TK
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+D\/)([PWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^TK" + match[3])
                    #vPB/K → ^TKP
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+PB\/K)([WHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^TKP" + match[3])
                    #vF/   → ^TP
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+F\/)([WHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^TP" + match[3])
                    #vBG/  → ^K
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+BG\/)([PWHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^K" + match[3])
                    #vP/   → ^P
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+P\/)([WHRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^P" + match[3])
                    #vB/   → ^PW
                    match = re.fullmatch(r'(.*[/X]#?\+?)([AOEU]+B\/)([HRAO\*EU].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^PW" + match[3])
                if folding_rules['/-y → *D']:
                    #Suffixes
                    #/KWREU     → *D
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)\-?(E?U?F?R?P?B?L?G?T?S?)\/KWREU([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "D" + match[3])
                    #/HREU      → *LD
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)\-?(E?U?F?R?P?B?)\/HREU([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "LD" + match[3])
                    #/HRAOEU    → *LD
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)([EU\-FRPB]*)\/HRAOEU([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + str(match[2]).replace("-","") + "LD" + match[3])
                    #/SEU    → *FD
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)([EU\-]*)\/SEU([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + str(match[2]).replace("-","") + "FD" + match[3])
                if folding_rules['ex/ → ^SK-']:
                    #S(*)/KP(*)/SK(*)/SP(*) → ^SK
                    if "ex" in translated_phrase.lower():
                        #S
                        match = re.fullmatch(r'(.*[\/X]#?\+?)S(P?W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                            #S*
                            match = re.fullmatch(r'(.*[\/X]#?\+?)S(P?W?H?R?A?O?)\*([\/X].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                        #KP
                        match = re.fullmatch(r'(.*[\/X]#?\+?)KP(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                            #KP*
                            match = re.fullmatch(r'(.*[\/X]#?\+?)KP(W?H?R?A?O?)\*([\/X].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                        #SK
                        match = re.fullmatch(r'(.*[\/X]#?\+?)SK(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                            #SK*
                            match = re.fullmatch(r'(.*[\/X]#?\+?)SK(W?H?R?A?O?)\*([\/X].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                        #SP
                        match = re.fullmatch(r'(.*[\/X]#?\+?)SP(W?H?R?A?O?-?\*?[\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^SK" + match[2])
                            #SP*
                            match = re.fullmatch(r'(.*[\/X]#?\+?)SP(W?H?R?A?O?)\*([\/X].*)', working_outline)
                            if match:
                                unchecked_outlines_to_add.append(match[1] + "^SK" + match[2] + match[3])
                if folding_rules['v  → -FB']:
                    #Infixes
                    #F  → FB
                    if "covenant" in translated_phrase:
                        print("here")
                    if "v" in translated_phrase.lower() and not "rv" in translated_phrase.lower() and not " " in translated_phrase:
                        match = re.fullmatch(r'(.*)([AOEU*-]+)F([LGTSDZ\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + match[2] + "FB"  + match[3])
                if folding_rules['z → STKPW-']:
                    #Infixes
                    #S* → STKPW
                    if "z" in translated_phrase.lower():
                        match = re.fullmatch(r'(.*[\/X]#?\+?\^?)S([HRAO]*)\*(.*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "STKPW" + match[2] + match[3])
                if folding_rules['/-chure → -FRP']:
                    #/KHUR      → -FRP
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?[AO\-\*EU]+)/KHUR(B?L?G?T?S?D?Z?[/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "FRP" + match[2])
                if folding_rules['/-ckchure → *FRP']:
                    #BG/KHUR    → *FRP
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)\-?(E?U?)BG/KHUR(T?S?D?Z?[/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + match[2] + "FRP" + match[3])
                if folding_rules['^ for words ending in o']:
                    #suffixes
                    #/SKWRO(*)  → ^
                    match = re.fullmatch(r'(.*[/X][#+]*)(S?T?K?P?W?H?R?A?O?E?U?\-?F?R?P?B?L?G?T?S?D?Z?)/SKWRO[*]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + match[3])
                    #/KWRO(E)   → ^
                    match = re.fullmatch(r'(.*[/X][#+]*)(S?T?K?P?W?H?R?A?O?E?U?\-?F?R?P?B?L?G?T?S?D?Z?)/KWRO[E]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + match[3])
                    #/RO(E)     → ^-R
                    match = re.fullmatch(r'(.*[/X]#?\+?)(S?T?K?P?W?H?R?[AO\-\*EU]+F?)([PBLGTSDZ]*)/RO[E]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "R" + match[3] + match[4])
                    #^HR        → ^-L
                    match = re.fullmatch(r'(.*[/X]#?\+?)(S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?B?)/HRO[E]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "L" + match[3])
                    #BG/SO(E) → -BGS/^
                    match = re.fullmatch(r'(.*[/X]#?\+?)(S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?)BG/SO[E]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "S" + match[3])
                    #TO[E] → ^-T
                    match = re.fullmatch(r'(.*[/X]#?\+?)(S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?B?L?G?)/TO[E]?([/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "^" + match[2] + "T" + match[3])
                if folding_rules['inter → EURPBT']:
                    if "inter" in translated_phrase.lower():
                        #EUPBT ↑ EURPBT
                        match = re.fullmatch(r'(.*[\/X])EUPBT([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "EURPBT" + match[2])
                    if "intro" in translated_phrase.lower():
                        #EUPBT ↑ EURPBT
                        match = re.fullmatch(r'(.*[\/X])EURPBT([\/X].*)', working_outline)
                        if match:
                            unchecked_outlines_to_add.append(match[1] + "^EURPBT" + match[2])
                if folding_rules['KHUR → KHAOUR']:
                    match = re.fullmatch(r'(.*)KHUR(.*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "KHAOUR" + match[2])

                if folding_rules['/-dy → *D']:
                    match = re.fullmatch(r'(.*[/X]#?\+?\^?S?T?K?P?W?H?R?A?O?)-?(E?U?F?R?P?B?L?G?T?S?D)/KWREU(S?[\/X].*)', working_outline)
                    if match:
                        unchecked_outlines_to_add.append(match[1] + "*" + match[2])

                if folding_rules['/-ddle → -BL']:
                    match = re.fullmatch(r'(.*[/X]#?\+?S?T?K?P?W?H?R?[AO\-\*EU]+F?R?P?)D/-L(.*)', working_outline)
                    if match:
                        print(translated_phrase + " " + match[1] + "BL" + match[2])
                        unchecked_outlines_to_add.append(match[1] + "BL" + match[2])

                checked_outlines_to_add.append(working_outline)
                ###########check for duplicates
                unchecked_outlines_to_add =  list(set(unchecked_outlines_to_add) - set(checked_outlines_to_add))



            for checked_outline_to_add in checked_outlines_to_add:

                    if make_schwa_use_the_number_key_actually:
                        briefed_outline = str(checked_outline_to_add.replace("/X","X").replace("X",'').replace('^','#').replace("//","/"))
                    else:
                        briefed_outline = str(checked_outline_to_add.replace("/X","X").replace("X",'').replace("//","/"))
                    


                    if not briefed_outline in comparison_dictionary and not '##' in briefed_outline:
                        briefed_dictionary[briefed_outline] = translated_phrase
                        
                        if stare_mode:
                            if not stare_number % stare_mode:

                                #print(translated_phrase+'\t'+outline+'\tinto '+briefed_outline)

                                print(f"{translated_phrase:<25} {outline:<25} into\t"+briefed_outline)
                            stare_number+=1




    return briefed_dictionary




briefed_dictionary = {}
reverse_lookup_dictionary = {}

#Send everything just to squish
comparison_dictionary = {}

print('Writing comparison dictionary')
for dictionary in list_of_dictionaries:
    with (open(dictionary+'.json', "r", encoding="utf-8")) as temp_dictionary:
        comparison_dictionary.update(json.load(temp_dictionary))



if folding_rules['numberkey_capping']:
    print('Writing capped up dictionary')
    for dictionary in list_of_dictionaries:
        with (open(dictionary+'.json', "r", encoding="utf-8")) as temp_dictionary:
            uncapped_dictionary = (json.load(temp_dictionary))
            for entry in uncapped_dictionary:
                briefed_dictionary[('#'+entry).replace('##','#')] = uncapped_dictionary[entry].capitalize()


if include_input_dictionaries:
    briefed_dictionary = comparison_dictionary

if make_schwa_use_the_number_key_actually:
    outlines_to_delete=[]
    for outline in briefed_dictionary:
        if "^" in outline:
            outlines_to_delete.append(outline)
    for outline in outlines_to_delete:
        del briefed_dictionary[outline]

#Send everything through normally
for dictionary in list_of_dictionaries:
    print('\n\ncurrently briefing '+dictionary)
    briefed_dictionary = dictionary_briefer(dictionary + ".json", briefed_dictionary, folding_rules, comparison_dictionary, stare_mode)

if folding_rules['numberkey_capping']:
    print('Capping the new briefs')
    for dictionary in list_of_dictionaries:
        with (open(dictionary+'.json', "r", encoding="utf-8")) as temp_dictionary:
            uncapped_dictionary = (json.load(temp_dictionary))
            for entry in uncapped_dictionary:
                if not entry.startswith('#'):
                    briefed_dictionary['#'+entry] = uncapped_dictionary[entry].capitalize()


#reverse_dictionary = {translated_phrase:outline for outline,translated_phrase in briefed_dictionary.items()} 

#briefed_dictionary['-PG'] = str(len(briefed_dictionary))


def lookup(strokes):

    outline = "/".join(strokes)
    outline = aericks_denumberizer(outline)

    return briefed_dictionary[outline]

with open("autobriefed.json", "w") as outfile:
    json.dump(briefed_dictionary, outfile, indent=0)

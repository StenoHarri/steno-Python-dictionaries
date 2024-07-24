"""
Left hand = Activate Harri numbers
Right fingers = any two digit number
Right thumbs = stick up to three 0's on the end
"""

import re

LONGEST_KEY = 4 


starter_chord = {

   #Default numbers
   "#"       : {"prefix" : " ",
                "suffix" : " "},
   
   #KWR for sticking stuff, so no spacing
   "#KWR"    : {"prefix" : "{^",
              "suffix"   : "}"},

    #KL for clock stuff
    "#KHR"   : {"prefix" : "{^:",
                "suffix" : "}"},

    #TWO for years 2000's
    #TW for 20
    #O  for 00
    "#TWO"   : {"prefix" : "20",
                "suffix" : " "},


    #NO for years 1900's
    #N for 19
    #O for 00
    "#TPHO"   : {"prefix" : "19",
                "suffix" : " "},


    #Po for pound
    "#PO"    : {"prefix" : "£",
                "suffix" : ""},

    #DL for dollar
    "#TKHRA" : {"prefix" : "$",
                "suffix" : ""},

    #P for point or pennies
    "#P"     : {"prefix" : "{^.",
                "suffix" : " }"}
}

linker_chord = { #by linker, I mean collapsing a 100 with 23 to output 123 (two strokes)
    
}



primary_number = {
    ""    : "",
    "R"   : "1",
    "RB"  : "2",
    "B"   : "3",
    "FR"  : "4",
    "FRPB": "5",
    "PB"  : "6",
    "F"   : "7",
    "FP"  : "8",
    "P"   : "9",
    #everything else is zero
    "FB"  : "0",
    "RP"  : "0",
    "FRP" : "0",
    "FRB" : "0",
    "FPB" : "0",
    "RPB" : "0"
}
secondary_number = {
    ""    : "",
    "G"   : "1",
    "GS"  : "2",
    "S"   : "3",
    "LG"  : "4",
    "LGTS": "5",
    "TS"  : "6",
    "L"   : "7",
    "LT"  : "8",
    "T"   : "9",
    #everything else is zero
    "LS"  : "0",
    "GT"  : "0",
    "LGT" : "0",
    "LGS" : "0",
    "LTS" : "0",
    "GTS" : "0"
}
trailing_zeroes = {
    ""  : "",
    "E" : "0",
    "U" : "00",
    "EU": ",000"
}

def end_zeros(string):
    # How many zeroes at the end of a given string
    count = len(string) - len(string.rstrip("0"))
    return count



def lookup(strokes):

    assert len(strokes) <= LONGEST_KEY, '%d/%d' % (len(strokes), LONGEST_KEY)

    output_number= ''
    for stroke_number in range(len(strokes)):

        #make the raw steno use just letters
        if any(single_digit_number in "0123456789" for single_digit_number in strokes[stroke_number]):
            strokes=list(strokes)
            strokes[stroke_number]= "#" + strokes[stroke_number].replace(
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


        match = re.fullmatch(r'(#?\^?S?T?K?P?W?H?R?A?O?\*?)-?([EU]*)([FRPB]*)([LGTS]*)', strokes[stroke_number])
 
        #if it's not valid
        if not match:
            raise KeyError
        # If there's no numbers
        if not match[2]+match[3]+match[4]:
            raise KeyError


        if stroke_number==0:
            if not (starter_chord[match[1]]):
                raise KeyError
            prefix = starter_chord[match[1]]['prefix']
            suffix = starter_chord[match[1]]['suffix']

            output_number+=(primary_number[match[3]]+
                            secondary_number[match[4]]+
                            trailing_zeroes[match[2]])
        else:
            if not (linker_chord[match[1]]):
                raise KeyError
            successive_numbers=(primary_number[match[3]]+
                                secondary_number[match[4]]+
                                trailing_zeroes[match[2]])
            if len(successive_numbers) > end_zeros(output_number):
                raise KeyError
            output_number = (output_number[0:len(output_number)-len(successive_numbers)]+
                             successive_numbers)

    return (prefix+
            output_number +
            suffix)

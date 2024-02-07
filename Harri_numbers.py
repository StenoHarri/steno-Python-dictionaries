"""
Example of how to write:
29,312 takes 3 strokes

29,000      #EURBT
   300      #UB
    12      #RGS
======
29,312

the initial number is optional

,000        #EU
 100        #UR
  23        #RBS
====
,123
"""





import re


LONGEST_KEY = 4


starter_chord = {
    #In plover, {&} in the outline, means treat it like fingerspelling
    "#*"   : {"prefix"       : "{&",
              "suffix(one)"  : "}",
              "suffix(many)" : "}"},

    "#"    : {"prefix"       : " ",
              "suffix(one)"  : " ",
              "suffix(many)" : " "},

    "#KWR" : {"prefix"       : " ",
              "suffix(one)"  : " year ",
              "suffix(many)" : " years "},

    "#HRAO"  : {"prefix"     : " oh look, ",
              "suffix(one)"  : " mouse ",
              "suffix(many)" : " mice "}
}

linker_chord = { #by linker, I mean if it can get combined into the zeroes, it will
    "#"   : True,
    "KWR" : True,
    "#HRAO":True
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
            suffix_one = starter_chord[match[1]]['suffix(one)']
            suffix_many = starter_chord[match[1]]['suffix(many)']

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
    
    if output_number=='1':
        suffix=suffix_one
    else:
        suffix=suffix_many
    
    return (prefix+
            output_number +
            suffix)

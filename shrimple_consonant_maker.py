with open("Jalexu parts.json", "w") as outfile:
    outfile.write("you gotta copy paste this thing")



starter_letter={
    "" : "",

    "^":"a",
    "^SK":"ex",
    "^SKPH":"em",
    "^SKHR":"excl",
    "^SKR":"excr", #maybe?
    "^TPH":"on ", #maybe?
    "^SKWR":"eng", #maybe?

    "S" : "s",
    "STK": "dis",
    "STKPW": "z", #I've decided not disg
    "SKPH":"im",
    "SKP": "and ",
    "SKWR": "j",
    "SKHR": "shr",
    "SPW":"int",
    "SH" : "sh",
    "SR" : "v",
    #"S*" : "z",

    "T" : "t",
    "TK": "d",
    "TKPW":"g",
    "TKW":"dev",
    "TKR":"dr",
    "TP": "f",
    "TPH": "n",

    "K":"k",
    "KP":"x",
    "KPW":"imp",
    "KW":"q", #interesting, cause vowel?
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


def steno_fingers_into_letters(steno_consonant, left_or_right_dictionary):


    #if it's one/two splittable, do this:
    for split_location in range(len(steno_consonant)):

        #print("now on " + steno_consonant[:split_location] + " and " + steno_consonant[split_location:])

        if (steno_consonant[:split_location] in left_or_right_dictionary and
            steno_consonant[split_location:] in left_or_right_dictionary):
            
            #print ("\n"+steno_consonant[:split_location] + steno_consonant[split_location:])
            #print("found: "+ left_or_right_dictionary[steno_consonant[:split_location]]+left_or_right_dictionary[steno_consonant[split_location:]])
            return (left_or_right_dictionary[steno_consonant[:split_location]]+left_or_right_dictionary[steno_consonant[split_location:]])

    #else, you gotta split some more
    
    match=[]
    for split_location in range(1, len(steno_consonant)):
        #print("\tnow on " + steno_consonant[:split_location]
        #      + " and "
        #        + steno_consonant[split_location:])
        
        match.append (steno_fingers_into_letters(steno_consonant[:split_location], left_or_right_dictionary) + 
                 steno_fingers_into_letters(steno_consonant[split_location:], left_or_right_dictionary))
    
    no_dupes = list(dict.fromkeys(match))
    #I'm lazy, this is literally all the conflict resolution, as you can see, I just pick the first one generated:
    no_dupes = "("+'|'.join(match)+")"
    
    #I do not understand why they work different, but they do
    if left_or_right_dictionary==starter_letter:
        no_dupes= match[0]
    elif left_or_right_dictionary==ender_letter:
        no_dupes= match[-1]
        for dupe in match:
            if not "delete" in dupe:
                no_dupes=dupe
        for dupe in match:
            if not "delete" in dupe:
                if not "z" in dupe:
                    no_dupes=dupe
    

    return (str(no_dupes))

for shwa_key in ["^", ""]:
    for S_key in ["S", ""]:
        for T_key in ["T", ""]:
            for K_key in ["K", ""]:
                for P_key in ["P", ""]:
                    for W_key in ["W", ""]:
                        for H_key in ["H", ""]:
                            for R_key in ["R", ""]:
                                starter_steno = shwa_key+S_key+T_key+K_key+P_key+W_key+H_key+R_key
                                if not starter_steno == '':
                                    thing_to_add=("'"+starter_steno+"': '"+steno_fingers_into_letters(starter_steno, starter_letter)+"',")
                                    #print(thing_to_add)
                                    with open("Jalexu parts.json", "a") as outfile:
                                        outfile.write("\n"+thing_to_add)

with open("Jalexu parts.json", "a") as outfile:
    outfile.write("\n\n\n################################################################################\n\n")


ender_letter={
    "":"",
    "*":"[delete me]",
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
    "FRB":"mb", #come back to this
    "FRL":"ml",
    "FRBL":"mbl",
    "FP":"ch",
    "FPL":"tual",
    "FPLT":"{.}",
    "FB":"v",
    "FT":"st",

    "R":"r", #if o, then end in e
    "RPBLG":"rg",
    "RB":"sh", #unless AU to make it rb carb barb
    "RBL":"rrow",
    "RBT":"tial",
    "RBG":"rk",
    "RBGS":"{,}",
    "RBS":"tious",

    "P":"p",
    "PB":"n",
    "PBLG":"dg",
    "PBLGS":"jection",
    "PBG":"ng",
    "PBGS":"nction",
    "PL":"m",
    #PZ for h?

    "B":"b",
    "BLG":"ckle",
    "BG":"k",
    "BGT":"ct", 
    "BGTS":"cts",
    "BGS":"x", #I don't know about ction, maybe asterisk?

    "L":"l", #come back to this

    "G":"g",
    "GT":"xt",
    "GS":"tion", #fuck you

    "T":"t",
    "TS":"ts",
    "TZ":"se",

    "S":"s", #might be some logic here for c? Realtime uses `SZ` for c
    "SD":"e",
    
    "D":"d",
    

    "Z":"e"

}


for F_key in ["F", ""]:
    for R_key in ["R", ""]:
        for P_key in ["P", ""]:
            for B_key in ["B", ""]:
                for L_key in ["L", ""]:
                    for G_key in ["G", ""]:
                        for T_key in ["T", ""]:
                            for S_key in ["S", ""]:
                                for D_key in ["D", ""]:
                                    for Z_key in ["Z", ""]:

                                        ender_steno = F_key+R_key+P_key+B_key+L_key+G_key+T_key+S_key+D_key+Z_key
                                        if not ender_steno == '':
                                            a_thing_to_add = False 
                                            #ideally I'd like this to go backwards
                                            for asterisk_location in range(len(ender_steno),0,-1):
                                                asterisk_location-=1
                                                
                                                ender_steno_with_asterisk=ender_steno[:asterisk_location]+"*"+ender_steno[asterisk_location:]
                                                
                                                thing_to_add= ("'*"+ender_steno_with_asterisk.replace("*","")+"': '"+steno_fingers_into_letters(ender_steno_with_asterisk, ender_letter)+"',")
                                                #print(ender_steno_with_asterisk)
                                                if not "delete me" in thing_to_add:
                                                    a_thing_to_add = thing_to_add
                                            if a_thing_to_add:
                                                with open("Jalexu parts.json", "a") as outfile:
                                                    outfile.write("\n"+a_thing_to_add)
                                            thing_to_add= ("'"+ender_steno+"': '"+steno_fingers_into_letters(ender_steno, ender_letter)+"',")
                                            #print(thing_to_add)
                                            with open("Jalexu parts.json", "a") as outfile:
                                                outfile.write("\n"+thing_to_add)

print("check your files for Jalexu parts, so you can copy paste the contents into the shrimp python dictionary")

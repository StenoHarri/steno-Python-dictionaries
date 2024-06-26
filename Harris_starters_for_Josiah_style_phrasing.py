"""

"""

starters={
    '':'',
    '^STHAU'    :'as though',
    '^STHOE'    :'as though',
    '^STHOU'    :'as though',
    '^SPHAE'    :'as many',
    '^SPHOE'    :'as most',
    '^SPR'      :'as were',
    '^SPROU'    :'as proud',
    '^SPAOEU'   :'in spite',
    '^SWU'      :'as one',
    '^PHOU'     :'amount',
    '^HR'       :'a lot',
    '^HE'       :'ahead',
    '^AOE'      :'as each',
    'STKW'      :'does',
    'STPHE'     :'instead',
    'STPHAOE'   :'indeed',
    'STPHAOEU'  :'inside',
    'SKWR'      :'just',        #`SKWR*` → `{>}{&j}`
    'SPWOE'     :'is both',
    'SPWE'      :'is the best',
    'SPHAE'     :'is many',
    'SPHOE'     :'is most',
    'SPROU'     :'is proud',
    'SPAOEU'    :'spite',
    'SWU'       :'is one',
    #'SAOU'      :'is out',     #`SAOUT` → `suit` `SAO*UT` → `{^suit}`
    #'SOU'       :'is out',     #`SO*UT` → `south`
    'TKPWO'     :'got',
    'TKPWOU'    :'get out',
    'TKPHOE'    :'know',
    'TKPWU'     :'go out',
    'TKW'       :'do',
    'THOU'      :'thought',
    'THAU'      :'thought',     #`THA*UF` → `that you've`
    #'PWA'       :'because', #bath
    'PWAU'      :'because',
    'PWOE'      :'both',
    'PWE'       :'best',
    'PHAE'      :'many',
    'PHOE'      :'most',
    'PR'        :'were',
    'PROU'      :'proud',
    'WHR'       :'whether',
    'WHRAO'     :'whether or not',
    'WR'        :'where',
    'WOE'       :'worst',
    'WU'        :'one',
    'HRA'       :'last',
    'HRAOE'     :'least',
    'RE'        :'rest',
    'AOE'       :'each',
    'AOU'       :'out',
    'OU'        :'out',
}


enders={
    '*':'',
       '*F':' have',
    '*FRBG':' of your',
   '*FRBGS':' of yourself',
    '*FPBT':" haven't",
     '*FPL':' of my',
     '*FBL':' of those',
      '*FL':' of all',
      '*FT':' of the',
     '*FTS':' of it is',
      '*PL':' my',
       '*T':' the',
        'F':' of',
     'FRPG':' of these',
    'FPBTS':' of them',
      'FPL':' of me',
      'FBL':' those',
     'FBLS':' of their',
    'FLGTS':' of that',
    'FTSDZ':' of this',
       'FT':' of it',
      'FTS':' of its',      #`HRAFTS` → `lasts` or `last of its`
       'FS':' of us',
      'RPG':' these',
     'PBTS':' them',
       'PL':' me',
      #'BL':' believe',
      'BLS':' their',
     'LGTS':' that',
        'T':' it',
     'TSDZ':' this',
}



conflicts={
    "SKWR*"     : "{>}{&j}",        #just
    "TKPWO*UT"  : "gout",           #get out the
    "TKPWOUT"   : "got you",        #get out it
    "THA*UF"    : "that you've",    #thought have
    "PWOET"     : "boat",           #both it
    "PWET"      : "bet",            #best it
    "PHAEPL"    : "mayhem",         #many me
    "PHAET"     : "meat",           #many it
    "HRAOEPL"   : "lemme",          #least me
    "AO*U"      : "{out^}",         #out
    "AOEFT"     : "east",           #each of it
    "AOET"      : "eat",            #each it
    "*F"        : "{^'ve}"          #have
}





joined_dictionary={}




for starter in starters:
    for ender in enders:
        if not (starter == "" and ender == "*"):
            joined_dictionary[(starter+'-'+ender).replace("-*","*").replace("U-","U").replace("E-","E").replace("O-","O").replace("A-","A").replace("U*","*U").replace("E*","*E")] = starters[starter]+enders[ender]

joined_dictionary = joined_dictionary | conflicts

#print(joined_dictionary)

LONGEST_KEY = 1

def lookup(strokes):
    return joined_dictionary[strokes[0]]

"""
import json
with open("Harri_starters.json", "w") as outfile:
    json.dump(joined_dictionary, outfile, indent=0)
"""

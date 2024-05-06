"""

"""

starters={
    '':'',
    '^SPAOEU'   :'in spite',
    '^HR'       :'a lot',
    'STKW'      :'does',
    'STPHE'     :'instead',
    'STPHAOE'   :'indeed',
    'STPHAOEU'  :'inside',
    'SPAOEU'    :'spite',
    'TKPWO'     :'got',
    'TKPWOU'    :'get out',
    'TKW'       :'do',
    'THOU'      :'thought',
    'THAU'      :'thought',
    'PWAU'      :'because',
    'PWOE'      :'both',
    'PWE'       :'best',
    'PHAE'      :'many',
    'PHOE'      :'most',
    'PROU'      :'proud',
    'WOE'       :'worst',
    'WU'        :'one',
    'HRA'       :'last',
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
      'FPL':' of me',
      'FBL':' those',
     'FBLS':' of their',
    'FLGTS':' of that',
    'FTSDZ':' of this',
       'FT':' of it',
      'FTS':' of its',
       'FS':' of us',
      'RPG':' these',
       'PL':' me',
      #'BL':' believe',
      'BLS':' their',
     'LGTS':' that',
        'T':' it',
     'TSDZ':' this',
}


joined_dictionary={}

for starter in starters:
    for ender in enders:
        if not (starter == "" and ender == "*"):
            joined_dictionary[(starter+ender).replace("U*","*U").replace("E*","*E")] = starters[starter]+enders[ender]


print(joined_dictionary)

LONGEST_KEY = 1

def lookup(strokes):
    return joined_dictionary[strokes[0]]


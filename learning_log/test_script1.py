fav_lan={'jen':['python','ruby'],
         'sarah':['c'],
         'edward':['ruby','go'],
         'phil':['python','haskell']}

for name, lang in fav_lan.items():
    if len(lang)>1:
        print(f"\n{name.title()}'s favourite languages are:")
        for lan in lang:
            print(f"\t{lan.title()}")
    else:
        print(f"\n{name.title()}'s favourite language is:")
        for lan in lang:
            print(f"\t{lan.title()}")
import random

first = ["Chelm", "Elm", "El", "Bur", "En", "Eg", "Pem", "Pen", "Edg", "Sud", "Sod", "Hors", "Dur", "Sun", "Nort", "Brad", "Farn", "Barn", "Dart", "Hart", "South", "Shaft", "Blan", "Rock", "Alf", "Wy", "Marl", "Staf", "Wet", "Cas", "Stain", "Whit", "Stap", "Brom", "Wych", "Watch", "Win", "Horn", "Mel", "Cook", "Hurst", "Ald", "Shriv", "Kings", "Clere", "Maiden", "Leather", "Brack","Brain", "Walt", "Prest", "Wen", "Flit", "Ash"]
doubles = ["Bass", "Chipp", "Sodd", "Sudd", "Ell", "Burr", "Egg", "Emm", "Hamm", "Hann", "Cann", "Camm", "Camb", "Sund", "Pend", "End", "Warr", "Worr", "Hamp", "Roth", "Both", "Sir", "Cir", "Redd", "Wolv", "Mill", "Kett", "Ribb", "Dribb", "Fald", "Skell", "Chedd", "Chill", "Tipp", "Full", "Todd", "Abb", "Booth"]
postdoubles = ["ing", "en", "er"]
mid = ["bas", "ber", "stan", "ring", "den", "-under-", " on ", "en", "re", "rens", "comp", "mer", "sey", "mans"]
last = ["ford", "stoke", "ley", "ney",  "don", "den", "ton", "bury", "well", "beck", "ham", "borough", "side", "wick", "hampton", "wich", "cester", "chester", "ling", "moor", "wood", "brook", "port", "wold", "mere", "castle", "hall", "bridge", "combe", "smith", "field", "ditch", "wang", "over", "worth", "by", "brough", "low", "grove", "avon", "sted", "bourne", "borne", "thorne", "lake", "shot", "bage", "head", "ey", "nell", "tree", "down"]

def doname():
    finished_name = ""
    pd = 0
    if(random.random()  > 0.4):
        finished_name = finished_name + random.choice(doubles)
        if(random.random()  > 0.6):
            finished_name = finished_name + random.choice(postdoubles)
            pd = 1
        else:
            finished_name = finished_name[0:len(finished_name) - 1]
    else:
        finished_name = finished_name + random.choice(first)

    if(random.random()  > 0.5 and not pd):
        if(finished_name.endswith("r") or finished_name.endswith("b")):
            if(random.random()  > 0.4):
                finished_name = finished_name + "ble"
            else:
                finished_name = finished_name + "gle"
        elif(finished_name.endswith("n") or finished_name.endswith("d")):
            finished_name = finished_name + "dle"
        elif(finished_name.endswith("s")):
            finished_name = finished_name + "tle"

    if(random.random()  > 0.7 and finished_name.endswith("le")):
        finished_name = finished_name + "s"

    elif(random.random()  > 0.5):
        if(finished_name.endswith("n")):
            if(random.random()  > 0.5):
                finished_name = finished_name + "s"
            else:
                finished_name = finished_name + "d"
        elif(finished_name.endswith("m")):
            finished_name = finished_name + "s"

    if(random.random()  > 0.7):
        finished_name = finished_name + random.choice(mid)
    finished_name = finished_name + random.choice(last)

    fix = finished_name.rpartition(' ')
    if(fix[1] == ' '):
        finished_name = fix[0] + ' ' + fix[2].capitalize()

    fix = finished_name.rpartition('-')
    if(fix[1] == '-'):
        finished_name = fix[0] + '-' + fix[2].capitalize()

    return str(finished_name)

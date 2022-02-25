import os
import random

while True :
    entries = os.listdir('db/')

    print('Learn Katakana🗾')
    print('Chose a serie, press q for quit')
    print("Series >", *entries)
    r = input(os.getlogin() + ' : ')
    
    if(r == "q"):
        break
    else:
        # Read file
        try:
            f = open("db/" + r, encoding="UTF-8")
            content = f.read().split('\n')
        except:
            continue

        for i in range(10):
            try:
                jp, tr = random.choice(content).split(' ')
            except:
                continue
            usr = ""
            while True:
                usr = input(jp + " : ")
                if tr == usr:
                    break
                else:
                    print(jp + " > " + tr)
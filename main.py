#-*-coding:utf8;-*-
#qpy:3
#qpy:console


import androidhelper

droid = androidhelper.Android()

roda = True
while roda:
    msg = input ("\n'esc' sai, q + posso dizer? ") 
    if msg == "esc":
        roda = False
        break
    droid.ttsSpeak(msg)

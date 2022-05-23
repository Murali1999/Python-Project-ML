import tkinter as tk
from tkinter import Button

fa=open('unames.txt','a+')
fa.close()
fb=open('pwds.txt','a+')
fb.close()

def savecreds():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    if((a=='' and b=='') or (a=='' and c=='')):
        check=tk.Label(win3,text='YOU CANNOT LEAVE THE CREDENTIALS EMPTY!')
        check.place(x=20,y=150)
        
    if(len(a)<4):
        check=tk.Label(win3,text='USERNAME IS SHORT.',bg='red',fg='white')
        check.place(x=20,y=165)
    else:
        fa=open('unames.txt', 'a+')
        fa.write(a)
        fa.write("\n")
        show=tk.Label(win3,text='USERNAME IS VALID. SAVED!',bg='green',fg='black')
        show.place(x=20,y=165)
        
    if(b!=c):
        check=tk.Label(win3,text='PASSWORDS DO NOT MATCH.',bg='red',fg='white')
        check.place(x=20,y=195)
    else:
        fb=open('pwds.txt', 'a+')
        fb.write(b)
        fb.write("\n")
        show=tk.Label(win3,text='PASSWORD IS VALID. SAVED!',bg='green',fg='black')
        show.place(x=20,y=195)
        
    fb.flush()
    fa.flush()
    fb.close()
    fa.close()

    '''fa=open('unames.txt','r')
    un=fa.read().splitlines()
    fa.close()
    fb=open('pwds.txt','w')

    if((a not in un) and (len(a)<4)):
        stop=tk.Label(win3,text='USERNAME IS SHORT, BUT UNIQUE. TRY AGAIN.',bg='green',fg='black')
        stop.place(x=20,y=225)
        fa=open('unames.txt','w')
        fb.write('')
        fa.write('')
    else:
        stop=tk.Label(win3,text='USERNAME IS NOT UNIQUE. TRY AGAIN.',bg='green',fg='black')
        stop.place(x=20,y=225)
        fa=open('unames.txt','w')
        fb.write('')
        fa.write('')

    fb.flush()
    fa.flush()
    fb.close()
    fa.close()'''

def quitnow():
    exit()

win3=tk.Tk()
win3.title('SIGN-UP PAGE')
win3.geometry('300x300')
title1=tk.Label(win3,text='WELCOME TO THE SIGN-UP PAGE')
title1.place(x=30,y=1)
lab1=tk.Label(win3,text='Enter Username:')
lab1.place(x=2,y=35)
lab2=tk.Label(win3,text='Enter Password:')
lab2.place(x=2,y=65)
lab3=tk.Label(win3,text='Enter Again:')
lab3.place(x=2,y=95)
button1=Button(win3,text='Submit',command=savecreds)
button1.place(x=10,y=125)
ent1=tk.Entry(win3)
ent1.place(x=95,y=35)
ent2=tk.Entry(win3,show='*')
ent2.place(x=95,y=65)
ent3=tk.Entry(win3,show='*')
ent3.place(x=95,y=95)
exit1=tk.Button(win3,text='Exit',command=quitnow)
exit1.place(x=70,y=125)

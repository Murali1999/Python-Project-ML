import tkinter as tk
from tkinter import Button
import smtplib

win=tk.Tk()
win.title('LOGIN PAGE')
win.geometry('300x300')
title1=tk.Label(win,text='WELCOME TO THE LOGIN PAGE')
title1.place(x=30,y=1)
lab1=tk.Label(win,text='Enter Username:')
lab1.place(x=2,y=30)
lab2=tk.Label(win,text='Enter Password:')
lab2.place(x=2,y=65)
global fr,pw,to,c

def send():
    fr=ea.get()
    to=eb.get()
    pw=ec.get()
    c=ed.get()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.ehlo()
        server.starttls()
        server.login(fr,pw)
        server.sendmail(fr,to,c)
        print('Email sent!')
    except:  
        print('Something went wrong... Please try again.')
    finally:
        server.quit()

def emailwindow():
    new=tk.Tk()
    global ea,eb,ec,ed
    new.geometry('700x400')
    new.title('EMAIL APPLICATION')
    h=tk.Label(new,text='REMOTE EMAIL SENDING APPLICATION')
    h.grid(row=1,column=3)
    info=tk.Label(new,text='CREDENTIALS ARE CORRECT. WELCOME!')
    info.grid(row=3,column=2)
    exit1=Button(new,text='LogOut',command=quitnow)
    exit1.grid(row=9,column=3)
    l1=tk.Label(new,text='FROM:')
    l1.grid(row=5,column=2)
    ea=tk.Entry(new)
    ea.grid(row=5,column=3)
    l2=tk.Label(new,text='PASSWORD:')
    l2.grid(row=6,column=2)
    eb=tk.Entry(new,show='*')
    eb.grid(row=6,column=3)
    l3=tk.Label(new,text='TO:')
    l3.grid(row=7,column=2)
    ec=tk.Entry(new)
    ec.grid(row=7,column=3)
    l4=tk.Label(new,text='CONTENT:')
    l4.grid(row=8,column=2)
    ed=tk.Entry(new)
    ed.grid(row=8,column=3)
    s=tk.Button(new,text='Submit',command=send)
    s.grid(row=9,column=2)
            
def checkcreds():
    u=entry1.get()
    p=entry2.get()
    fa=open('unames.txt','r')
    un=fa.read().splitlines()
    fb=open('pwds.txt','r')
    pw=fb.read().splitlines()

    if(u in un):
        if(p in pw and un.index(u)==pw.index(p)):
            emailwindow()
        elif(p not in pw):
            win2=tk.Tk()
            win2.geometry('400x100')
            info=tk.Label(win2,text='PASSWORD IS WRONG')
            info.place(x=20,y=40)
            exit1=tk.Button(win2,text='Exit',command=quitnow)
            exit1.place(x=20,y=70)
    else:
        win2=tk.Tk()
        win2.geometry('400x100')
        info=tk.Label(win2,text='CREDENTIALS ARE WRONG')
        info.place(x=20,y=40)
        exit1=tk.Button(win2,text='Exit',command=quitnow)
        exit1.place(x=20,y=70)

    fb.close()
    fa.close()
    
def change():
    import signup_project
    
button1=Button(win,text='Submit',command=checkcreds)
button1.place(x=10,y=100)
button2=Button(win,text='SignUp',command=change)
button2.place(x=115,y=100)
entry1=tk.Entry(win)
entry1.place(x=95,y=30)
entry2=tk.Entry(win,show='*')
entry2.place(x=95,y=65)

def quitnow():
    exit()

exit1=Button(win,text='Quit',command=quitnow)
exit1.place(x=70,y=100)

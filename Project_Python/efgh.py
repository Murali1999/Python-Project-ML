import tkinter as tk
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
entry1=tk.Entry(win)
entry1.place(x=95,y=30)
entry2=tk.Entry(win,show='*')
entry2.place(x=95,y=65)

win2=tk.Tk()
win2.title('EMAIL APPLICATION')
win2.geometry('300x300')
    
def check():
    u=entry1.get()
    p=entry2.get()
    
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.login(u,p)
        a1=tk.Label(win2,text='NOW YOU CAN SEND EMAILS USER!')
        a1.place(x=10,y=2)
        To=tk.Label(win2,text='TO:')
        To.place(x=1,y=30)
        To1=tk.Entry(win2)
        To1.place(x=30,y=30)
        From=tk.Label(win2,text='FROM:')
        From.place(x=1,y=60)
        From1=tk.Label(win2,text=u)
        From1.place(x=40,y=60)
        Text=tk.Label(win2,text='CONTENT:')
        Text.place(x=1,y=90)
        Text1=tk.Entry(win2)
        Text1.place(x=70,y=90)
        s.quit()
    except:
        a1=tk.Label(win2,text='SORRY! SOMETHING WENT WRONG.')
        a1.place(x=1,y=2)

def send():
    e1=To1.get()
    e2=Text1.get()
    u=entry1.get()
    p=entry2.get()
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.ehlo()
        server.starttls()
        server.login(u,p)
        server.sendmail(u,To1,Text1)
        print('Email sent!')
        server.quit()
    except:  
        print('Something went wrong... Please try again.')

but=tk.Button(win2,text='Submit',command=send)
but.place(x=100,y=120)
button1=tk.Button(win,text='Submit',command=check)
button1.place(x=10,y=100)

def quitnow():
    exit()

exit1=tk.Button(win,text='Quit',command=quitnow)
exit1.place(x=70,y=100)

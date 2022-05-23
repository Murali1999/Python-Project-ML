import sklearn
import mlxtend
import tkinter as tk

items={'Milk':25,'Bread':30,'Butter':60,'Cheese':50,
       'Lays':20,'Kurkure':20,'Bhujia':40,'Pringles':90,
       'Salsa':120,'Maiyonnaise':120,'Tomato sauce':90,'Hot n Sweet sauce':100,
       'Pepsi':45,'Thumbs up':45,'Nimbooz':30,'Roohafza':70}
nums=[1,2,3,4,5,6,7,8,9,10]

win=tk.Tk()
win.title('DEPARTMENTAL STORE')
win.geometry('400x200')
title1=tk.Label(win,text='WELCOME TO OUR DEPARTMENTAL STORE')
title1.grid(row=1,column=3)
l1=tk.Label(win,text='Choose item:')
l1.grid(row=3,column=2)
num1=tk.IntVar()
num1.set(nums[0])
w1=tk.OptionMenu(win,num1,*nums)
w1.grid(row=5,column=3)
num2=tk.StringVar()
num2.set(list(items.keys())[0])
w2=tk.OptionMenu(win,num2,*items)
w2.grid(row=5,column=2)
button=tk.Button(win,text='Submit',command=done)
button.grid(row=7,column=3)

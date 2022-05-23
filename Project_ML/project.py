import sklearn
import csv
import pandas as pd
import mlxtend
import tkinter as tk
from mlxtend.frequent_patterns import apriori  #for recommendations
from mlxtend.preprocessing import TransactionEncoder

#list of items present in the departmental store
items={'Milk':25,'Bread':30,'Butter':60,'Cheese':50,
       'Lays':20,'Kurkure':20,'Bhujia':40,'Pringles':90,
       'Salsa':120,'Maiyonnaise':120,'Tomato sauce':90,'Hot n Sweet sauce':100,
       'Pepsi':45,'Thumbs up':45,'Nimbooz':30,'Roohafza':70}
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
win=tk.Tk()
win.title('DEPARTMENTAL STORE')
win.geometry('480x200')

win1=tk.Tk()
win1.geometry('350x200')
win1.title('YOUR BILL')

title1=tk.Label(win,text='WELCOME TO OUR DEPARTMENTAL STORE')
title1.grid(row=1,column=2)
bill=tk.Label(win1,text='YOUR BILL')
bill.grid(row=1,column=2)
N=tk.Label(win1,text='NAME')
No=tk.Label(win1,text='NO.')
P=tk.Label(win1,text='PRICE')
N.grid(row=2,column=1,sticky='WE')
No.grid(row=2,column=2,sticky='WE')
P.grid(row=2,column=3,sticky='WE')

r,c=3,1
summ,i,j=[],0,0
lists=[] #global and local variable at the same time; can be accessed inside and outside the function

win2=tk.Tk()
win2.title('RECOMMENDATIONS LIST') #show all the recommendations
win2.geometry('250x250')

def done():
    global r,c,summ,i,j
    e1=num1.get()
    e2=num2.get()
    lists.append(e2) #add items to the list everytime button is clicked
    n=int(e1)
    p=int(items[e2])
    price=n*p
    summ.append(price)
    total=sum(summ)
    pro=tk.Label(win1,text=e2,bg='White',fg='Black')
    nos=tk.Label(win1,text=n,bg='White',fg='Black')
    pri=tk.Label(win1,text=price,bg='White',fg='Black')
    tot=tk.Label(win1,text=total,bg='White',fg='Black')
    amt=tk.Label(win1,text='TOTAL =',bg='White',fg='Black')
    pro.grid(row=r,column=c,sticky='WE')
    nos.grid(row=r,column=c+1,sticky='WE')
    pri.grid(row=r,column=c+2,sticky='WE')
    tot.grid(row=r+1,column=c+2,sticky='WE')
    amt.grid(row=r+1,column=c,sticky='WE',columnspan=2)
    r=r+1
    print(lists)

l1=tk.Label(win,text='Choose item:')
l1.grid(row=3,column=1)
num1=tk.IntVar()
num1.set(nums[0])
w1=tk.OptionMenu(win,num1,*nums)
w1.config(width=5)
w1.grid(row=5,column=2)
num2=tk.StringVar()
num2.set(list(items.keys())[0])
w2=tk.OptionMenu(win,num2,*items)
w2.config(width=10)
w2.grid(row=5,column=1)
button=tk.Button(win,text='Submit',command=done)
button.grid(row=7,column=2)
row,col=0,0
lines=[]

def generate():
    with open('itemlists.csv','a',newline='') as myfile:
        wr = csv.writer(myfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        wr.writerow(lists)
    print('Added to the .csv file!')

gen=tk.Button(win1,text='Generate',command=generate)
gen.grid(row=3,column=6)

def quitnow():
    exit()
    
def showlists():
    dataset=[]
    dataset = pd.read_csv('itemlists.csv',header=None).fillna(" ")
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary,columns=te.columns_)
    listbox=tk.Listbox(win2)
    '''
    with open('.csv','r') as myfile:
        rd = csv.reader(myfile,delimiter=',')
        reclist=list(rd)
        listbox.insert(reclist)
    listbox.grid(row=2,column=2)
    '''
        
exit1=tk.Button(win,text='Exit',command=quitnow)
exit1.grid(row=7,column=1)
show=tk.Button(win,text='Show Recommendations',command=showlists)
show.grid(row=7, column=3)
ex=tk.Button(win1,text='Exit',command=quitnow)
ex.grid(row=4,column=6)

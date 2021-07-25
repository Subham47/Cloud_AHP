# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:04:20 2021

@author: hp
"""

import csv
import pandas as pd 
import numpy as np
import random
import getpass
from tkinter import *
import tkinter
from PIL import Image, ImageTk

#from google.colab import drive
#drive.mount('/content/gdrive')# force_remount=True)

df = pd.read_csv('./cloud.csv')
df1 = pd.read_csv('./initial.csv')
print()
#print("Original data::")
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df.head(12))

def platform():
    root = Tk()
    root.attributes("-fullscreen", True)
    #cb=0
    def login():
        global flag
        print("Enter login credentials to continue::")
        print("Enter username:")
        name=input()
        print("Enter password:")
        password=getpass.getpass()
        
        if name=='Subham1' and password=='gb29':
            print('login successful!')
            flag=1
        else:
            print('Wrong username or password') 
            flag=0
    def quit_(*args):
        root.destroy()
        
    def my_upd1():
        global cb
        cb = 1
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd2():
        global cb
        cb = 2
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd3():
        global cb
        cb = 3
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd4():
        global cb
        cb = 4
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd5():
        global cb
        cb = 5
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd6():
        global cb
        cb = 6
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd7():
        global cb
        cb = 7
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd8():
        global cb
        cb = 8
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
    def my_upd9():
        global cb
        cb = 9
        if flag==1:
            print('Service Agreement Analysis:')
            print('Provider:',df1.columns[cb])
            print('Cost for service:',df1.loc[0][cb])
            print('Validity:',df1.loc[1][cb],'month')
            print('Services:')
            for i in range(2,5):
                if df1.loc[i][cb]==1:
                    print(df1.loc[i][0])
                
    image = Image.open("google.png")
    photo = ImageTk.PhotoImage(image)
    #l = Label(root, text='Google')
    #l.pack()
    #l.bind('<Button-1>', login) 
    b = Button(root, image=photo, command=lambda:[quit_(),login(),my_upd1()])
    b.pack()
    b.place(x=0, y=0)
    #b = Button(root, text="Close", command=root.destroy)
    #b.pack()
    
    image1 = Image.open("amazon.png")
    photo1 = ImageTk.PhotoImage(image1)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo1, command=lambda:[quit_(),login(),my_upd2()])
    b.pack()
    b.place(x=600, y=0)
    #b = Button(root, text="Close", command=root.destroy)
    #b.pack()
   
    image2 = Image.open("microsoft.png")
    photo2 = ImageTk.PhotoImage(image2)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo2, command=lambda:[quit_(),login(),my_upd3()])
    b.pack()
    b.place(x=1100, y=0)
    
    
    image3 = Image.open("alibaba.png")
    photo3 = ImageTk.PhotoImage(image3)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo3, command=lambda:[quit_(),login(),my_upd4()])
    b.pack()
    b.place(x=0, y=200)
    
 
    image4 = Image.open("salesforce.png")
    photo4 = ImageTk.PhotoImage(image4)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo4, command=lambda:[quit_(),login(),my_upd5()])
    b.pack()
    b.place(x=600, y=200)
    
 
    image5 = Image.open("dell.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo5, command=lambda:[quit_(),login(),my_upd6()])
    b.pack()
    b.place(x=1025, y=200)
    
   
    image6 = Image.open("ibm.png")
    photo6 = ImageTk.PhotoImage(image6)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo6, command=lambda:[quit_(),login(),my_upd7()])
    b.pack()
    b.place(x=0, y=500)
    
  
    image7 = Image.open("digital_ocean.png")
    photo7 = ImageTk.PhotoImage(image7)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo7, command=lambda:[quit_(),login(),my_upd8()])
    b.pack()
    b.place(x=600, y=500)
    
 
    image8 = Image.open("oracle.png")
    photo8 = ImageTk.PhotoImage(image8)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo8, command=lambda:[quit_(),login(),my_upd9()])
    b.pack()
    b.place(x=1100, y=500)
    
    '''image9 = Image.open("dropbox.png")
    photo9 = ImageTk.PhotoImage(image9)
    #l = Label(root, text='Amazon')
    #l.pack()
    #l.bind('<Button-2>', login) 
    b = Button(root, image=photo9, command=lambda:[quit_(),login()])
    b.pack()
    b.place(x=300, y=200)'''
    
    root.mainloop()
    #print(cb)
    return flag, cb

def demander():
    top = Tk()
    top.attributes("-fullscreen", True)
    def quit_(*args):
        top.destroy()
    global CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7, CheckVar8, CheckVar9, CheckVar10, CheckVar11, CheckVar12  
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10 = IntVar()
    CheckVar11 = IntVar()
    CheckVar12 = IntVar()
    C1 = Checkbutton(top, text = "1.Cost_benefit", variable = CheckVar1, \
                     onvalue = 1, offvalue = 0, height=1, \
                     width = 20)
    C2 = Checkbutton(top, text = "2.Efficiency", variable = CheckVar2, \
                     onvalue = 2, offvalue = 0, height=1, \
                     width = 20)
    C3 = Checkbutton(top, text = "3.Ease_of_use", variable = CheckVar3, \
                     onvalue = 3, offvalue = 0, height=1, \
                     width = 20)
    C4 = Checkbutton(top, text = "4.Customization", variable = CheckVar4, \
                     onvalue = 4, offvalue = 0, height=1, \
                     width = 20)
    C5 = Checkbutton(top, text = "5.Commitment", variable = CheckVar5, \
                     onvalue = 5, offvalue = 0, height=1, \
                     width = 20)
    C6 = Checkbutton(top, text = "6.Tech_infra", variable = CheckVar6, \
                     onvalue = 6, offvalue = 0, height=1, \
                     width = 20)
    C7 = Checkbutton(top, text = "7.Relative_pos", variable = CheckVar7, \
                     onvalue = 7, offvalue = 0, height=1, \
                     width = 20)
    C8 = Checkbutton(top, text = "8.Law_policy", variable = CheckVar8, \
                     onvalue = 8, offvalue = 0, height=1, \
                     width = 20)
    C9 = Checkbutton(top, text = "9.Availability", variable = CheckVar9, \
                     onvalue = 9, offvalue = 0, height=1, \
                     width = 20)
    C10 = Checkbutton(top, text = "10.Support", variable = CheckVar10, \
                     onvalue = 10, offvalue = 0, height=1, \
                     width = 20)
    '''C11 = Checkbutton(top, text = "Priority_Rating_Client", variable = CheckVar11, \
                     onvalue = 1, offvalue = 0, height=1, \
                     width = 20)
    C12 = Checkbutton(top, text = "Priority_Rating_Provider", variable = CheckVar12, \
                     onvalue = 1, offvalue = 0, height=1, \
                     width = 20)'''
    exit_button = Button(top, text="Finish & exit", command=quit_)
    C1.pack(pady=10)
    C1.place(x=100, y=100)
    C2.pack(pady=10)
    C2.place(x=400, y=100)
    C3.pack(pady=10)
    C3.place(x=700, y=100)
    C4.pack(pady=10)
    C4.place(x=100, y=200)
    C5.pack(pady=10)
    C5.place(x=400, y=200)
    C6.pack(pady=10)
    C6.place(x=700, y=200)
    C7.pack(pady=10)
    C7.place(x=100, y=300)
    C8.pack(pady=10)
    C8.place(x=400, y=300)
    C9.pack(pady=10)
    C9.place(x=700, y=300)
    C10.pack(pady=10)
    C10.place(x=100, y=400)
    '''C11.pack(pady=10)
    C11.place(x=400, y=400)
    C12.pack(pady=10)
    C12.place(x=700, y=400)'''
    
    exit_button.pack(pady=10)
    exit_button.place(x=400, y=600)
    top.mainloop()
    
    #print(CheckVar1.get(),CheckVar2.get())
    
def provider():
    result=[]
    j=1
    a=0
    for i in range(9):
        score = 0
        if CheckVar1.get()==1:
            if a==0:
                print('Selected Cost benefit:Factor Beneficial')
            score += df.loc[CheckVar1.get()-1][j]*(20*7)
        if CheckVar2.get()==2:
            if a==0:
                print('Selected Efficiency::Factor Beneficial')
            score += df.loc[CheckVar2.get()-1][j]*(19*7)
        if CheckVar3.get()==3:
            if a==0:
                print('Selected Ease of use:Factor Beneficial')
            score += df.loc[CheckVar3.get()-1][j]*(13*3)
        if CheckVar4.get()==4:
            if a==0:
                print('Selected Customization:Factor Beneficial')
            score += df.loc[CheckVar4.get()-1][j]*(15*3)
        if CheckVar5.get()==5:
            if a==0:
                print('Selected Commitment:Factor Risky')
            score += df.loc[CheckVar5.get()-1][j]*(3*1)
        if CheckVar6.get()==6:
            if a==0:
                print('Selected Technological infrastructure:Factor Beneficial')
            score += df.loc[CheckVar6.get()-1][j]*(5*4)
        if CheckVar7.get()==7:
            if a==0:
                print('Selected Relative position in market:Factor Risky')
            score += df.loc[CheckVar7.get()-1][j]*(1*2)
        if CheckVar8.get()==8:
            if a==0:
                print('Selected Law policy:Factor Risky')
            score += df.loc[CheckVar8.get()-1][j]*(4*5)
        if CheckVar9.get()==9:
            if a==0:
                print('Selected Availability:Factor Beneficial')
            score += df.loc[CheckVar9.get()-1][j]*(7*6)
        if CheckVar10.get()==10:
            if a==0:
                print('Selected Support:Factor Beneficial')
            score += df.loc[CheckVar10.get()-1][j]*(14*6)
        a+=1
        result.append(score)
        j+=1
    #print(result)
    '''if CheckVar11.get()=='1':
        score = df.loc[0]['Google']*(20*7)
    if CheckVar12.get()=='1':
        score = df.loc[0]['Google']*(20*7)'''
    print('Analysis:')

    def rankify(result):
        R = [0 for x in range(len(result))]
        for i in range(len(result)):
            (r, s) = (1, 1)
            for j in range(len(result)):
                if j != i and result[j] > result[i]:
                    r += 1
                if j != i and result[j] == result[i]:
                    s += 1      
            
            # Use formula to obtain rank
            R[i] = r + (s - 1) / 2
     
        # Return Rank Vector
        return R
    ranking=rankify(result)
    for i in range(len(result)):
        print('||',int(ranking[i]),df.columns[i+1],result[i],'||') 
    #print(result.index(max(result)))
    mx=max(result[0],result[1])
    secondmax=min(result[0],result[1])
    n =len(result)
    for i in range(2,n):
        if result[i]>mx:
            secondmax=mx
            mx=result[i]
        elif result[i]>secondmax and \
            mx != result[i]:
            secondmax=result[i]
    #print(mx,secondmax)
    #print(df.loc[-1][result.index(mx)])
    #print(df.columns)
    print('Best CSP is::',df.columns[result.index(mx)+1])
    print('Second best CSP is::',df.columns[result.index(secondmax)+1]) 
    return result, df.columns[result.index(mx)+1], df.columns[result.index(secondmax)+1]

if __name__=='__main__':
    flag, cb=platform()
    #print(flag)
    #print(cb)
    list=[1,2,3,4,5,6,7,8,9]
    
    if flag == 1:
        print('Do you want to see recommendations::')
        print('[y/n]')
        ans = input()
        if ans == 'y':
            demander()
            result, mx, secondmax=provider()
            #print(mx,secondmax)
            if df.columns[cb]==mx or df.columns[cb]==secondmax:
                print('Best service selected:',df.columns[cb])
            else:
                print('ALternatives with weights:')
                list.remove(cb)
                for i in list:
                    print('||',df.columns[i],result[i-1],"||")
        elif ans == 'n':
            if cb==1:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==2:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==3:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==4:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==5:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==6:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==7:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==8:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            if cb==9:
                print('Continuing with',df.columns[cb],'...')
                list.remove(cb)
            #if cb==10:
            #    print('Continuing with',df.columns[cb])
            print('Alternative subnodes/services:')
            for i in list:
                print(df.columns[i])
        else:
            print('Invalid input')
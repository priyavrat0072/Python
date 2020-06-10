from Tkinter import *
from tkMessageBox import *

import sqlite3
con=sqlite3.Connection('mypizza')
cur=con.cursor()
cur.execute("create table if not exists mypizza(cust_name varchar2(20) not null,cust_id varchar2(10) primary key,total number,margherita number,farmhouse number,Peppypanner number,mexicangreen number,Deluxeveggie number,Chesecorn number,vegparadise number,Freshveggie number,onioncreem number,oniontomato number,pepperbarbecue number,barbecuechicken number, chickentikka number,chickensausage number,chickendelight number,nonvegsupreme number,chickendominator number,periperichicken number,chickenfiesta number,chickenonion number)")

root=Tk()
#root.resizable(width=False,height=False)
root.geometry("750x470")
img=PhotoImage(file='bit.gif')
Label(root,image=img).place(x=0,y=0)
Label(root,text='MY PIZZA',font='algerian 20 bold',fg='black',bg='orange',bd=5).grid(row=0,column=0,columnspan=6)
Label(root,text='Enter customer name:',font='eras 10',fg='blue',bg='yellow').grid(row=1,column=0,pady=7)
e1=Entry(root,font='eras 10',fg='blue',bg='pink',width=18)
e1.grid(row=1,column=1,pady=7)
Label(root,text='Enter customer id:',font='eras 10',fg='blue',bg='yellow').grid(row=1,column=2,pady=7,padx=10)
e2=Entry(root,font='eras 10',fg='blue',bg='pink',width=10)
e2.grid(row=1,column=3,pady=7)
Label(root,text='VEG PIZZA',font='broadway 10',fg='brown',bg='pink',bd=5).grid(row=2,column=0,columnspan=2,pady=3)
Label(root,text='Margherita:',justify='left',fg='Black',bg='light blue').grid(row=3,column=0,sticky='w')
d1=Entry(root,bg='dark grey')
d1.grid(row=3,column=1)
Label(root,text='Farm House:',justify='left',fg='Black',bg='light blue').grid(row=4,column=0,sticky='w')
d2=Entry(root,bg='dark grey')
d2.grid(row=4,column=1)
Label(root,text='Peppy Paneer:',justify='left',fg='Black',bg='light blue').grid(row=5,column=0,sticky='w')
d3=Entry(root,bg='dark grey')
d3.grid(row=5,column=1)
Label(root,text='Mexican Green:',justify='left',fg='Black',bg='light blue').grid(row=6,column=0,sticky='w')
d4=Entry(root,bg='dark grey')
d4.grid(row=6,column=1)
Label(root,text='Deluxe Veggie:',justify='left',fg='Black',bg='light blue').grid(row=7,column=0,pady=3,sticky='w')
d5=Entry(root,bg='dark grey')
d5.grid(row=7,column=1)
Label(root,text='Cheese corn:',justify='left',fg='Black',bg='light blue').grid(row=8,column=0,pady=3,sticky='w')
d6=Entry(root,bg='dark grey')
d6.grid(row=8,column=1)
Label(root,text='Veggie Paradise:',justify='left',fg='Black',bg='light blue').grid(row=9,column=0,pady=3,sticky='w')
d7=Entry(root,bg='dark grey')
d7.grid(row=9,column=1)
Label(root,text='Fresh Veggie:',justify='left',fg='Black',bg='light blue').grid(row=10,column=0,pady=3,sticky='w')
d8=Entry(root,bg='dark grey')
d8.grid(row=10,column=1)
Label(root,text='Onion Cream:',justify='left',fg='Black',bg='light blue').grid(row=11,column=0,pady=3,sticky='w')
d9=Entry(root,bg='dark grey')
d9.grid(row=11,column=1)
Label(root,text='Onion Tomato:',justify='left',fg='black',bg='light blue').grid(row=12,column=0,pady=3,sticky='w')
d10=Entry(root,bg='dark grey')
d10.grid(row=12,column=1)

Label(root,text='NON VEG PIZZA',font='broadway 10',fg='brown',bg='pink',bd=5).grid(row=2,column=2,columnspan=2,pady=7)
Label(root,text='Pepper Barbecue:',fg='Black',bg='light blue').grid(row=3,column=2,padx=3,sticky='w')
f1=Entry(root,bg='dark grey')
f1.grid(row=3,column=3)
Label(root,text='Barbecue Chicken:',fg='Black',bg='light blue').grid(row=4,column=2,padx=3,sticky='w')
f2=Entry(root,bg='dark grey')
f2.grid(row=4,column=3)
Label(root,text='Chicken Tikka:',fg='Black',bg='light blue').grid(row=5,column=2,padx=3,sticky='w')
f3=Entry(root,bg='dark grey')
f3.grid(row=5,column=3)
Label(root,text='Chicken Sausage:',fg='Black',bg='light blue').grid(row=6,column=2,padx=3,sticky='w')
f4=Entry(root,bg='dark grey')
f4.grid(row=6,column=3)
Label(root,text='Chicken Delight:',fg='Black',bg='light blue').grid(row=7,column=2,padx=3,sticky='w')
f5=Entry(root,bg='dark grey')
f5.grid(row=7,column=3)
Label(root,text='Non-veg supreme:',fg='Black',bg='light blue').grid(row=8,column=2,padx=3,sticky='w')
f6=Entry(root,bg='dark grey')
f6.grid(row=8,column=3)
Label(root,text='Chicken Dominator:',fg='Black',bg='light blue').grid(row=9,column=2,padx=3,sticky='w')
f7=Entry(root,bg='dark grey')
f7.grid(row=9,column=3)
Label(root,text='Peri Peri Chicken:',fg='Black',bg='light blue').grid(row=10,column=2,padx=3,sticky='w')
f8=Entry(root,bg='dark grey')
f8.grid(row=10,column=3)
Label(root,text='Chicken Fiesta:',fg='Black',bg='light blue').grid(row=11,column=2,padx=3,sticky='w')
f9=Entry(root,bg='dark grey')
f9.grid(row=11,column=3)
Label(root,text='Onion Chicken :',fg='Black',bg='light blue').grid(row=12,column=2,padx=3,sticky='w')
f10=Entry(root,bg='dark grey')
f10.grid(row=12,column=3)

v1=IntVar()
Label(root,text='DRINKS',font='broadway 10',fg='brown',bg='pink',bd=5).grid(row=2,column=4)
Radiobutton(root,text='Coca-cola',variable=v1,value=1,justify='left',font='impact 10',fg='blue',bg='light blue' ).grid(row=3,column=4,padx=7,pady=3,sticky='w')
Radiobutton(root,text='Thumps-up',variable=v1,value=2,justify='left',font='impact 10',fg='blue',bg='light blue').grid(row=4,column=4,padx=7,pady=3,sticky='w')
Radiobutton(root,text='Mountain-dew',variable=v1,value=3,justify='left',font='impact 10',fg='blue',bg='light blue').grid(row=5,column=4,padx=7,pady=3,sticky='w')
Radiobutton(root,text='Sprite',variable=v1,value=4,justify='left',font='impact 10',fg='blue',bg='light blue').grid(row=6,column=4,padx=7,pady=3,sticky='w')

Label(root,text='Total',font='broadway 10',fg='brown',bg='pink',bd=5).grid(row=2,column=5)
t1=Entry(root,bg='orange',width=14)
t1.grid(row=3,column=5)

def fun1():
    t1.delete(0,END)
    if len(e1.get())==0:
        showerror('Error','Enter your name')
        return
    if len(e2.get())==0:
        showerror('Error','Enter your Id')
        return
    s=0
    if len(d1.get())!=0:
        s=s+60*int(d1.get())
    if len(d2.get())!=0:
        s=s+65*int(d2.get())
    if len(d3.get())!=0:
        s=s+70*int(d3.get())
    if len(d4.get())!=0:
        s=s+80*int(d4.get())
    if len(d5.get())!=0:
        s=s+85*int(d5.get())
    if len(d6.get())!=0:
        s=s+90*int(d6.get())
    if len(d7.get())!=0:
        s=s+95*int(d7.get())
    if len(d8.get())!=0:
        s=s+100*int(d8.get())
    if len(d9.get())!=0:
        s=s+105*int(d9.get())
    if len(d10.get())!=0:
        s=s+110*int(d10.get())
    if len(f1.get())!=0:
        s=s+115*int(f1.get())
    if len(f2.get())!=0:
        s=s+120*int(f2.get())
    if len(f3.get())!=0:
        s=s+125*int(f3.get())
    if len(f4.get())!=0:
        s=s+130*int(f4.get())
    if len(f5.get())!=0:
        s=s+135*int(f5.get())
    if len(f6.get())!=0:
        s=s+140*int(f6.get())
    if len(f7.get())!=0:
        s=s+145*int(f7.get())
    if len(f8.get())!=0:
        s=s+150*int(f8.get())
    if len(f9.get())!=0:
        s=s+155*int(f9.get())
    if len(f10.get())!=0:
        s=s+160*int(f10.get())
    t1.insert(16,s)

def fun2():
    a=askyesno('Confirm','Are you sure')
    if a==True:
        try:
            cur.execute("insert into mypizza values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),t1.get(),d1.get(),d2.get(),d3.get(),d4.get(),d5.get(),d6.get(),d7.get(),d8.get(),d9.get(),d10.get(),f1.get(),f2.get(),f3.get(),f4.get(),f5.get(),f6.get(),f7.get(),f8.get(),f9.get(),f10.get()))
            con.commit()
        except:
            t1.delete(0,END)
            showerror('Error','Id already exists')
        return
    t1.delete(0,END)

def fun3():
    cur.execute("select * from mypizza where cust_id==(?)",(id1.get(),))
    a=cur.fetchall()
    k=[]
    for i in a:
        for j in i:
            k.append(j)
    e1.insert(20,k[0])
    e2.insert(20,k[1])
    t1.insert(20,k[2])
    d1.insert(20,k[3])
    d2.insert(20,k[4])
    d3.insert(20,k[5])
    d4.insert(20,k[6])
    d5.insert(20,k[7])
    d6.insert(20,k[8])
    d7.insert(20,k[9])
    d8.insert(20,k[10])
    d9.insert(20,k[11])
    d10.insert(20,k[12])
    f1.insert(20,k[13])
    f2.insert(20,k[14])
    f3.insert(20,k[15])
    f4.insert(20,k[16])
    f5.insert(20,k[17])
    f6.insert(20,k[18])
    f7.insert(20,k[19])
    f8.insert(20,k[20])
    f9.insert(20,k[21])
    f10.insert(20,k[22])
    
            

def fun4():
    e1.delete(0,END)
    e2.delete(0,END)
    d1.delete(0,END)
    d2.delete(0,END)
    d3.delete(0,END)
    d4.delete(0,END)
    d5.delete(0,END)
    d6.delete(0,END)
    d7.delete(0,END)
    d8.delete(0,END)
    d9.delete(0,END)
    d10.delete(0,END)
    f1.delete(0,END)
    f2.delete(0,END)
    f3.delete(0,END)
    f4.delete(0,END)
    f5.delete(0,END)
    f6.delete(0,END)
    f7.delete(0,END)
    f8.delete(0,END)
    f9.delete(0,END)
    f10.delete(0,END)
    t1.delete(0,END)
    
Button(root,text='Submit',command=fun2,font='algerian 10',fg='black',bg='yellow').grid(row=4,column=5)
Button(root,text='ADD',command=fun1,font='algerian 10',fg='black',bg='yellow').grid(row=13,column=0,pady=3,columnspan=2)
Button(root,text='Reset',command=fun4,font='algerian 10',fg='black',bg='yellow').grid(row=13,column=2,pady=3,columnspan=2)
Label(root,text='Enter id to fetch record:',font='eras 10',fg='blue',bg='yellow').grid(row=14,column=0)
id1=Entry(root,font='eras 10',fg='blue',bg='pink')
id1.grid(row=14,column=1)
Button(root,text='Show',command=fun3,font='algerian 10',fg='black',bg='yellow').grid(row=14,column=2)
root.mainloop()

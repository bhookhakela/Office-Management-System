#importing libraries

import tkinter as tk
from tkinter.constants import END
import mysql.connector
from tkinter.font import Font
from tkinter import *
from datetime import * 
import time

#Connection to SQL Server:

con=mysql.connector.connect(host='localhost', password='123',user='root',database='office')

#Cursor Name is cur

cur=con.cursor()                                                 

#Declarations:
l3 = 0
l=0
entry=[]
log = []
emp=[]
wkl=[]
qwe=[]


Date = date.today()
Date = str(Date)
Time = datetime.now()
hour = int(Time.hour)

#Making the new window

gui = tk.Tk()
gui.geometry("626x417")
gui.title("Office Management System")

#insert the icon image

gui.iconbitmap(r'C:\Users\Lenovo\Desktop\New folder\logo.ico')
fnt = Font(family = "Lucida Sans Unicode", size = 15) 
 
#frame creation for content

frame = LabelFrame(gui,padx=5,pady=5)
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
frame = LabelFrame(canvas,padx=5,pady=5,bg='#e5f7fb')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
bg=PhotoImage(file=r"C:\Users\Lenovo\Desktop\New folder\bg.png")

#canvas creation to contain frame

canvas=tk.Canvas(gui,width=626,height=417)
canvas.place(x = 0, y = 0, anchor = NW)
canvas.create_image(0,0,image=bg,anchor=NW)

#functions

def tablecreation():
    cur.execute('create table if not exists info(ec int  primary key auto_increment, name varchar(45), address varchar(200), blood_grp varchar(8),ph_no varchar(10), dob date, dept varchar(15), designation varchar(15), password varchar(30), work varchar(200), wkhr int default 0) ;')
    cur.execute('ALTER TABLE info AUTO_INCREMENT=2')
    cur.execute("insert into info values(1, 'Admin', 'nil','nil',1234567890, '2000-10-10', 'ADMIN', 'BOD', 'admin','Assign Designations',0)")
    con.commit()


def logexe():
    global x
    x=ecno.get()
    log.append(x)
    
    cur.execute("select password from info where ec=%s",log)
    z=cur.fetchall()
    print(pwd.get())
    if z==[]:
            
        tk.Label(gui,text='User does not exist!',font=fnt,bg='#e5f7fb').grid(column='0',row='8',sticky='w')
        tk.Label(gui,text='Please contact your higher up.',font=fnt,bg='#e5f7fb').grid(column='0',row='9',sticky='w')
        log.clear()
            
        
    else:     
        for i in z:
            for j in i:
                p=j
        if pwd.get()!=p:
            global l3
            global l
            l+=1

            if l==1:
                l3=tk.Label(gui,text='Incorrect Password',font=fnt,bg='#e5f7fb')
                l3.grid(column='1',row='3')
                log.clear()
                pwd.delete(0,END)
            else:
                log.clear()
                pwd.delete(0,END)
            
        elif pwd.get()==p:
            
            log.append(pwd.get())
            
            cur.execute('select name from info where ec=%s and password= %s',(log[0],log[1]))
            data=cur.fetchall()
            
            for i in data:
                   for j in i:
                         n=j
            l1.destroy()
            l2.destroy()
            ecno.destroy()
            pwd.destroy()
            bt1.destroy()
            if l>=1:
                
                l3.destroy()
                tk.Label(frame,text='Welcome '+n,font=fnt,bg='#e5f7fb').grid(column='0',row='0',sticky='w')
                postlogin()
                
            else:   
                tk.Label(frame,text='Welcome '+n,font=fnt,bg='#e5f7fb').grid(column='0',row='0',sticky='w')
                postlogin()
                
                
def postlogin():

    if dgn()!='EMPLOYEE':
        tk.Label(frame,text='To Register A New Employee ',font=fnt,bg='#e5f7fb').grid(column='0',row='6',sticky='w')
        tk.Label(frame,text='',font=fnt,bg='#e5f7fb').grid(column='0',row='4',sticky='w')
        tk.Button(frame,text='Click Here',command=register,font=fnt).grid(column='1',row='6',sticky='w')
    else:
        pass
    
    starttime = time.time()
    Tim = datetime.now().strftime("%H:%M:%S")


    tk.Label(frame, text = "Date: " + Date,font=fnt,bg='#e5f7fb').grid(column = 0, row = 1,sticky='w')
    tk.Label(frame, text = "Time: " + Tim,font=fnt,bg='#e5f7fb').grid(column = 0, row = 2,sticky='w')

    if hour<=11 and hour>7:
        tk.Label(frame, text = "You are on Time",font=fnt,bg='#e5f7fb').grid(column = 0, row = 3,sticky='w')

    else:
        tk.Label(frame, text = "You are Late",font=fnt,bg='#e5f7fb').grid(column = 0, row = 3,sticky='w')
    cur.execute('select work from info where ec=%s',log)
    
    for i in cur.fetchall():
        for j in i:
            wrk=j

    print(wrk)        
    if wrk==None:
        tk.Label(frame, text="No Work Alotted",font=fnt,bg='#e5f7fb').grid(column = 0,row = 10)
    else:
        tk.Label(frame,text='',font=fnt,bg='#e5f7fb').grid(column='0',row='8',sticky='w')
        tk.Label(frame, text="Work Alotted: "+wrk,font=fnt,bg='#e5f7fb').grid(column = 0,row = 9,sticky='w')
        #tk.Label(frame, text=wrk,font=fnt,bg='#e5f7fb').grid(column =1,row = 9,sticky='w')
    
    def logout():
        endtime=time.time()
        elapsed = 'Workseconds:', round (endtime-starttime, 2)
        for i in elapsed:
            z = i
        wk = int(z)#//60//60
        wkl.clear()
        wkl.append(wk)
        qwe.append(x)
        
        cur.execute("select wkhr from info where ec=%s",qwe)
        z = cur.fetchall()
        for i in z:
                for j in i:
                        n=j
        print(n)
        
        wkl.append(n)
        twh = int(wkl[0])+int(wkl[1])
        print('twh',twh)
                    
        tk.Label(frame, text = "Work hour: "+ str(wk),bg='#e5f7fb').grid(column = 0, row = 3)

        upd =[]

        upd.append(twh)
        upd.append(x)
        print("Update",upd)

        cur.execute("update info set wkhr=%s where ec= %s",(upd[0],upd[1]))
        con.commit()
        frame.destroy()

    lo = tk.Button(frame,text='Logout',command= logout,font=fnt).grid(column='1',row='14',sticky='SE')
    tk.Label(frame,text='',font=fnt,bg='#e5f7fb').grid(column='0',row='4',sticky='w')
    wk = tk.Button(frame,text='Add Work',command= work,font=fnt).grid(column='0',row='14',sticky='w')

            
tk.StringVar
                    
def login():
    global ecno,pwd,l1,l2,bt1

    #labels
    l1=tk.Label(frame,text='EC',font=fnt,bg='#e5f7fb')
    l1.grid(column='0',row='0', sticky='w')
    l2=tk.Label(frame,text='Password ',font=fnt,bg='#e5f7fb')
    l2.grid(column='0',row='1', sticky='w')

    #entries
    ecno=tk.Entry(frame,width=15)
    ecno.grid(column='1',row='0')
    pwd=tk.Entry(frame,width=15,show='*')
    pwd.grid(column='1',row='1')
    bt1=tk.Button(frame,text='Login',command=logexe,font=fnt)
    bt1.grid(column='1',row='15')
    
def register():
    if dgn()!='EMPLOYEE':

        #creation of new window for registration
        
        global gui1
        gui1=tk.Toplevel()
        gui1.resizable(False, False)
        gui1.configure(bg='#e5f7fb')
        gui1.title("REGISTRATION")          

        #global declaration
        
        global a,b,c,d,e,f,g,h,clicked

        #stores the chosen entry from optionmenu
        
        clicked = tk.StringVar()        
        
        #Labels
        tk.Label(gui1,text='Name',bg='#e5f7fb').grid(column='8',row='0')
        tk.Label(gui1,text='Address',bg='#e5f7fb').grid(column='8',row='1')
        tk.Label(gui1,text='Blood Group',bg='#e5f7fb').grid(column='8',row='2')
        tk.Label(gui1,text='Phone Number',bg='#e5f7fb').grid(column='8',row='3')
        tk.Label(gui1,text='Date of Birth',bg='#e5f7fb').grid(column='8',row='4')
        tk.Label(gui1,text='Department',bg='#e5f7fb').grid(column='8',row='5')
        tk.Label(gui1,text='Designation',bg='#e5f7fb').grid(column='8',row='6')
        tk.Label(gui1,text='password',bg='#e5f7fb').grid(column='8',row='7')

        #Entries
        a=tk.Entry(gui1,width=15)
        a.grid(column='9',row='0')
        b=tk.Entry(gui1,width=15)
        b.grid(column='9',row='1')
        c=tk.Entry(gui1,width=15)
        c.grid(column='9',row='2')
        d=tk.Entry(gui1,width=15)
        d.grid(column='9',row='3')
        e=tk.Entry(gui1,width=15)
        e.grid(column='9',row='4')
        f=tk.Entry(gui1,width=15)
        f.grid(column='9',row='5')
        h=tk.Entry(gui1,width=15,show='*')
        h.grid(column='9',row='7')
        
        clicked.set( "EMPLOYEE" )
        if dgn()=='BOD':
            g = tk.OptionMenu( gui1 ,clicked,'CEO','DIRECTOR','MANAGER','EMPLOYEE')
            g.grid(column='9',row='6')
        elif dgn()=='CEO':
            g = tk.OptionMenu( gui1 ,clicked,'DIRECTOR','MANAGER','EMPLOYEE')
            g.grid(column='9',row='6')
        elif dgn()=='DIRECTOR':
            g = tk.OptionMenu( gui1 ,clicked,'MANAGER','EMPLOYEE')
            g.grid(column='9',row='6')
        elif dgn()=='MANAGER':
            g = tk.OptionMenu( gui1 ,clicked,'EMPLOYEE')
            g.grid(column='9',row='6')

        bt=tk.Button(gui1,text='Submit',command=submit).grid(column='0',row='8')

#inserts the new employee data        

def submit():
    cur.execute("INSERT INTO info(name,address,blood_grp,ph_no,dob,dept,designation,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),clicked.get(),h.get()))
    gui1.destroy()
    con.commit()

#fetches the designation of given ec
    
def dgn():
    log.clear()
    log.append(x)
    
    cur.execute('select designation from info where ec=%s',log)
    des=cur.fetchall()
    for i in des:
        for j in i:
            return j

#assigning work to juniors only*
        
def work():
    
    #global assignment
    
    global gui2,k,h,i,g,m,clicked1,l

    #creation of new window for work assignment

    gui2=tk.Toplevel()
    gui2.configure(bg='#e5f7fb')
    gui2.resizable(False, False)

    
    clicked1 = tk.StringVar()
    clicked1.set("EMPLOYEE")
    if dgn()=='BOD':
        g = tk.OptionMenu( gui2 ,clicked1,'CEO','DIRECTOR','MANAGER','EMPLOYEE')
        g.grid(column='2',row='0')
    elif dgn()=='CEO':
        g = tk.OptionMenu( gui2 ,clicked1,'DIRECTOR','MANAGER','EMPLOYEE')
        g.grid(column='2',row='0')
    elif dgn()=='DIRECTOR':
        g = tk.OptionMenu( gui2 ,clicked1,'MANAGER','EMPLOYEE')
        g.grid(column='2',row='0')
    elif dgn()=='MANAGER':
        g = tk.OptionMenu( gui2 ,clicked1,'EMPLOYEE',font=fnt)
        g.grid(column='2',row='0')
           

    l = tk.Label(gui2,text='EC',font=fnt,bg='#e5f7fb')
    l.grid(column='0',row='16')
    m = tk.Entry(gui2,width=15)
    m.grid(column='1',row='16')
    k = tk.Label(gui2,text='Work',font=fnt,bg='#e5f7fb')
    k.grid(column='0',row='15')
    h = tk.Entry(gui2,width='15')
    h.grid(column='1',row='15')
    i = tk.Button(gui2,text='Send',command=destwork,font=fnt)
    i.grid(column='0',row='17')

#updating the appointed working the database

def destwork():
    if upwork() == True:
        cur.execute("update info set Work=%s where ec= %s",(wku[1],m.get()))
        
        gui2.destroy()
        con.commit()

    else:
        l.destroy()

#checks if the given ec matches the claimed designation
        
def upwork():
    global wku
    k=''
    wrkec=[]
    wku=[]
    wku.append(clicked1.get())
    wku.append(h.get())
    wrkec.append(m.get())
    
    cur.execute("select designation from info where ec= %s",wrkec)
    tbldes=cur.fetchall()
    for i in tbldes:
        for j in i:
            k=j

    if k==clicked1.get():
        return True
             
    else:
        tk.Label(gui2,text='Designation and EC does not Match',font=fnt,bg='#e5f7fb').grid(column='0',row='18')
        print('Wrong Designation',font=fnt)
        return False

#main code
    
tablecreation()

login()

gui.mainloop()

con.commit()

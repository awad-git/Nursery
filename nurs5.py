from tkinter import *
from datetime import *
from PIL  import  ImageTk,Image
from  tkinter import  ttk
from   tkinter import  messagebox
from tkinter.filedialog import asksaveasfile
import sqlite3
import csv
w=Tk()
w.title('جمعية عرب الحسون الخيرية')
w.geometry('500x400')
img=Image.open(r'C:\bel.jpg')
img2=ImageTk.PhotoImage(img)
l0=Label(w,image=img2)
l0.place(width=500,height=400)
#im=ImageTk.PhotoImage(Image.open(r'D:\Courses\Programming\Pyt\ground.png').resize((500,400)))
w.configure()
w.resizable(False,False)
global now
now=date.today()
print(now)

#Interface buttons (الحضانة)

def button1():
    f=Frame(w)
    f.place(width=500,height=400)
    f.configure(bg='blue')
    f2 = Frame(f,bg='blue')
    f2.grid(row=0, column=6)
    #bf2 = Button(f2, text='frame2').grid(row=1, column=8, padx=50)
    f1 = Frame(f,bg='blue')
    f1.grid(row=0, column=0)
    #bf1 = Button(f1, text='المعلمات',bg='green',command=miss).grid(row=1, column=1, padx=20,ipadx=50,ipady=50)
    f3 = Frame(f,bg='blue')
    f3.grid(row=0, column=22)
    #bf3 = Button(f3, text='التلاميذ',bg='green',command=child).grid(row=1, column=13, padx=20,ipadx=50,ipady=50)
    f4 = Frame(f,bg='blue')
    f4.grid(row=15, column=7)

    def home():
        f.destroy()


    hom = Button(f4, text='home',bg='red',command=home).grid(row=20, column=5, padx=10, pady=50,ipadx=20,ipady=20)
def miss():
        f= Frame(w)
        f.place(width=500, height=400)
        f.configure(bg='turquoise')
        f2 = Frame(f,bg='turquoise')
        f2.grid(row=0, column=6)
        f1 = Frame(f,bg='turquoise')
        f1.grid(row=0, column=0)

        f4 = Frame(f,bg='turquoise')
        f4.grid(row=15, column=7)

        def home():
            f.destroy()

        hom = Button(f4, text='home', command=home).grid(row=15, column=5, padx=10, pady=50)

        bf1 = Button(f1, text='المعلمات', command=miss).grid(row=1, column=3, padx=20,columnspan=3)
        bf2 = Button(f1, text='اضافة', command=miss).grid(row=5, column=1, padx=20,pady=10,ipadx=10,ipady=10)
        bf3 = Button(f1, text='تعديل', command=miss).grid(row=6, column=1, padx=20,pady=10,ipadx=10,ipady=10)
        bf4 = Button(f1, text='حذف', command=miss).grid(row=7, column=1, padx=20,pady=10,ipadx=10,ipady=10)
        bf5 = Button(f1, text='طباعة', command=miss).grid(row=8, column=1, padx=20,pady=5,ipadx=10,ipady=5)
        bf6 = Button(f1, text='بحث', command=miss).grid(row=9, column=1, padx=20, pady=10,ipadx=5,ipady=5)


        lf1 = Label(f2, text='الاسم', fg='red').grid(row=2, column=7)
        comb1=ttk.Combobox(f2).grid(row=2, column=8, padx=10, pady=10)
        lf2 = Label(f2, text='السن', fg='red').grid(row=3, column=7)
        e2 = Entry(f2)
        e2.grid(row=3, column=8, padx=10, pady=10)
        lf3 = Label(f2, text='عدد الطلبة', fg='red').grid(row=4, column=7)
        e3 = Entry(f2)
        e3.grid(row=4, column=8, padx=10, pady=10)
        lf4 = Label(f2, text='رقم الهاتف', fg='red').grid(row=5, column=7)
        e4 = Entry(f2)
        e4.grid(row=5, column=8, padx=10, pady=10)
#chilldren buttons functions
#save new children




def checkchild():
    #bd2= datetime.datetime.strptime(bd, '%Y-%m-%d')
    #age=datetime.datetime.strptime(now,'%Y-%m-%d') - strftime('%Y', bd2)
    lcs=Label(tc,text=' ').grid(row=7,column=9,padx=5,pady=5,ipadx=5)


def addc():
    global tc
    tc=Toplevel(w,bg='springgreen',width=350,height=400)
    ndate= Label(tc, text=now, fg='black').grid(row=1, column=6)
    global en0
    global en0, en1,en2,en3,en4
    global nc0
    global nc1
    global nc2
    global nc3
    global nc4
    nc0=StringVar()
    nc1=IntVar()
    nc2=StringVar()
    nc3=IntVar()
    nc4=IntVar()
    ln0 = Label(tc, text='الاسم', fg='red').grid(row=2, column=7)
    en0 = Entry(tc,textvariable=nc0)
    en0.grid(row=2, column=8, padx=10, pady=10)
    ln1 = Label(tc, text='تاريخ الميلاد', fg='red').grid(row=3, column=7)
    en1 = Entry(tc,textvariable=nc1)
    en1.grid(row=3, column=8, padx=10, pady=10)
    ln2 = Label(tc, text='المعلمة', fg='red').grid(row=4, column=7)
    en2 = Entry(tc,textvariable=nc2)
    en2.grid(row=4, column=8, padx=10, pady=10)
    ln3 = Label(tc, text='السن', fg='red').grid(row=5, column=7)
    en3 = Entry(tc,textvariable=nc3)
    en3.grid(row=5, column=8, padx=10, pady=10)
    ln4 = Label(tc, text='رقم الهاتف', fg='red').grid(row=6, column=7)
    en4 = Entry(tc,textvariable=nc4)
    en4.grid(row=6, column=8, padx=10, pady=10)
    #bnsearch=Button(tc,text='فحص',bg='yellow').grid(row=7,column=7,padx=5,pady=5,ipadx=5)
    global childata
    #childata=[en0.get(),en1.get(),en2.get(),en3.get(),en4.get()]
    nc0=str(en0.get())
    nc1 = str(en1.get())
    nc2 = str(en2.get())
    nc3 = str(en3.get())
    nc4 = str(en4.get())
    childata=[nc0,nc1,nc2,nc3,nc4]
    print (type(childata[0]))


    bnsave=Button(tc,text='حفظ',bg='green',command=chilsave).grid(row=7,column=8,padx=5,pady=5,ipadx=5)
    #lcheckn = Label(tc, text='مقبول', fg='black').grid(row=8, column=8, padx=5, pady=5, ipadx=5)

def error():
        messagebox.showerror('خطأ', 'البيانات غير مكتملة')
#\\\\new save location
def chilsave ():
    nc0 = en0.get()
    nc1 = en1.get()
    nc2 = en2.get()
    nc3 = en3.get()
    nc4 = en4.get()
    if en0.get() and en2.get() and en2.get() and en3.get() and en4.get():
        childata = [nc0, nc1, nc2, nc3, nc4]
        conn=sqlite3.connect('nursery.db')
        c=conn.cursor()
        #c.execute('DROP TABLE children ')
        #c.execute('DROP TABLE balance ')
        #c.execute("CREATE TABLE children (name text,birth integer,teacher text,age integer ,phone integer)")
        c.execute("INSERT INTO children  VALUES (?,?,?,?,?)",childata)
        conn.commit()
        conn.close()
        en0.delete(0,END)
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        en4.delete(0,END)
    #tc.destroy()
    else:
        error()

def combochild():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM children")
    print(c.fetchall())
    c.execute("SELECT name FROM children ")
    data=[]
    for row in c.fetchall():
        data.append(row[0])
    return data
    print(data)

    conn.commit()
    conn.close()

def child():
    global  comb1
    global esc2,esc3,esc4,esc5
    f= Frame(w)
    f.place(width=500, height=400)
    f.configure(bg='springgreen')
    f2 = Frame(f,bg='springgreen')
    f2.grid(row=0, column=6)
    f1 = Frame(f,bg='springgreen')
    f1.grid(row=0, column=0)

    f4 = Frame(f,bg='springgreen')
    f4.grid(row=15, column=7)

    def home():
        f.destroy()

    hom = Button(f4, text='home', command=home).grid(row=15, column=5, padx=10, pady=50)

    bf1 = Button(f1, text='التلاميذ', command=miss).grid(row=1, column=3, padx=20, columnspan=3)
    bf2 = Button(f1, text='اضافة', command=addc).grid(row=5, column=1, padx=20, pady=10,ipadx=10,ipady=10)
    bf3 = Button(f1, text='تعديل', command=eitchild).grid(row=6, column=1, padx=20, pady=10,ipadx=10,ipady=10)
    bf4 = Button(f1, text='حذف', command=chidel).grid(row=7, column=1, padx=20, pady=10,ipadx=10,ipady=10)
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM children")
    result = c.fetchall()
    bf5 = Button(f1, text='طباعة', command=lambda :exceld(result)).grid(row=8, column=1, padx=20, pady=5,ipadx=10,ipady=5)
    bf6 = Button(f1, text='بحث', command=searchild).grid(row=9, column=1, padx=20, pady=5,ipadx=10,ipady=5)

    lf1 = Label(f2, text='الاسم', fg='red').grid(row=2, column=7)
    comb1=ttk.Combobox(f2)
    comb1.grid(row=2, column=8, padx=10, pady=10)
    comb1['values'] =combochild()
    #comb1.bind('<<ComboboxSelected>>', combochild)
    #e1 = Entry(f2)
    #e1.grid(row=2, column=8, padx=10, pady=10)
    lf2 = Label(f2, text='السن', fg='red').grid(row=3, column=7)
    esc2 = Entry(f2)
    esc2.grid(row=3, column=8, padx=10, pady=10)
    lf3 = Label(f2, text='المعلمة', fg='red').grid(row=4, column=7)
    esc3 = Entry(f2)
    esc3.grid(row=4, column=8, padx=10, pady=10)
    lf4 = Label(f2, text='تاريخ الميلاد', fg='red').grid(row=5, column=7)
    esc4 = Entry(f2)
    esc4.grid(row=5, column=8, padx=10, pady=10)
    lf4 = Label(f2, text='رقم الهاتف', fg='red').grid(row=6, column=7)
    esc5 = Entry(f2)
    esc5.grid(row=6, column=8, padx=10, pady=10)
#search child
def searchild():
    esc2.delete(0,END)
    esc3.delete(0, END)
    esc4.delete(0, END)
    esc5.delete(0, END)
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    a=comb1.get()
    print (a)
    c.execute("SELECT * FROM children WHERE name=?",(a,))
    kidsearch =c.fetchall()
    print(c.fetchall())
    #en0.insert(END,kidsearch[0])
    esc2.insert(END,kidsearch[0][3])
    esc3.insert(END,kidsearch[0][2])
    esc4.insert(END,kidsearch[0][1])
    esc5.insert(END,kidsearch[0][4])
def exceld(result):
    #with open('child.csv','a') as f :
       # w=csv.writer(f,dialect='excel')
       # for record in result:
            #w.writerow(record)
    #with open('child.csv','r') as f:
       # m= csv.reader(f,dialect='excel',delimiter=',')
        #for i in result :
             #   print(i)
    with open(r'C:\التلاميذ.csv','a') as f:
            w = csv.writer(f, dialect='excel')
            for record in result:
                w.writerow(record)

def chidel():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    a = comb1.get()
    c.execute("DELETE FROM children WHERE name=?", (a,))
    conn.commit()
    conn.close()
    comb1.delete(0, END)
    esc2.delete(0, END)
    esc3.delete(0, END)
    esc4.delete(0, END)
    esc5.delete(0, END)

def eitchild ():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    a = comb1.get()
    editedc1 = esc2.get()
    editedc2 = esc3.get()
    editedc3 = esc4.get()
    editedc4 = esc5.get()
    c.execute("UPDATE children SET birth=?,teacher=?,age =? ,phone =? WHERE name=?", (editedc3,editedc2,editedc1,editedc4,a))
    #editedchild=[editedc1,editedc2,editedc3,editedc4]
    conn.commit()
    conn.close()
    comb1.delete(0, END)
    esc2.delete(0, END)
    esc3.delete(0, END)
    esc4.delete(0, END)
    esc5.delete(0, END)
#التقوية
def button2():
    f = Frame(w)
    f.place(width=500, height=400)
    # f.config(bg='blue')
    l1 = Label(f, text='الاسم').grid(row=0, column=0)
    l2 = Label(f, text='السن').grid(row=1, column=0)
    ae = Entry(f)
    ae.grid(row=0, column=1)
    be = Entry(f)
    be.grid(row=1, column=1)
    btn1 = Button(f, text='save').grid(row=5, column=3, columnspan=3)

    def home():
        f.destroy()

    hom = Button(f, text='home', command=home).grid(row=6, column=5, padx=3, pady=3)

#التحفيظ
def button3():
    f = Frame(w)
    f.place(width=500, height=400)
    # f.config(bg='blue')
    l1 = Label(f, text='الاسم').grid(row=0, column=0)
    l2 = Label(f, text='السن').grid(row=1, column=0)
    ae = Entry(f)
    ae.grid(row=0, column=1)
    be = Entry(f)
    be.grid(row=1, column=1)
    btn1 = Button(f, text='save').grid(row=5, column=3, columnspan=3)

    def home():
        f.destroy()

    hom = Button(f, text='home', command=home).grid(row=6, column=5, padx=3, pady=3)
#الحسابات
def button4():
    f = Frame(w)
    f.place(width=500, height=400)
    f.config(bg='green')
    global bnot, dateb, empe, ob, ine, labelb ,eb
    bbtn = Button(f, text='الميزانية',command=budg).grid(row=0, column=7,padx=5,pady=5)
    #labelb = Label(f, text=total, bg='green').grid(row=0, column=6, padx=5, pady=5)
    eb = Entry(f)
    eb.grid(row=0, column=6)
    wared=IntVar()
    inl = Label(f, text='وارد').grid(row=1, column=7, padx=5, pady=5)
    ine = Entry(f,textvariable=wared)
    ine.grid(row=1, column=6)
    wared.set(0)
    monsaref=IntVar()
    monsaref.set(0)
    ol = Label(f, text='منصرف').grid(row=2, column=7, padx=5, pady=5)
    ob = Entry(f,textvariable=monsaref)
    ob.grid(row=2, column=6)
    empl = Label(f, text='مسؤول').grid(row=3, column=7, padx=5, pady=5)
    empe = Entry(f)
    empe.grid(row=3, column=6)
    dateb = Label(f, text='التاريخ').grid(row=4, column=7, padx=5, pady=5)
    dateb = Entry(f)
    dateb.grid(row=4, column=6)
    nl = Label(f, text='ملاحظات').grid(row=5, column=7, padx=5, pady=5)
    bnot = Entry(f)
    bnot.grid(row=5, column=6)


    bsave = Button(f, text='حفظ',command=savbal).grid(row=6, column=7, padx=5, pady=5,ipady=10)

    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM balance")
    budgres = c.fetchall()

    bprin=Button(f, text='تقرير',command=lambda: prinbal(budgres)).grid(row=6, column=6, padx=5, pady=5)

    def home():
        f.destroy()

    hom= Button(f, text='home',command=home).grid(row=6, column=5, padx=10, pady=10)

#ACCOUNTING FUNCTIONS

def savbal():
    if ine.get() and ob.get() and empe.get() and dateb.get() and bnot.get():
    #in1=ine.get()- ob1=ob.get()- empe1=empe.get()- dateb1=dateb.get()-  bnot1=bnot.get()
        balist = [ine.get(), ob.get(), empe.get(), dateb.get(), bnot.get()]
        conn = sqlite3.connect('nursery.db')
        c = conn.cursor()
        #c.execute("CREATE TABLE balance (income integer,output integer,empl text ,date integer,note text)")
        c.execute("INSERT INTO balance  VALUES (?,?,?,?,?)", balist)
        conn.commit()
        conn.close()
        ine.delete(0,END)
        ob.delete(0, END)
        empe.delete(0, END)
        dateb.delete(0, END)
        bnot.delete(0, END)
    else:
        error()
def budg():
    global income_sum
    global out_sum
    eb.delete(0,END)
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("INSERT INTO balance  VALUES (?,?,?,?,?)", (0,0,0,0,0));conn.commit()
    c.execute("SELECT SUM(income) FROM balance" )
    insum=c.fetchall()
    print(insum[0])
    global income_sum
    income_sum=insum[0][0]
    c.execute("SELECT SUM(output) FROM balance")
    outsum = c.fetchall()
    global out_sum
    out_sum = outsum[0][0]
    global total
    total=int(income_sum)-int(out_sum)
    print(total)
    eb.insert(0,total)
    c.execute("DELETE FROM  balance WHERE date=? ",(0,));conn.commit()
    '''
    income_sum=0
    for i in range(len(insum)):
        income_sum=income_sum+insum[i][0]

    c.execute("SELECT SUM(output) FROM balance")
    outsum=c.fetchall()
    global out_sum
    out_sum=0
    for i in range(len(outsum)):
        out_sum=out_sum+outsum[i][0]
    print(out_sum)
    print(outsum)
    print(outsum[0][0])
    print(outsum[1][0])
    print(outsum[2][0])
    global total
    total=income_sum-out_sum
    print(total)
    eb.insert(0,total)
    '''
def prinbal(budgres):
    #import socket
    #be = str(socket.gethostname())
    #path1 = r'C:\Users' + "\\"+ be + "\\" + 'Desktop' + "\\" +
    #with open(r'C:\Users\{be}\Desktop\الحسابات.csv'), 'a') as f:
    #from os.path import join
    #import os
    #print(os.environ['USERPROFILE'])
    #ww = os.environ[r'USERPROFILE'] + "\\" + 'Deskto'+ "\\" +'accountant.csv'
    import shutil
    orig=r'C:\الحسابات.csv'
    dest=r'ww'
    with open(r'C:\الحسابات.csv','a') as f:

        w = csv.writer(f, dialect='excel')
        for record in budgres:
            w.writerow(record)
    shutil.copyfile(orig,dest)
#interface
l1=Label(w,text='جمعية عرب الحسون الخيرية',fg='red',font=14).grid(column=4,row=0,padx=20,pady=20,columnspan=3)
b1=Button(w,text='الحضانة',fg='red',font=14,command=child).grid(column=15,row=1,padx=50,pady=20,ipadx=20,ipady=10)
#b2=Button(w,text='فصول التقوية',
#b3=Button(w,text='تحفيظ القرآن',fg='red',font=14,command=button3).grid(column=9,row=1,padx=20,pady=20,ipadx=10,ipady=5)
b3=Button(w,text='الحسابات',fg='red',font=14,command=button4).grid(column=15,row=12,ipadx=20,ipady=20,padx=10,pady=60,columnspan=3)


















































w.mainloop()
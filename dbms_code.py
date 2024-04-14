from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import sqlite3
from tkinter import PhotoImage
from PIL import ImageTk, Image
import random
from datetime import date

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('new_record.db') as db:
    c = db.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY,password TEXT);')
db.commit()
db.close()

'''
conn = sqlite3.connect("medical_record.db")
c = conn.cursor()
c.execute("CREATE TABLE medical (first_name TEXT, last_name TEXT, age INT, blood_gp TXT, height INT, weight INT)")
conn.commit()
conn.close()
'''

#main Class


class main:
    def __init__(self, master):
    	# Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.age = IntVar()
        self.blood_group = StringVar()
        self.height = IntVar()
        self.weight = IntVar()
        self.widgets()

    #Login Function

    def login(self):
    	#Establish Connection
        with sqlite3.connect('new_record.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + ' Logged In'
            self.head['pady'] = 25
            self.main_screen()
            ms.showinfo("Log In", "Log In Successfully !")
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('new_record.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        #Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    #Draw Widgets

    def widgets(self):

        #opening screen
        frm0 = Frame(root, bg="lavender", bd=7)
        frm0.place(x=0, y=0, width=1450, height=750)

        image2 = Image.open("back_img_edit.jpg")
        image2 = ImageTk.PhotoImage(image2)
        lbl_img2 = Label(image=image2)
        lbl_img2.image = image2
        lbl_img2.place(x=0, y=0)

        image1 = Image.open("Picture1a.png")
        image1 = ImageTk.PhotoImage(image1)
        lbl_img1 = Label(image=image1)
        lbl_img1.image = image1
        lbl_img1.place(x=515, y=300)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        frm2 = Frame(root, bg="steel blue", bd=5)
        frm2.place(x=490, y=0, width=500, height=200)
        self.head = Label(root, text="Welcome to Heal Hands",
                          relief=SUNKEN, fg="black", font=("Times", 22), bg="yellow")
        self.head.place(x=40, y=10, width=500, height=50)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text="Enter User ID:", fg="black", font=("Helvetica", 16),
              bg="light cyan", borderwidth=3, relief="sunken", pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username,
              bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text="   Password :  ", fg="black", font=("Helvetica", 16),
              bg="light cyan", borderwidth=3, relief="sunken", pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5,
              font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), bg="light green",
               fg="black", padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), bg="light green",
               fg="black", padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', fg="black", font=("Helvetica", 16),
              bg="light cyan", borderwidth=3, relief="sunken", pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username,
              bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', fg="black", font=("Helvetica", 16),
              bg="light cyan", borderwidth=3, relief="sunken", pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5,
              font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=(
            '', 15), bg="light goldenrod", fg="black", padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), bg="light goldenrod",
               fg="black", padx=5, pady=5, command=self.log).grid(row=2, column=1)

    def insert_db(self):

        with sqlite3.connect('new_record.db') as db:
            c = db.cursor()

        print(age_insert)

        insert = 'INSERT INTO user(age) VALUES(?)'
        c.execute(insert, [age_insert])
        db.commit()
        db.close()

    def your_profile(self):

        global age_insert

        with sqlite3.connect('new_record.db') as db:
            c = db.cursor()

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="Enter Record", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.record_entry)
        btn.place(x=500, y=50, width=150, height=50)

        btn = Button(root, text="Display Record", bg="goldenrod3",
                     fg="black", font=("Helvetica"), bd=5)
        btn.place(x=1000, y=50, width=150, height=50)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

        '''photo = PhotoImage(file = "back_button.png") 
        btn=Button(root, image=photo,command=self.back).pack(side=RIGHT)
        Button.pack(side=RIGHT)'''

        frm1 = Frame(root, bg="black", bd=7)
        frm1.place(x=268, y=128, width=280, height=35)

        lbl2 = Label(root, text=" Enter the Following Details :- ",
                     fg="black", font=("Bahnschrift", 16), bg="Light salmon")
        lbl2.place(x=270, y=130, width=275, height=30)

        '''    lbl3=Label(root,text=" First Name ", fg="black", font=("Helvetica",16) ,bg="PeachPuff2")
        lbl3.place(x=270,y=200,width=150,height=30)
        e1=Entry(root,textvariable = self.first_name,bg="white",fg="black", font=("Helvetica",16) ,bd=5)
        e1.place(x=450,y=200,width=230,height=30)
        self.first_name = e1.get()'''

        '''--------------------------------------------------------------------------------------'''

        lbl5 = Label(root, text=" Age ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl5.place(x=270, y=300, width=50, height=30)
        e3 = Entry(root, textvariable=self.age, bg="white",
                   fg="black", font=("Helvetica", 16), bd=5)
        e3.place(x=450, y=300, width=230, height=30)
        age_insert = e3.get()

        btn = Button(root, text="Enter Record", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.insert_db)
        btn.place(x=500, y=50, width=150, height=50)

        '''----------------------------------------------------------------------------------------'''

        lbl4 = Label(root, text=" Last Name ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl4.place(x=270, y=250, width=130, height=30)
        e2 = Entry(root, textvariable=self.last_name, bg="white",
                   fg="black", font=("Helvetica", 16), bd=5)
        e2.place(x=450, y=250, width=230, height=30)
        self.last_name = e2.get()

        lbl6 = Label(root, text=" Blood Group ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl6.place(x=270, y=350, width=150, height=30)
        e4 = Entry(root, textvariable=self.blood_group, bg="white",
                   fg="black", font=("Helvetica", 16), bd=5)
        e4.place(x=450, y=350, width=230, height=30)
        self.blood_group = e4.get()

        lbl7 = Label(root, text=" Height ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl7.place(x=270, y=400, width=80, height=30)
        e5 = Entry(root, textvariable=self.height, bg="white",
                   fg="black", font=("Helvetica", 16), bd=5)
        e5.place(x=450, y=400, width=230, height=30)
        self.height = e5.get()

        lbl8 = Label(root, text=" Weight ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl8.place(x=270, y=450, width=80, height=30)
        e6 = Entry(root, textvariable=self.weight, bg="white",
                   fg="black", font=("Helvetica", 16), bd=5)
        e6.place(x=450, y=450, width=230, height=30)
        self.weight = e6.get()

    def record_entry(self):

        name = self.first_name.get()

        print(name)
        '''
        print(self.last_name)
        print(self.age)
        print(self.blood_group)
        print(self.height)
        '''

    def Medical_record(self):

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

        '-----------------------------'

        #cart
        frm2 = Frame(root, bg="pale violet red", bd=5)
        frm2.place(x=350, y=10, width=295, height=530)

        lblfrm = LabelFrame(root, text="R E P O R T")
        lblfrm.place(x=352, y=13, width=285, height=500)

        img1 = Image.open("report2.png")
        img = ImageTk.PhotoImage(img1)
        lbl_img = Label(image=img)
        lbl_img.image = img
        lbl_img.place(x=550, y=30)

        btn = Button(root, text="FACTS", bg="goldenrod3", fg="black", font=(
            "Bahnschrift SemiBold", 23), bd=5, command=self.facts)
        btn.place(x=70, y=600, width=100, height=38)

        lbl = Label(root, text=" Enter your Medical Report ",
                    font=('Bahnschrift 10 underline'))
        lbl.place(x=355, y=60, width=150, height=30)

        bl1 = Label(root, text=" Blood Group -")
        bl1.place(x=355, y=100)
        b1 = Entry()
        b1.place(x=550, y=100, width=40, height=30)

        bl2 = Label(root, text=" Hemoglobin -")
        bl2.place(x=355, y=150)
        b2 = Entry()
        b2.place(x=550, y=150, width=40, height=30)

        bl3 = Label(root, text=" SpO2 Level -")
        bl3.place(x=355, y=200)
        b3 = Entry()
        b3.place(x=550, y=200, width=40, height=30)

        bl4 = Label(root, text=" Sugar Level -")
        bl4.place(x=355, y=250)
        b4 = Entry()
        b4.place(x=550, y=250, width=40, height=30)

        bl5 = Label(root, text=" RCBs -")
        bl5.place(x=355, y=300)
        b5 = Entry()
        b5.place(x=550, y=300, width=40, height=30)

        bl6 = Label(root, text=" Platelets -")
        bl6.place(x=355, y=350)
        b6 = Entry()
        b6.place(x=550, y=350, width=40, height=30)

        '----------'
        frm2 = Frame(root, bg="pale violet red", bd=5)
        frm2.place(x=950, y=10, width=295, height=530)

        lblfrm = LabelFrame(root, text="R E P O R T")
        lblfrm.place(x=952, y=13, width=285, height=500)

        img1 = Image.open("report2.png")
        img = ImageTk.PhotoImage(img1)
        lbl_img = Label(image=img)
        lbl_img.image = img
        lbl_img.place(x=1150, y=30)

        btn = Button(root, text="FACTS", bg="goldenrod3", fg="black", font=(
            "Bahnschrift SemiBold", 23), bd=5, command=self.facts)
        btn.place(x=70, y=600, width=100, height=38)

        lbl = Label(root, text=" Enter your Medical Report ",
                    font=('Bahnschrift 10 underline'))
        lbl.place(x=955, y=60, width=150, height=30)

        bl1 = Label(root, text=" Blood Group -")
        bl1.place(x=955, y=100)
        b1 = Entry()
        b1.place(x=1145, y=100, width=40, height=30)

        bl2 = Label(root, text=" Hemoglobin -")
        bl2.place(x=955, y=150)
        b2 = Entry()
        b2.place(x=1145, y=150, width=40, height=30)

        bl3 = Label(root, text=" SpO2 Level -")
        bl3.place(x=955, y=200)
        b3 = Entry()
        b3.place(x=1145, y=200, width=40, height=30)

        bl4 = Label(root, text=" Sugar Level -")
        bl4.place(x=955, y=250)
        b4 = Entry()
        b4.place(x=1145, y=250, width=40, height=30)

        bl5 = Label(root, text=" RCBs -")
        bl5.place(x=955, y=300)
        b5 = Entry()
        b5.place(x=1145, y=300, width=40, height=30)

        bl6 = Label(root, text=" Platelets -")
        bl6.place(x=955, y=350)
        b6 = Entry()
        b6.place(x=1145, y=350, width=40, height=30)

        '--------'

        frm2 = Frame(root, bg="pale violet red", bd=5)
        frm2.place(x=650, y=10, width=295, height=530)

        lblfrm = LabelFrame(root, text="R E P O R T")
        lblfrm.place(x=652, y=13, width=285, height=500)

        img1 = Image.open("report2.png")
        img = ImageTk.PhotoImage(img1)
        lbl_img = Label(image=img)
        lbl_img.image = img
        lbl_img.place(x=850, y=30)

        btn = Button(root, text="FACTS", bg="goldenrod3", fg="black", font=(
            "Bahnschrift SemiBold", 23), bd=5, command=self.facts)
        btn.place(x=70, y=600, width=100, height=38)

        lbl = Label(root, text=" Enter your Medical Report ",
                    font=('Bahnschrift 10 underline'))
        lbl.place(x=655, y=60, width=150, height=30)

        bl1 = Label(root, text=" Blood Group -")
        bl1.place(x=655, y=100)
        b1 = Entry()
        b1.place(x=847, y=100, width=40, height=30)

        bl2 = Label(root, text=" Hemoglobin -")
        bl2.place(x=655, y=150)
        b2 = Entry()
        b2.place(x=847, y=150, width=40, height=30)

        bl3 = Label(root, text=" SpO2 Level -")
        bl3.place(x=655, y=200)
        b3 = Entry()
        b3.place(x=847, y=200, width=40, height=30)

        bl4 = Label(root, text=" Sugar Level -")
        bl4.place(x=655, y=250)
        b4 = Entry()
        b4.place(x=847, y=250, width=40, height=30)

        bl5 = Label(root, text=" RCBs -")
        bl5.place(x=655, y=300)
        b5 = Entry()
        b5.place(x=847, y=300, width=40, height=30)

        bl6 = Label(root, text=" Platelets -")
        bl6.place(x=655, y=350)
        b6 = Entry()
        b6.place(x=847, y=350, width=40, height=30)

        btn7 = Button(root, text=" Submit ", bg="blue4",
                      fg="white", font=("Bahnschrift SemiBold", 20), bd=5)
        btn7.place(x=750, y=600, width=150, height=50)

        frm0 = Frame(root, bg="LightSkyBlue2", bd=7)
        frm0.place(x=0, y=0, width=250, height=750)

        img0 = Image.open("brain.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=10, y=20)

        img0 = Image.open("eyes.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=80, y=140)

        img0 = Image.open("liver.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=10, y=240)

        img0 = Image.open("kidney.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=140, y=300)

        img0 = Image.open("heart.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=10, y=400)

        img0 = Image.open("intestine.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=110, y=530)

    def Search_doner(self):

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

    def Make_request(self):

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

        frm1 = Frame(root, bg="black", bd=7)
        frm1.place(x=460, y=10, width=540, height=70)
        lbl1 = Label(root, text="Welcome to Heal Hands", relief=SUNKEN,
                     fg="black", font=("Times", 22), bg="orange")
        lbl1.place(x=480, y=20, width=500, height=50)

        lbl3 = Label(root, text=" Enter Your Request ", fg="black",
                     font=("Helvetica", 16), bg="PeachPuff2")
        lbl3.place(x=270, y=150, width=200, height=30)
        e1 = Entry(root, bg="white", fg="black", font=("Helvetica", 16), bd=5)
        e1.place(x=450, y=200, width=700, height=400)

        btn7 = Button(root, text=" Submit ", bg="blue4",
                      fg="white", font=("Bahnschrift SemiBold", 13), bd=5)
        btn7.place(x=1000, y=600, width=80, height=30)

    def call_expert(self):

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

    def Book6(self):

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

    def facts(self):

        img0 = Image.open("fact_bg.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

        fact1 = Image.open("fact1.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=275, y=70)

        fact1 = Image.open("fact2-2.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=685, y=10)

        fact1 = Image.open("fact2-1.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=900, y=60)

        fact1 = Image.open("fact4-1.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=300, y=250)

        fact1 = Image.open("fact4-2.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=680, y=230)

        fact1 = Image.open("fact3.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=900, y=250)

        fact1 = Image.open("fact5.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=520, y=480)

        fact1 = Image.open("Organ.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=260, y=420)

        fact1 = Image.open("graph.jpg")
        fact1 = ImageTk.PhotoImage(fact1)
        lbl_fact1 = Label(image=fact1)
        lbl_fact1.image = fact1
        lbl_fact1.place(x=930, y=420)

    def destroy(self):
        ms.showinfo("Log Out", "Logged out successfully !")
        root.destroy()

    def back(self):
        self.main_screen()

    def certificate(self):

        global textarea, weltext
        img0 = Image.open("main_bg.jpg")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        frm2 = Frame(root, bg="black", bd=7)
        frm2.place(x=400, y=10, width=910, height=575)

        textarea = Text(frm2, width=400, height=400)
        textarea.pack()

        self.welcome()

        textarea.insert(
            END, f"\n\t This is to certify that Mr/Ms __________ \n\n")
        textarea.insert(END, f"\t has recieved the organ _________ \n\n")
        textarea.insert(END, f"\t from our organ bank    HEAL HANDS .\n\n\n\n")
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        textarea.insert(END, f"\t\t {d1} \n")
        textarea.insert(
            END, f"\t\t      Date                                 ")

        seal = Image.open("seal.jpg")
        seal = ImageTk.PhotoImage(seal)
        lbl_seal = Label(image=seal)
        lbl_seal.image = seal
        lbl_seal.place(x=1050, y=400)

        seal = Image.open("cetitle.jpg")
        seal = ImageTk.PhotoImage(seal)
        lbl_seal = Label(image=seal)
        lbl_seal.image = seal
        lbl_seal.place(x=640, y=50)

    def welcome(self):
        global weltext
        textarea.delete(1.0, END)
        textarea.insert(
            END, "\n\n\t\t                 C E R T I F I C A T E\n\n")
        textarea.insert(END, "\n")
        textarea.configure(font='arial 18 bold')

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1350, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)
        '''img7 = Image.open("certificate.jpg")
        bk6= ImageTk.PhotoImage(img7)
        lbl_img6 = Label(image=bk6,bg="snow3",bd=3)
        lbl_img6.image = bk6
        lbl_img6.place(x=1250,y=300)'''

    def faq(self):

        frm1 = Frame(root, bg="black", bd=7)
        frm1.place(x=460, y=10, width=540, height=70)
        lbl1 = Label(root, text="Heal Hands", relief=SUNKEN,
                     fg="black", font=("Times", 22), bg="pink")
        lbl1.place(x=600, y=20, width=150, height=50)

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="BACK", bg="MediumPurple1", fg="black",
                     font=('Bahnschrift', 16), bd=5, command=self.back)
        btn.place(x=260, y=10, width=70, height=50)

        frame1 = Frame(root, bg="black", bd=7)
        frame1.place(x=460, y=10, width=540, height=70)
        label1 = Label(root, text="+91 8955373717", relief=SUNKEN,
                       fg="black", font=("Times", 22), bg="yellow")
        label1.place(x=480, y=20, width=500, height=50)

    def main_screen(self):

        image2 = Image.open("back_img_edit.jpg")
        image2 = ImageTk.PhotoImage(image2)
        lbl_img2 = Label(image=image2)
        lbl_img2.image = image2
        lbl_img2.place(x=0, y=0)

        img0 = Image.open("macbook-bg.png")
        img0 = ImageTk.PhotoImage(img0)
        lbl_img0 = Label(image=img0)
        lbl_img0.image = img0
        lbl_img0.place(x=250, y=0)

        logo = Image.open("logo.jpeg")
        bk6 = ImageTk.PhotoImage(logo)
        lbl_logo = Label(image=bk6, bg="snow3", bd=3)
        lbl_logo.image = bk6
        lbl_logo.place(x=1300, y=25)

        btn = Button(root, text="FACTS", bg="goldenrod3", fg="black", font=(
            "Bahnschrift SemiBold", 23), bd=5, command=self.facts)
        btn.place(x=90, y=675, width=100, height=38)

        btn = Button(root, text="Contact Us", bg="blue4", fg="white", font=(
            "Bahnschrift SemiBold", 13), bd=5, command=self.faq)
        btn.place(x=1150, y=25, width=120, height=38)

        #title
        '''    
        frm1=Frame(root,bg="black",bd=7)
        frm1.place(x=643,y=10,width=340,height=70)
        lbl1=Label(root,text="HEAL HANDS", fg="black", font=("Bahnschrift SemiBold",23) ,bg="coral")
        lbl1.place(x=660,y=20,width=300,height=50)'''

        frm1 = Frame(root, bg="SteelBlue1", bd=7)
        frm1.place(x=625, y=5, width=314, height=88)

        img1 = Image.open("title.jpeg")
        img = ImageTk.PhotoImage(img1)
        lbl_img = Label(image=img)
        lbl_img.image = img
        lbl_img.place(x=630, y=10)

        #Your_profile
        img2 = Image.open("profile3.jpg")
        bk1 = ImageTk.PhotoImage(img2)
        lbl_img1 = Label(image=bk1, bg="snow3", bd=3)
        lbl_img1.image = bk1
        lbl_img1.place(x=370, y=100)
        btn1 = Button(root, text="Your Profile", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.your_profile)
        btn1.place(x=370, y=270, width=150, height=50)

        #book2
        img3 = Image.open("record.jpg")
        bk2 = ImageTk.PhotoImage(img3)
        lbl_img2 = Label(image=bk2, bg="snow3", bd=3)
        lbl_img2.image = bk2
        lbl_img2.place(x=700, y=100)
        btn2 = Button(root, text="Medical Records", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.Medical_record)
        btn2.place(x=700, y=270, width=170, height=50)

        #book3
        img4 = Image.open("search.png")
        bk3 = ImageTk.PhotoImage(img4)
        lbl_img3 = Label(image=bk3, bg="snow3", bd=3)
        lbl_img3.image = bk3
        lbl_img3.place(x=1050, y=100)
        btn3 = Button(root, text="Search a Doner", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.Search_doner)
        btn3.place(x=1050, y=270, width=160, height=50)

        #book4
        img5 = Image.open("request.jpg")
        bk4 = ImageTk.PhotoImage(img5)
        lbl_img4 = Label(image=bk4, bg="snow3", bd=3)
        lbl_img4.image = bk4
        lbl_img4.place(x=370, y=420)
        btn4 = Button(root, text="Make a Request", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.Make_request)
        btn4.place(x=370, y=590, width=160, height=50)

        #book5
        img6 = Image.open("call.png")
        bk5 = ImageTk.PhotoImage(img6)
        lbl_img5 = Label(image=bk5, bg="snow3", bd=3)
        lbl_img5.image = bk5
        lbl_img5.place(x=700, y=420)
        btn5 = Button(root, text="Call an Expert", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.call_expert)
        btn5.place(x=700, y=590, width=150, height=50)

        #book6
        img7 = Image.open("log.jpg")
        bk6 = ImageTk.PhotoImage(img7)
        lbl_img6 = Label(image=bk6, bg="snow3", bd=3)
        lbl_img6.image = bk6
        lbl_img6.place(x=1050, y=420)
        btn6 = Button(root, text="Log Out", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.destroy)
        btn6.place(x=1050, y=590, width=120, height=50)

        img7 = Image.open("certificate.jpg")
        bk6 = ImageTk.PhotoImage(img7)
        lbl_img6 = Label(image=bk6, bg="snow3", bd=3)
        lbl_img6.image = bk6
        lbl_img6.place(x=1250, y=300)
        btn6 = Button(root, text="Certificate", bg="goldenrod3", fg="black", font=(
            "Helvetica"), bd=5, command=self.certificate)
        btn6.place(x=1270, y=440, width=120, height=50)

        #cart
        frm2 = Frame(root, bg="pale violet red", bd=5)
        frm2.place(x=5, y=10, width=245, height=530)

        lblfrm = LabelFrame(root, text="R E P O R T")
        lblfrm.place(x=12, y=13, width=230, height=500)

        img1 = Image.open("report2.png")
        img = ImageTk.PhotoImage(img1)
        lbl_img = Label(image=img)
        lbl_img.image = img
        lbl_img.place(x=150, y=30)

        bl1 = Label(root, text=" Blood Group -")
        bl1.place(x=20, y=100)
        b1 = Entry()
        b1.place(x=180, y=100, width=40, height=30)

        bl2 = Label(root, text=" Hemoglobin -")
        bl2.place(x=20, y=150)
        b2 = Entry()
        b2.place(x=180, y=150, width=40, height=30)

        bl3 = Label(root, text=" SpO2 Level -")
        bl3.place(x=20, y=200)
        b3 = Entry()
        b3.place(x=180, y=200, width=40, height=30)

        bl4 = Label(root, text=" Sugar Level -")
        bl4.place(x=20, y=250)
        b4 = Entry()
        b4.place(x=180, y=250, width=40, height=30)

        bl5 = Label(root, text=" RCBs -")
        bl5.place(x=20, y=300)
        b5 = Entry()
        b5.place(x=180, y=300, width=40, height=30)

        bl6 = Label(root, text=" Platelets -")
        bl6.place(x=20, y=350)
        b6 = Entry()
        b6.place(x=180, y=350, width=40, height=30)

        bl7 = Label(root, text=" Vitamins D-")
        bl7.place(x=20, y=400)


if __name__ == '__main__':
	#Create Object
	#and setup window

    root = Tk()
    root.title('Login Form')
    root.geometry('1450x750+30+30')
    main(root)

root.mainloop()

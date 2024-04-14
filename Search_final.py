#!/usr/bin/env python
# coding: utf-8

# In[37]:


#!/usr/bin/env python
# coding: utf-8

# In[25]:


from tkinter import *
import sqlite3
import tkinter.ttk as ttk

def Search_donor():
    root = Tk()
    root.title("Sourcecodester")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    #=====================================METHODS==============================================
    def Database():
        conn = sqlite3.connect("new_record.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `Donor` ORDER BY `donor_id` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Search():
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("new_record.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Donor` WHERE `name` LIKE ? OR `donor_id` LIKE ?", ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH.get())+'%'))
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
    def Reset():
        conn = sqlite3.connect("new_record.db")
        cursor = conn.cursor()
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `Donor` ORDER BY `donor_id` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    #=====================================VARIABLES============================================
    SEARCH = StringVar()

    #=====================================FRAME================================================
    Top = Frame(root, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    TopFrame = Frame(root, width=500)
    TopFrame.pack(side=TOP)
    TopForm= Frame(TopFrame, width=300)
    TopForm.pack(side=LEFT, pady=10)
    TopMargin = Frame(TopFrame, width=260)
    TopMargin.pack(side=LEFT)
    MidFrame = Frame(root, width=500)
    MidFrame.pack(side=TOP)

    #=====================================LABEL WIDGET=========================================
    lbl_title = Label(Top, width=500, font=('arial', 18), text="Python: Simple Table Search Filter")
    lbl_title.pack(side=TOP, fill=X)

    #=====================================ENTRY WIDGET=========================================
    search = Entry(TopForm, textvariable=SEARCH)
    search.pack(side=LEFT)

    #=====================================BUTTON WIDGET========================================
    btn_search = Button(TopForm, text="Search", bg="#006dcc", command=Search)
    btn_search.pack(side=LEFT)
    btn_reset = Button(TopForm, text="Reset", command=Reset)
    btn_reset.pack(side=LEFT)
    #=====================================Table WIDGET=========================================
    scrollbarx = Scrollbar(MidFrame, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidFrame, orient=VERTICAL)
    tree = ttk.Treeview(MidFrame, columns=("donor_id", "Name", "Organ", "blood_grp","age","state"), selectmode="extended", height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('donor_id', text="Donor ID",anchor=W)
    tree.heading('Name', text="Donor Name",anchor=W)
    tree.heading('Organ', text="Organ",anchor=W)
    tree.heading('blood_grp', text="Blood Group",anchor=W)
    tree.heading('age', text="Age",anchor=W)
    tree.heading('state', text="State",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=170)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=80)
    tree.pack()


#=====================================INITIALIZATION=======================================
root.mainloop()


# In[ ]:


# In[36]:


Search_donor()


# In[ ]:





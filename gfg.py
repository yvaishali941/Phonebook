#CONTACT APPLICATION 

import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, FALSE, LEFT, RIGHT, SUNKEN, TOP, Y
import sqlite3
from tkinter import ttk
import PIL
import PIL.Image
import PIL.ImageTk

conn=sqlite3.connect('contactapp/contacts.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS CONTACT_DETAILS
              ( NAME TEXT,
                NUMBER TEXT,
                EMAIL TEXT,
                ADDRESS TEXT,
                WORK_INFO TEXT,
                IMP_DATES TEXT,
                RELATION TEXT
                  )''')

cur.execute('''CREATE TABLE IF NOT EXISTS IMP_DATES(
    Title TEXT,
    Date TEXT
    )''')
cur.close()
conn.commit()
conn.close()
 
class mainpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)      
        conn=sqlite3.connect("contactapp/contacts.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM CONTACT_DETAILS")
        datas=cur.fetchall()
        my_names=[]
        my_numbers=[]
        for row in datas:
            my_names.append(row[0])
            my_numbers.append(row[1])
        conn.commit()
        conn.close()
        my_names.sort()
        
        f1=tk.Frame(self,height=30,bg="green")
        f1.pack(fill="x")
        
        f2=tk.Frame(self,height=500,bg="yellow")
        f2.pack(fill="x")

        
        image=PIL.Image.open("/home/vaishu/Desktop/python pro/con1.jpeg")
        load=image.resize((50,50), PIL.Image.ANTIALIAS)
        photo=PIL.ImageTk.PhotoImage(image=load)
        cont_icon=tk.Label(f1,image = photo)
        cont_icon.image=photo
        cont_icon.pack(side=LEFT,padx=(50,0))
        label1=tk.Label(f1,text="PhoneBook",font=("times new roman",20),pady=20)
        label1.place(x=180,y=5)
        
        search_box=tk.Entry(f2,width=39,font=("times new roman",12))
        search_box.grid(row=0,column=0,columnspan=5)
        
        My_scroll=tk.Scrollbar(f2,orient="vertical")
        
        contact_list=tk.Listbox(f2,height=200,width=38)
        for names in my_names:
            contact_list.insert(tk.END,names)
        contact_list.grid(row=1,column=0)
        My_scroll.grid(row=1,column=1,sticky="ns")
        My_scroll.config(command=contact_list.yview)
        
        b1=tk.Button(f2,text="Add Contact",font=("timesnewroman",12),relief=SUNKEN,command= lambda: controller.showframe(createnew))
        b1.place(x=360,y=150)
        b2=tk.Button(f2,text="Update Contact",font=("timesnewroman",12),relief=SUNKEN)
        b2.place(x=350,y=190)
        b3=tk.Button(f2,text="Delete Contact",font=("timesnewroman",12),relief=SUNKEN)
        b3.place(x=352,y=230)
    

class createnew(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)
        print(self.winfo_geometry())
        self.config(background="cyan")
        def clickname(event):
            name.config(state=tk.NORMAL)
            name.delete(0,tk.END)
        def clickph_no(event):
            ph_no.config(state=tk.NORMAL)
            ph_no.delete(0,tk.END)
        def clickemail(event):
            email.config(state=tk.NORMAL)
            email.delete(0,tk.END)
        
        def clickaddr(event):
            addr.config(state=tk.NORMAL)
            addr.delete(0,tk.END)
        def clickworkinfo(event):
            workinfo.config(state=tk.NORMAL)
            workinfo.delete(0,tk.END)
        def clickimpd(event):
            imp_dates.config(state=tk.NORMAL)
            imp_dates.delete(0,tk.END)
            date=tk.Tk()
            date.geometry("400x300")
            date.resizable(0,0)
            l1=tk.Label(date,text="Select type of important date",font=("timesnewroman",15))
            l1.pack()
            v = tk.StringVar(date, "1")
 
            values = {"Birthday" : "Birthday",
                    "Anniversary" : "Anniversary",
                    "Other" : "Other"
                    }
            for (text, value) in values.items():
                rb=tk.Radiobutton(date, text = text, variable = v,
                    value = value)
                rb.pack(side = tk.TOP, ipady = 5)
                
            
            l=tk.Label(date,text="Set Date",font=("timesnewroman",15))
            l.pack(anchor="w")
            months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            days= (1, '2', '3', '4', '5', '6', '7', '8', '9', 
                   '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
            years= ('2018', '2019', '2020', '2021', '2022','2023', '2024')
            
            month=tk.StringVar()
            year=tk.StringVar()
            day=tk.StringVar(value='day')
            
            day_box=ttk.Combobox(date,textvariable=day,width=15)
            day_box['values']=days
            day_box['state']='readonly'
            day_box.set("day")
            day_box.pack(side=LEFT)
            
            month_box=ttk.Combobox(date,textvariable=month,width=15)
            month_box['values']=months
            month_box['state']='readonly'
            month_box.set("month")
            month_box.pack(side=LEFT)
            
            year_box=ttk.Combobox(date,textvariable=year,width=15)
            year_box['values']=years
            year_box['state']='readonly'
            year_box.set("year")
            year_box.pack(side=LEFT)
            
            
            def save_date():
                my_date= day_box.get()+"-"+ month_box.get()+"-"+year_box.get()
                entry_set= v.get()+", "+day_box.get()+" "+ month_box.get()
                conn = sqlite3.connect('contactapp/contacts.db')
                cur= conn.cursor()
                cur.execute("INSERT INTO IMP_DATES VALUES ('%s','%s')"%(v.get(),my_date))
                cur.close()
                conn.commit()
                conn.close()
                imp_dates.insert(0,entry_set)
                date.destroy()
 
            
            save=tk.Button(date,text="Save",font=("timesnewroman",15),command=save_date)
            save.place(x=150,y=255)

            date.mainloop()
      
        def clickrel(event):
            relation.config(state=tk.NORMAL)
            relation.delete(0,tk.END)
        
        
        
        
        name=tk.Entry(self,font=("times new roman",15))
        ph_no=tk.Entry(self,font=("times new roman",15))
        email=tk.Entry(self,font=("times new roman",15))
        workinfo=tk.Entry(self,font=("times new roman",15))
        addr=tk.Entry(self,font=("times new roman",15))
        imp_dates=tk.Entry(self,font=("times new roman",15))
        relation=tk.Entry(self,font=("times new roman",15))
        
        name.insert(0,"Name")
        ph_no.insert(0,"Phone Number")
        email.insert(0,"Email")
        workinfo.insert(0,"Work Info")
        addr.insert(0,"Address")
        imp_dates.insert(0,"Important Dates")
        relation.insert(0,"Relation")
        
        name.config(state=tk.DISABLED)
        ph_no.config(state=tk.DISABLED)
        email.config(state=tk.DISABLED)
        workinfo.config(state=tk.DISABLED)
        addr.config(state=tk.DISABLED)
        imp_dates.config(state=tk.DISABLED)
        relation.config(state=tk.DISABLED)
        
        name.bind("<Button-1>",clickname)
        ph_no.bind("<Button-1>",clickph_no)
        email.bind("<Button-1>",clickemail)
        workinfo.bind("<Button-1>",clickworkinfo)
        imp_dates.bind("<Button-1>",clickimpd)
        addr.bind("<Button-1>",clickaddr)
        relation.bind("<Button-1>",clickrel)
        
        
        name.pack(fill="x",pady=(10,5))
        ph_no.pack(fill="x",pady=5)
        email.pack(fill="x",pady=5)
        workinfo.pack(fill="x",pady=5)
        addr.pack(fill="x",pady=5)
        imp_dates.pack(fill="x",pady=5)
        relation.pack(fill="x",pady=5)
        
        def save_details():
            conn=sqlite3.connect("contactapp/contacts.db")
            cur=conn.cursor()
            cur.execute("INSERT INTO CONTACT_DETAILS VALUES('%s','%s','%s','%s','%s','%s','%s')"%(name.get(),ph_no.get(),email.get(),addr.get(),workinfo.get(),imp_dates.get(),relation.get()))
            cur.close()
            conn.commit()
            conn.close()
            print("your contact saved sucessfully")
            controller.showframe(mainpage)
            

            
        b1=tk.Button(self,text="Cancel",font=("timesnewroman",15),command=lambda:controller.showframe(mainpage))
        b1.place(x=150,y=350)
        b2=tk.Button(self,text="Save",font=("timesnewroman",15),command=save_details)
        b2.place(x=238,y=350)

class Contactapp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk. __init__(self,*args,**kwargs )
 
        # creating window
        root=tk.Frame(self)
        root.pack()
        
        root.grid_rowconfigure(0,minsize=500)
        root.grid_columnconfigure(0,minsize=500)
        
        
        self.frames={}
        for F in (mainpage,createnew):
            frame=F(root,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        
        self.showframe(mainpage)
        
    def showframe(self,page):
        frame=self.frames[page]
        frame.tkraise()
        
            
            
app = Contactapp()

app.geometry("500x600")
app.resizable(0,0)

app.mainloop()
        
        
       
        
    








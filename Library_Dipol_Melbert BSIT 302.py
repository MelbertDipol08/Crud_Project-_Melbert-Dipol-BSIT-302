from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox

Library = []

def update6():
    b6['state'] = DISABLED
    b7['state'] = NORMAL
    b2['state'] = DISABLED
    e1.insert(0,emp.getFirstname())
    e2.insert(0,emp.getLastname())
    e4.insert(0,emp.getCourse())
    e5.insert(0,emp.getSection())
    e6.insert(0,emp.getTitle())
def update7():
    b6['state'] = NORMAL
    b7['state'] = DISABLED

    MsgBox = messagebox.askquestion ('Update ','Are you sure you want to Update?',icon = 'warning')
    if MsgBox == 'yes':
        selected_item = tv.selection()[0]
        tv.item(selected_item, text=e1.get(),values=(e2.get(),self_gender.get(),e4.get(),e5.get(),e6.get()))
        e1.delete(0, END)
        e2.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
       
        
    else:
        print("returning...")
        
def add_to_list():
    global emp

    print("Name: " + " " + e1.get(), e2.get() + "  " + "Gender: " + " " + self_gender.get()+ "  " +"Course: " + " " + e4.get()+ "  " +"Section: " + " " + e5.get()+ "  " + "Title: " + " " + e6.get())
    emp = Student(e1.get(), e2.get(),self_gender.get(),e4.get(),e5.get(),e6.get())
    a = e1.get()
    b = e2.get()
    c = self_gender.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()
    students.append(Student(a,b,c,d,e,f))
    students.append(emp)
    messagebox.showinfo("Dialog box", "Added")
    e1.delete(0, END)
    e2.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    b2['state'] = NORMAL
    
def read_list():
    tv.insert('','end', text=emp.getName(),values=(emp.getGender(),emp.getCourse(), emp.getSection(), emp.getTitle()))
    window.i = window.i + 1
    b2['state'] = DISABLED

def exit_prog():
    MsgBox = messagebox.askquestion ('Exit','Are you sure you want to Exit?',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        print("welcome back!")
    
def delete_to_list():
        MsgBox = messagebox.askquestion ('Delete','Are you sure you want to Delete?',icon = 'warning')
        if MsgBox == 'yes':
            selected_item = tv.selection()
            remove_emp = tv.detach(selected_item)
            e1.delete(0, END)
            e2.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
        else:
            messagebox.showinfo('Return','You will now return to the Main Screen')
  
class Student:
    def __init__(self, first_name, last_name, gender, course, section, title):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.course = course
        self.section = section
        self.title = title
        
    def getName(self):
        return self.first_name  + " " + self.last_name
    def getGender(self):
        self_gender.get()
        return self.gender
    
    def getCourse(self):
        return self.course
    
    def getSection(self):
        return self.section

    def getFirstname(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
    
    def getTitle(self):
        return self.title

window = Tk()
window.resizable(1, 50)
window.i = 10000000
self_gender = StringVar()
window.configure(background='Purple') 
window.title("Library")
Label(window, text="Full Name: ").grid(row=0, column=0, padx=10, pady=5)
Label(window, text="Students Number: ").grid(row=1, column=0, padx=10, pady=5)
Label(window, text="Course: ").grid(row=3, column=0, padx=10, pady=5)
Label(window, text="Section: ").grid(row=4, column=0, padx=10, pady=5)


e1 = Entry(window, width=15)

e2 = Entry(window, width=15)

e4 = Entry(window, width=15)

e5 = Entry(window, width=15)


e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e4.grid(row=3, column=1, padx=10, pady=5)
e5.grid(row=4, column=1, padx=10, pady=5)
e6 = Entry(window, width=15)


b1 = Button(window, text="        Insert        ", command=add_to_list)
b1.grid(row=4, column= 1, padx=10, pady=5,columnspan=4)

b2 = Button(window, text="       View      ", command=read_list)
b2.grid(row=4, column=2, padx=12, pady=10,columnspan=4)

b4 = Button(window, text="      Delete      ", command=delete_to_list)
b4.grid(row=4, column=3, padx=10, pady=5,columnspan=4)

b6 = Button(window, text="     Update     ",state=NORMAL, command=update6)
b6.grid(row=4, column=4 ,padx=10, pady=5, columnspan=4)

b5 = Button(window, text="        Exit         ", command=exit_prog)
b5.grid(row=4, column=5 ,padx=10, pady=5,columnspan=4)

b7 = Button(window, text="     Update     ",state=DISABLED, command=update7)
b7.grid(row=4, column=6 ,padx=10, pady=5,columnspan=4)

tv = ttk.Treeview(window, height=15,columns=('gender','Course','Section','title'))

tv.grid(row=5, column=0 , columnspan=6)


tv.heading('#0', text="Full Name")
tv.heading('#1', text="Students Number")
tv.heading('#2', text="Course")
tv.heading('#3', text="Section")

window.mainloop()

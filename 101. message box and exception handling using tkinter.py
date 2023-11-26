import tkinter as tk
from tkinter import ttk
window=tk.Tk()# create new window
from tkinter import messagebox as m_box #package for message

label_form=ttk.LabelFrame(window,text="contact detail")# create label frame
label_form.grid(row=0,column=0,padx=40,pady=10)# for position
name_label=ttk.Label(label_form,text="enter your name",font=('Helvetica',14))# create label of name
age_label=ttk.Label(label_form,text="enter your age",font=('helvetica',14))# create label of age
age_var=tk.StringVar()# varible for storing age
name_var=tk.StringVar()# variable for storing name
name_entry=ttk.Entry(label_form,width=36,textvariable=name_var)# create entry box
age_entry=ttk.Entry(label_form,width=36,textvariable=age_var)# create entry box
name_label.grid(row=0,column=0,padx=5,pady=5)# for posiiton
age_label.grid(row=0,column=1,padx=5,pady=5)# for position
age_entry.grid(row=1,column=1,padx=5,pady=5)# for position
name_entry.grid(row=1,column=0,padx=5,pady=5)# for position
def submit(): # function to define he action of submit button
    name=name_var.get()# get usr input for name
    age=age_var.get()# get user input age
    if name=='' or age=='':# if any of name or age is empty
        m_box.showerror('Error','please enter both name and age')# this will show error
    else:
        try:
            age=int(age)#convert age to integer type
        except ValueError:
            m_box.showerror('title','only numeric value')# show error
        else:
            print(f'{name} is {age} years old')# statement

submit_btn=ttk.Button(window,text='submit',command=submit)# create submit btn
submit_btn.grid(row=1,columnspan=2,padx=40)# for position
window.mainloop()# last line

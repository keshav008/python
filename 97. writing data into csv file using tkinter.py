import tkinter as tk
from csv import DictWriter
import os
window=tk.Tk() # creating object of tk class
window.title("GUI Application") #this will give title to new window

#CREATE LABELS
from tkinter import ttk
name_label=ttk.Label(window,text='Enter your name:')# create label on window with given text
name_label.grid(row=0,column=0)# this function is used for position
age_label=ttk.Label(window,text='Enter your age:')# create another label
age_label.grid(row=1,column=0)# function for position

#CREATE ENRTY BOX
name_var=tk.StringVar() # function of tkinter to store string value
name_entrybox=ttk.Entry(window,width=16,textvariable=name_var) # function for entrybox
name_entrybox.grid(row=0,column=1)# fucntion for position
age_var=tk.StringVar()# create another variable
age_entrybox=tk.Entry(window,width=14,textvariable=age_var)# crete box for age
age_entrybox.grid(row=1,column=1)# for position

#CREATE COMBOBOX
gender_var=tk.StringVar() #create variable
gender_combobox=ttk.Combobox(window,width=14,textvariable=gender_var,state='readonly')# here readonly will not allow us to type gender manully
gender_combobox['values']=('male','female','other')# values for combobox
gender_combobox.current(0)# this will show male as default value on combobox
gender_combobox.grid(row=3,column=0)# function for position

#CREATE RADIO BUTTONS
usertype=tk.StringVar()# create variable
radiobtn1=ttk.Radiobutton(window,text='student',value='student',variable=usertype)# create radio button for student
radiobtn1.grid(row=4,column=0)# for position
radiobtn2=ttk.Radiobutton(window,text='teacher',value='teacher',variable='usertype')# create radio buttton for teacher
radiobtn2.grid(row=4,column=1)# for position

#CREATE CHECK BUTTTON
checkbtn_var=tk.IntVar()# create variable
checkbtn=ttk.Checkbutton(window,text='Agree',variable=checkbtn_var)# create checkbutton
checkbtn.grid(row=5,columnspan=4)# here columnspan=3 will allow your taxt to extend upto 3 columns

#CREATE BUTTONS
def action(): # function for performing action using submit buttton
    username=name_var.get()# get name_var value form user and store in username
    userage=age_var.get()# get age_var value from user and store in userage
    print(f'{username} is {userage} years old') # statement to execute by action function
    user_gender=gender_var.get()# get usertype value and store in usergender
    user_type=usertype.get()# get user type and store in usertype according to butttons
    if checkbtn_var.get()==0:# condition for checkbtn_var
        subscribed='NO'
    else:
        subscribed='YES'
    print(user_gender,user_type,subscribed)# statement to print
    # writing data into a file
    with open('file1.csv','a') as f: # this will open a file in append mode
        dict_writer=DictWriter(f,fieldnames=['NAME','AGE','SEX','TYPE','SUBSCRIBED'])#we are creating caller(dict_writer) of DictWriter(use to write into csv file) where fieldname is a list of all the headers of this file
        if os.stat('file1.csv').st_size==0:# checking whether file is empty or not
            dict_writer.writeheader()# if file is empty it will write headers into that
        dict_writer.writerow( # this method is used to write row into csv file with dictionary and headers as key and values comes from user
            {'NAME':username,
             'AGE':userage,
             'SEX':user_gender,
             'TYPE':user_type,
             'SUBSCRIBED':subscribed
                })

    name_entrybox.delete(0,tk.END)# this will clear text of name_enrty box after submitting
    age_entrybox.delete(0,tk.END)# this will clear text of age_enrty box after submitting
    name_label.configure(foreground='Red')# this will change the color of name_label after submiting
    submit_button.configure(foreground='Blue')# this will change the color of age_label after submiting
  #creating submit button
submit_button=ttk.Button(window,text="submit",command=action)# we give function name as command to perform action
submit_button.grid(row=3,column=3)# for position of submit button


window.mainloop() # this will show newly created window on screen and this is the last line of any gui application with tkinter



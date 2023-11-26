import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("using loop")

labels=['NAME','AGE','GENEDR','COUNTRY','STATE','CITY']
for i in range(len(labels)):
    curr_label='lable'+str(i)
    curr_label=ttk.Label(window,text=labels[i])
    curr_label.grid(row=i,column=0,sticky=tk.W)

user_info={'name':tk.StringVar(),
           'age':tk.StringVar(),
           'gender':tk.StringVar(),
           'country':tk.StringVar(),
           'state':tk.StringVar(),
           'city':tk.StringVar()}
counter=0
for i in user_info:
    curr_entrybox='entry'+i
    curr_entrybox=ttk.Entry(window,width=16,textvariable=user_info[i])
    curr_entrybox.grid(column=1,row=counter)
    counter+=1

def action():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())

submit_button=ttk.Button(window,text='submit',command=action)
submit_button.grid(row=6,columnspan=2)
window.mainloop()

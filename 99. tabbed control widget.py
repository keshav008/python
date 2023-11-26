import tkinter as tk
from tkinter import ttk
window=tk.Tk()# function to create window
window.title("tab control")# add title to window
nb=ttk.Notebook(window)# create noetbook on the window
page1=ttk.Frame(nb)# create frames on newly created notebook nb
page2=ttk.Frame(nb)
nb.add(page1,text='ONE')# this will frames to notebook with given text
nb.add(page2,text='TWO')
nb.pack(expand=True,fill='both')# this is used insted of grid function
label1=ttk.Label(page1,text='this is label on page1:')# create label on page 1
label1.grid(row=0,column=0)# define position
label2=ttk.Label(page2,text='this is label on page2:')# create label on page 2
label2.grid(row=0,column=0)# define position
window.mainloop()# last line of code

import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("MENUBAR CREATION")

def func(): # function for labels
    print("calling of function")
menu_bar=tk.Menu(window)# create empty menu bar
menu_bar.add_command(label='save',command=func)# this will add label and command
main_menu=tk.Menu(window)# create main menu on window
file_menu=tk.Menu(main_menu,tearoff=0)#create menu bar on main menu
file_menu.add_command(label='New file',command=func)# add label and command
file_menu.add_command(label='SaveAs',command=func)# add label and command
file_menu.add_command(label='Open',command=func)#add another label and command
edit_menu=tk.Menu(main_menu,tearoff=0)# create edit menu on main menu
edit_menu.add_command(label='undo',command=func)# add label and command
edit_menu.add_command(label='redo',command=func)# add another label and commadn

main_menu.add_cascade(label='FILE',menu=file_menu)#this will add downway menu FILE
main_menu.add_cascade(label='EDIT',menu=edit_menu)# this will add downway menu EDIT
window.config(menu=main_menu)# we use config insted of grid in caes of menu bar


window.mainloop()# last line of code

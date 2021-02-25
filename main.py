from tkinter import *


def get_name():
    text = name_entry.get()


def clear_screen():
    things = root.grid_slaves()
    for l in things:
        l.destroy()


root = Tk()
name = Label(root, text='Name')
name.grid(row=0)
password = Label(root, text='Password')
password.grid(row=1)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)
pass_entry = Entry(root)
pass_entry.grid(row=1, column=1)
accept_button = Button(root, command=get_name, text='Log in')
accept_button.grid(row=2, column=1)

root.mainloop()

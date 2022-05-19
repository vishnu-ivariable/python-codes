import tkinter as tk
from tkinter import ttk
window = tk.Tk()  #creating an instance and assinginig to a veriable
window.title("python gui")
ttk.Label(window, text="A Lable").grid(column=0, row=0)

a_label = ttk.Label(window, text="basic gui")
a_label.grid(column=0, row=0)

def click_me():
    action.configure(text="** You have clicked! **")
    a_label.configure(foreground="red")
    a_label.configure(text= "A red lable")

action = ttk.Button(window, text="click Me!", command=click_me)
action.grid(column=1,row=0)

window.mainloop()
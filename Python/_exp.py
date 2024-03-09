from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import csv
import re

root = Tk()
root.title("RPG Maker MV Exp (30 Level)")
root.geometry("700x300")

def check_inp(val):
    return re.match("^[0-9\\.]*$",val) is not None and len(val) <= 5
check_num = (root.register(check_inp),"%P")
def check_inp2(val):
    return re.match("^[0-9]*$",val) is not None and len(val) <= 5
check_num2 = (root.register(check_inp2),"%P")

#second data validation
def data():
    file_name = inp1.get()
    base_exp = inp2.get()
    scale_exp = inp3.get()
    math_opt = opt.get()
    if file_name=="" or base_exp=="" or scale_exp=="":
        lbl_warn.config(text="please fill every form",fg="red")
    else:
        lbl_warn.config(text="please wait",fg="black")
        arty = [file_name, int(base_exp), float(scale_exp), math_opt]
        return arty

def draw_graph():
    data_list = data()
    cur_exp = data_list[1]
    scale = data_list[2]

    cur_lvl = []
    cur_val = []
    for i in range(30):
        cur_lvl.append(i+1)
        cur_val.append(math.ceil(cur_exp))
        if data_list[3]=="+":
            cur_exp+=scale
        elif data_list[3]=="*":
            cur_exp+=cur_exp*scale

    lbl_warn.config(text="complete, only showing up to lvl 30",fg="black")
    plt.plot(cur_lvl,cur_val)
    plt.suptitle("Up to level 30")
    plt.show()
    
def calculate():
    data_list = data()
    cur_exp = data_list[1]
    scale = data_list[2]
    for i in range(99):
        print(i+1,math.ceil(cur_exp))
        if data_list[3]=="+":
            cur_exp+=scale
        elif data_list[3]=="*":
            cur_exp+=cur_exp*scale
    lbl_warn.config(text="complete",fg="black")

inp1 = Entry(root,width=35)
inp1.grid(row=0,column=1)
inp2 = Entry(root,width=35,validate="key",validatecommand=check_num2)
inp2.grid(row=1,column=1)
inp3 = Entry(root,width=35,validate="key",validatecommand=check_num)
inp3.grid(row=2,column=1)

opt = ttk.Combobox(root,width=30)
opt["values"] = ("+","*")
opt.grid(row=3,column=1)
opt.current(1)
opt.state(["readonly"])

lbl1 = Label(root,text="File name")
lbl1.grid(row=0,column=0)
lbl2 = Label(root,text="Base exp")
lbl2.grid(row=1,column=0)
lbl3 = Label(root,text="Exp scale")
lbl3.grid(row=2,column=0)
lbl4 = Label(root,text="Operator")
lbl4.grid(row=3,column=0)


btn1 = Button(root,text="Create Graph",command=draw_graph)
btn1.grid(row=4,column=0,columnspan=2)
btn2 = Button(root,text="Create File",command=calculate)
btn2.grid(row=5,column=0,columnspan=2)

lbl_warn = Label(root,text="")
lbl_warn.grid(row=6,column=0,columnspan=2)

root.mainloop()

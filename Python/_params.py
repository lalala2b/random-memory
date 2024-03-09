from tkinter import *
import matplotlib.pyplot as plt
import math
import csv
import re

param = Tk()
param.title("RPG Maker MV Param")
param.geometry("700x300")

def check_inp(val):
    return re.match("^[0-9\\.]*$",val) is not None and len(val) <= 5
check_num = (param.register(check_inp),"%P")
def check_inp2(val):
    return re.match("^[0-9]*$",val) is not None and len(val) <= 5
check_num2 = (param.register(check_inp2),"%P")

def create_lbl(text1,text2,row,column):
    lbl1 = Label(param,text=text1)
    lbl1.grid(row=row,column=column)
    lbl2 = Label(param,text=text2)
    lbl2.grid(row=row+2,column=column)

def create_data():
    base_hp = hp_base.get()
    scale_hp = hp_scale.get()

    base_mp = mp_base.get()
    scale_mp = mp_scale.get()

    base_atk = atk_base.get()
    scale_atk = atk_scale.get()

    base_def = def_base.get()
    scale_def = def_scale.get()

    base_agi = agi_base.get()
    scale_agi = agi_scale.get()
    
    data_list = [["HP base",base_hp],
                 ["HP scale",scale_hp],
                 ["MP base",base_mp],
                 ["MP scale",scale_mp],
                 ["Attack base",base_atk],
                 ["Attack scale",scale_atk],
                 ["Defense base",base_def],
                 ["Defense scale",scale_def],
                 ["Agility base",base_agi],
                 ["Agility scale",scale_agi]]
    temp_data=[[] for i in range(5)]
    
    for i in range(len(data_list)):
        if data_list[i][1]=="":
            lbl_warn.config(text=f"please fill {data_list[i][0]}",fg="red")
            break
        else:
            data_id = math.floor(i/2)
            if i%2==0:
                temp_data[data_id].append(int(data_list[i][1]))
            elif i%2==1:
                temp_data[data_id].append(float(data_list[i][1]))

    final_data = [[] for i in range(5)]
    for i in range(len(temp_data)):
        if data_list[i][1]=="":
            lbl_warn.config(text=f"please fill {data_list[i][0]}",fg="red")
            break
        else:
            base = temp_data[i][0]
            for j in range(30):
                final_data[i].append(math.floor(base))
                base += temp_data[i][1]

    return final_data

def draw_graph():
    final_data = create_data()

    if len(final_data[1])==0:
        lbl_warn.config(text=f"please fill {data_list[i][0]}",fg="red")
    else:
        lbl_warn.config(text="please wait",fg="black")
        hp = plt.subplot2grid((2,3),(0,0))
        mp = plt.subplot2grid((2,3),(0,1))
        atk = plt.subplot2grid((2,3),(0,2))
        def_ = plt.subplot2grid((2,3),(1,0))
        agi = plt.subplot2grid((2,3),(1,1))

        hp.plot(final_data[0],final_data[1])
        hp.set_title("HP")
        mp.plot(final_data[0],final_data[2])
        mp.set_title("HP")
        atk.plot(final_data[0],final_data[3])
        atk.set_title("HP")
        def_.plot(final_data[0],final_data[4])
        def_.set_title("HP")
        agi.plot(final_data[0],final_data[5])
        agi.set_title("HP")

        plt.show()

def calculate():
    final_data = create_data()
    name = file_name.get()

    if name=="":
        lbl_warn.config(text="please fill the name",fg="red")
    elif len(final_data[1])!=0:
        lbl_warn.config(text="please wait",fg="black")
        for i in range(len(final_data)):
            for j in range(69):
                final_data[i].append(1)

        with open(name+".csv","w",newline="") as file:
            writer = csv.writer(file)
            field = ["Level","Max HP","Max MP","Attack","Defense",
                     "Magical Attack","Magical Defense","Agility","Luck"]
            writer.writerow(field)

            for i in range(99):
                writer.writerow([str(i+1),str(final_data[0][i]),str(final_data[1][i]),
                                 str(final_data[2][i]),str(final_data[3][i]),"1","1",
                                 str(final_data[4][i]),"1"])
        lbl_warn.config(text=f"complete, file name is {name}"+".csv",fg="green")
    

lbl_name = Label(param,text="File Name: ")
lbl_name.grid(row=0,column=0)

file_name = Entry(param,width=20)
file_name.grid(row=0,column=1)

create_lbl("HP base","HP scale",1,0)
create_lbl("MP base","MP scale",1,1)
create_lbl("Attack base","Attack scale",1,2)
create_lbl("Defense base","Defense scale",1,3)
create_lbl("Agility base","Agility scale",1,4)

hp_base = Entry(param,width=20,validate="key",validatecommand=check_num2)
hp_base.grid(row=2,column=0)
hp_scale = Entry(param,width=20,validate="key",validatecommand=check_num)
hp_scale.grid(row=4,column=0)

mp_base = Entry(param,width=20,validate="key",validatecommand=check_num2)
mp_base.grid(row=2,column=1)
mp_scale = Entry(param,width=20,validate="key",validatecommand=check_num)
mp_scale.grid(row=4,column=1)

atk_base = Entry(param,width=20,validate="key",validatecommand=check_num2)
atk_base.grid(row=2,column=2)
atk_scale = Entry(param,width=20,validate="key",validatecommand=check_num)
atk_scale.grid(row=4,column=2)

def_base = Entry(param,width=20,validate="key",validatecommand=check_num2)
def_base.grid(row=2,column=3)
def_scale = Entry(param,width=20,validate="key",validatecommand=check_num)
def_scale.grid(row=4,column=3)

agi_base = Entry(param,width=20,validate="key",validatecommand=check_num2)
agi_base.grid(row=2,column=4)
agi_scale = Entry(param,width=20,validate="key",validatecommand=check_num)
agi_scale.grid(row=4,column=4)

lbl_warn = Label(param,text="")
lbl_warn.grid(row=7,columnspan=5)

btn_graph = Button(param,text="Create Graph",command=draw_graph)
btn_graph.grid(row=5,columnspan=5)
btn_calc = Button(param,text="Save as CSV",command=calculate)
btn_calc.grid(row=6,columnspan=5)

param.mainloop()

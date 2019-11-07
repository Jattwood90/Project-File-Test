from tkinter import *


def close_window():
    root.destroy()

#Size of pop up window

root = Tk()
#root.geometry("400x500+0+0")
#title
root.title("Standard Calculator")

#frame for input
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.insert(0,"")

#buttons functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def screen_clear():
    e.delete(0, END)

#math functions

def button_add():
    first_number = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first_number)
    e.delete(0, END)

def equal_fun():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0,first_num + int(second_number))

    if math == "subtraction":
        e.insert(0,first_num - int(second_number))

    if math == "multiplication":
        e.insert(0, first_num * int(second_number))

    if math == "division":
        e.insert(0, first_num / int(second_number))

def subtract():
    first_number = e.get()
    global first_num
    global math
    math = "subtraction"
    first_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(first_number)
    e.delete(0, END)

def division():
    first_number = e.get()
    global first_num
    global math
    math = "division"
    first_num = int(first_number)
    e.delete(0, END)


#button sizes and specifications

button_1 = Button(root, text="1", padx=20,pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20,pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20,pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20,pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20,pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20,pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20,pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20,pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20,pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20,pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=20,pady=20, command=button_add)
button_clear = Button(root, text="C", padx=20,pady=20, command=screen_clear)
button_equal = Button(root, text="=", padx=20,pady=20, command= equal_fun)
button_sub = Button(root, text="-", padx=21,pady=20, command= subtract)
button_div = Button(root, text="/", padx=21,pady=20, command= division)
button_mult = Button(root, text="*", padx=21,pady=20, command= multiply)


#places the buttons onto display
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_mult.grid(row=4, column=3)
button_div.grid(row=4, column=2)
button_equal.grid(row=4, column=0)


root.mainloop()
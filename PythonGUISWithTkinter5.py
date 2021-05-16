from tkinter import *

root = Tk()
root.title("Basic Calculator")

buttonPadX = 40
buttonPadY = 20
buttonWidth = 4
buttonHeight = 1
memory = 0
operation = ""

myEntry = Entry(root)
myEntry.grid(row=0, column=0, columnspan=4)

#To pass a parameter into a function you use the lambda function on button click
def button_click(number):
    #myEntry.delete(0, END)
    memory = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0,memory + str(number))

def button_clear():
    myEntry.delete(0, END)

def button_add():
    global memory, operation
    memory = myEntry.get()
    operation = "+"
    myEntry.delete(0,END)
    #myEntry.insert(0, "+")

def button_subtract():
    global memory, operation
    operation = "-"
    memory = myEntry.get()
    myEntry.delete(0,END)
    #myEntry.insert(0, "+")

def button_multiply():
    global memory, operation
    operation = "*"
    memory = myEntry.get()
    myEntry.delete(0,END)
    #myEntry.insert(0, "+")

def button_divide():
    global memory, operation
    operation = "/"
    memory = myEntry.get()
    myEntry.delete(0,END)
    #myEntry.insert(0, "+")

def button_equal():
    global memory, operation
    if operation == "+":
        output = int(memory) + int(myEntry.get())
    elif operation == "-":
        output = int(memory) - int(myEntry.get())
    elif operation == "*":
        output = int(memory) * int(myEntry.get())
    else:
        output = int(memory) / int(myEntry.get())
    button_clear()
    myEntry.insert(0,output)


#Define each of the buttons for the calculator
myButton_0 = Button(root, text="0", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(0))
myButton_1 = Button(root, text="1", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(1))
myButton_2 = Button(root, text="2", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(2))
myButton_3 = Button(root, text="3", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(3))
myButton_4 = Button(root, text="4", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(4))
myButton_5 = Button(root, text="5", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(5))
myButton_6 = Button(root, text="6", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(6))
myButton_7 = Button(root, text="7", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(7))
myButton_8 = Button(root, text="8", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(8))
myButton_9 = Button(root, text="9", padx=buttonPadX, pady=buttonPadY, command=lambda: button_click(9))
myButton_add = Button(root, text="+", padx=buttonPadX, pady=buttonPadY, command=button_add)
myButton_subtract = Button(root, text="-", padx=buttonPadX, pady=buttonPadY, command=button_subtract)
myButton_multiply = Button(root, text="x", padx=buttonPadX, pady=buttonPadY, command=button_multiply)
myButton_divide = Button(root, text="/", padx=buttonPadX, pady=buttonPadY, command=button_divide)
myButton_equal = Button(root, text="=", padx=buttonPadX, pady=buttonPadY, command=button_equal)
myButton_clear = Button(root, text="Clr", padx=buttonPadX, pady=buttonPadY, command=button_clear)

#Put the buttons on the calculator window
myButton_clear.grid(row=1,column=0)
myButton_divide.grid(row=1, column=3)

myButton_7.grid(row=2, column=0)
myButton_8.grid(row=2, column=1)
myButton_9.grid(row=2, column=2)
myButton_multiply.grid(row=2, column=3)

myButton_4.grid(row=3, column=0)
myButton_5.grid(row=3, column=1)
myButton_6.grid(row=3, column=2)
myButton_subtract.grid(row=3, column=3)

myButton_1.grid(row=4, column=0)
myButton_2.grid(row=4, column=1)
myButton_3.grid(row=4, column=2)
myButton_add.grid(row=4,column=3)

myButton_0.grid(columnspan=2, row=5, column=0)
myButton_equal.grid(row=5,column=3)

root.mainloop()

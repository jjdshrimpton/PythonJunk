from tkinter import *

root = Tk()
clickCount = 0

def myClick():
    global clickCount
    clickCount += 1
    myLabel = Label(root, text="Click count: "+str(clickCount)+"!", fg="white", bg="blue")
    myLabel.pack()

myButton = Button(root, text="Test", pady=50, command=myClick)

myButton.pack()

root.mainloop()
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text=myEntry.get(), fg="white", bg="blue")
    myLabel.pack()


myEntry = Entry(root, width=50, border=10)
myButton = Button(root, text="Test", pady=50, command=myClick)

myEntry.pack()
myButton.pack()

myEntry.insert(0, "Enter your message here")

root.mainloop()
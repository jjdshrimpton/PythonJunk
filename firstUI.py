from tkinter import *

window = Tk()
window.title("Label Example")

label = Label(window, text="Hello World!")
btn_end = Button(window, text="Close", command=exit)

label.pack(padx=200, pady=50)
btn_end.pack(padx=150, pady=20)

window.mainloop()
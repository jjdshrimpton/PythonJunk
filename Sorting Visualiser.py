from tkinter import *
from random import randint
from time import sleep

root = Tk()
root.title("Sorting Algorithms Visualiser")

def go():
    data = []
    quantity = int(myEntryQuantity.get())
    for i in range(quantity):
        data.append(randint(int(myEntryRangeMin.get()),int(myEntryRangeMax.get())))
    
    bubble_sort(data)

def bubble_sort(data):
    iterations = 1
    sorted = False
    while sorted == False:
        changeMade = False
        #log to the screen the current state of the data array 
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(data)+"\n")
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                buffer = data[i]
                data[i] = data[i+1]
                data[i+1] = buffer
                changeMade = True
        iterations += 1
        plot_boxes(data)
        sleep(1)
        if changeMade == False:
            sorted = True

def plot_boxes(data):
    myCanvas.delete("all")
    quantity = len(data)
    rectangleWidth = 800/quantity

    for i in range(quantity):
        #TLX: i*canvas width/quantity of data items // TLY: canvas height - canvas height/max data value*current data value
        #BRX: i*canvas width/quantity of data items+quantity of data items // BRY: height of canvas
        myCanvas.create_rectangle(i*(800/quantity),400-400/50*data[i],i*(800/quantity)+800/quantity,400, fill="red")
        myCanvas.update()
    

myCanvas = Canvas(root, width=800, height=400)
myLabelQuantity = Label(root, text="Quantity of data points to sort:")
myEntryQuantity = Entry(root)
myLabelRangeMin = Label(root, text="Minimum value:")
myEntryRangeMin = Entry(root)
myLabelRangeMax = Label(root, text="Maximum value:")
myEntryRangeMax = Entry(root)
myButton = Button(root, text="Go!", command=go)
myText = Text(root, height=6)

myEntryQuantity.insert(0,"10")
myEntryRangeMin.insert(0,"0")
myEntryRangeMax.insert(0,"25")

myCanvas.grid(row=0, columnspan=7)
myLabelQuantity.grid(row=1,column=0)
myEntryQuantity.grid(row=1,column=1)
myLabelRangeMin.grid(row=2,column=0)
myEntryRangeMin.grid(row=2,column=1)
myLabelRangeMax.grid(row=3,column=0)
myEntryRangeMax.grid(row=3,column=1)
myText.grid(rowspan=3, row=1, column=2)
myButton.grid(row=4, columnspan=3)

root.mainloop()
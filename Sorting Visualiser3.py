import math
from tkinter import *
from random import randint, shuffle, sample
from time import sleep

root = Tk()
root.title("Sorting Algorithms Visualiser")
sortType = StringVar()
menuText = StringVar()
colourOptions = ["Red", "Green", "Blue", "Monochrome", "Random"]
sortingOptions = ["Bubble Sort", "Cocktail Shaker Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Bogo Sort"]

#Initialises the necessary functions based on entered parameters into the form.
def go():
    global sortType
    myText.delete("1.0",END)

    #Creates a random set of data based on selected parameters.
    data = []
    quantity = int(myScaleQuantity.get())
    rangeMax = int(myScaleRangeMax.get())
    for i in range(quantity):
        data.append(randint(0,rangeMax))
    
    #Runs the appropriate function based on which radio button for types of sort has been selected
    if sortType.get() == "Bubble Sort":
        bubble_sort(data,rangeMax)
    elif sortType.get() == "Cocktail Shaker Sort":
        cocktail_shaker_sort(data,rangeMax)
    elif sortType.get() == "Insertion Sort":
        insertion_sort(data,rangeMax)
    elif sortType.get() == "Merge Sort":
        merge_sort(data, rangeMax)
    elif sortType.get() == "Quick Sort":
        quick_sort(data, rangeMax)
    else:
        bogo_sort(data,rangeMax)

#Takes in a value and a max value and returns a hex colour code of corresponding intensity. e.g. 23/100 = 23% brightness on RGB.
def get_colour(value,rangeMax):
    global menuText
    activeColour = menuText.get()
    hexIntensity = str(hex(int(math.floor(float(value)/float(rangeMax)*255)))[2:])
    while len(hexIntensity) < 2:
        hexIntensity = "0" + hexIntensity
    if activeColour == "Red":
        return "#" + hexIntensity + "0000"
    elif activeColour == "Green":
        return "#00" + hexIntensity + "00"
    elif activeColour == "Blue":
        return "#0000" + hexIntensity
    elif activeColour == "Monochrome":
        return "#" + hexIntensity + hexIntensity + hexIntensity
    else:
        return "#" + "".join(sample("0123456789ABCDEF",6))

#Bubble sort function, takes in a set of data and the maximum value this data can be (used for some calculations regarding geometry)
def bubble_sort(data,rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100
    sorted = False
    while sorted == False:
        changeMade = False
        #log to the screen the current state of the data array 
        myText.delete("1.0",END)
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(data)+"\n")
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                buffer = data[i]
                data[i] = data[i+1]
                data[i+1] = buffer
                changeMade = True
                iterations += 1
        plot_boxes(data,rangeMax)
        sleep(speed)
        if changeMade == False:
            sorted = True
        
        myText.delete("1.0",END)
        myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: n^2\nAverage complexity: n^2\nBest complexity: n\nSpace complexity: 1\n\n"+str(data))

#Bubble sort function, takes in a set of data and the maximum value this data can be (used for some calculations regarding geometry)
def cocktail_shaker_sort(data,rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100
    sorted = False
    while sorted == False:
        changeMade = False
        #log to the screen the current state of the data array 
        myText.delete("1.0",END)
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(data)+"\n")
        #first parse over data
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                buffer = data[i]
                data[i] = data[i+1]
                data[i+1] = buffer
                changeMade = True
                iterations += 1
        plot_boxes(data,rangeMax)
        sleep(speed)
        myText.delete("1.0",END)
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(data)+"\n")

        #return parse over data
        for i in range(len(data)-1,0,-1):
            if data[i] < data[i-1]:
                buffer = data[i]
                data[i] = data[i-1]
                data[i-1] = buffer
                changeMade = True
                iterations += 1
        plot_boxes(data,rangeMax)
        sleep(speed)
        if changeMade == False:
            sorted = True
        
        myText.delete("1.0",END)
        myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: n^2\nAverage complexity: n^2\nBest complexity: n\nSpace complexity: 1\n\n" + str(data))

#Insertion sort function, takes in a set of data and the maximum value this data can be (used for some calculations regarding geometry)
def insertion_sort(data, rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100

    sortedData = []
    sortedData.insert(0,data.pop())

    while len(data) > 1:
        sortedData.insert(0,data.pop())
        currentIndex = 0
        while currentIndex < len(sortedData)-1:
            if sortedData[currentIndex] > sortedData[currentIndex + 1]:
                buffer = sortedData[currentIndex]
                sortedData[currentIndex] = sortedData[currentIndex+1]
                sortedData[currentIndex+1] = buffer
            else:
                currentIndex = len(sortedData)-1
            currentIndex += 1
            iterations += 1
        
        myText.delete("1.0",END)
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(sortedData+data)+"\n")
        
        plot_boxes(sortedData+data, rangeMax)
        sleep(speed)
    
    myText.delete("1.0",END)
    myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: n^2\nAverage complexity: n^2\nBest complexity: n\nSpace complexity: 1\n\n" + str(sortedData+data))

def merge_sort(data, rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100

    myText.delete("1.0",END)
    #myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: n*log(n)\nAverage complexity: n*log(n)\nBest complexity: n*log(n)\nSpace complexity: n\n\n" + str(data))
    myText.insert(END, "This sorting algorithm is currently not supported.")

def quick_sort(data, rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100

    myText.delete("1.0",END)
    #myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: n^2\nAverage complexity: n*log(n)\nBest complexity: n*log(n)\n\n" + str(data))
    myText.insert(END, "This sorting algorithm is currently not supported.")


#Randomly re-orders the numbers over and over until they are placed in order by chance.
def bogo_sort(data,rangeMax):
    iterations = 1
    #This simply inverts the speed selection (e.g. speed 100 leads to a sleep of 0, speed 1 leads to a sleep of 1 second, speed 50 leads to a sleep of 0.5 second)
    speed = (100-myScaleSpeed.get()) / 100
    sorted = False
    while sorted == False:
        plot_boxes(data,rangeMax)
        changeNeeded = False
        #log to the screen the current state of the data array 
        myText.delete("1.0",END)
        myText.insert(END,"Iteration " + str(iterations) + ": " + str(data)+"\n")

        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                changeNeeded = True

        if changeNeeded == False:
            sorted = True

        else:        
            iterations += 1
            sleep(speed)
            shuffle(data)
    
        myText.delete("1.0",END)
        myText.insert(END, "Sort completed after " + str(iterations) + " iterations.\n\nBIG O DATA\nWorst complexity: Infinite\nAverage complexity: n*n!\nBest complexity: n\nSpace complexity: 1\n\n" + str(data))

#Takes in a list of numbers as well as the maximum value each number can be. Plots these as points on the canvas relative to the parameters selected on the form.
def plot_boxes(data,rangeMax):
    myCanvas.delete("all")
    quantity = len(data)
    rectangleWidth = 800/quantity

    for i in range(quantity):
        #TLX: i*canvas width/quantity of data items // TLY: canvas height - canvas height/max data value*current data value
        #BRX: i*canvas width/quantity of data items+quantity of data items // BRY: height of canvas
        myCanvas.create_rectangle(i*rectangleWidth,400-400/rangeMax*data[i],i*rectangleWidth+rectangleWidth,400, width=0, fill=get_colour(data[i],rangeMax))
    myCanvas.update()
    
#Declaration of form objects
myCanvas = Canvas(root, width=800, height=400)
myLabelQuantity = Label(root, text="Data points:")
myScaleQuantity = Scale(root, from_=3, to=1000, orient=HORIZONTAL)
myLabelRangeMax = Label(root, text="Max value:")
myScaleRangeMax = Scale(root, from_=5, to=100, orient=HORIZONTAL)
myLabelSpeed = Label(root, text="Speed:")
myScaleSpeed = Scale(root, from_=0, to=100, orient=HORIZONTAL)
myButton = Button(root, text="Go!", command=go)
myDropdownSortType = OptionMenu(root , sortType, *sortingOptions)
myDropdownColours = OptionMenu(root , menuText, *colourOptions)
myText = Text(root, height=8)

#Default values set to form objects
sortType.set("Bubble Sort")
menuText.set("Red")
myScaleQuantity.set(25)
myScaleRangeMax.set(100)
myScaleSpeed.set(50)

#Form object 'packing' and layout.
myCanvas.grid(row=0, columnspan=4)
myDropdownSortType.grid(row=1, column=0)
myDropdownColours.grid(row=1, column=1)
myText.grid(rowspan=3, row=1, column=2)
myLabelQuantity.grid(row=2,column=0)
myScaleQuantity.grid(row=2,column=1)
myLabelRangeMax.grid(row=3,column=0)
myScaleRangeMax.grid(row=3,column=1)
myLabelSpeed.grid(row=4,column=0)
myScaleSpeed.grid(row=4,column=1)
myButton.grid(row=4, column=2, columnspan=2, pady=10)

root.mainloop()
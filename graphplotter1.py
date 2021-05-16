from tkinter import *

root = Tk()
root.title("Graph Plotter")

def button_click():
    parse_equation(myEntry.get())

def plot_line(startX,startY,endX,endY):
    myCanvas.create_line(startX,startY,endX,endY, fill="#FF0000")

def parse_equation(equationText):
    #y=5/x=0/x=1/y=7

    equationText = equationText.replace(" ","")
    equationText = equationText.lower()
    intercept = int(equationText[2:])

    if equationText[0] == "x":
        startX=math_to_canvas_coordinates(intercept)
        startY=math_to_canvas_coordinates(-10)
        endX=math_to_canvas_coordinates(intercept)
        endY=math_to_canvas_coordinates(10)
    else:
        startX=math_to_canvas_coordinates(-10)
        startY=math_to_canvas_coordinates(intercept)
        endX=math_to_canvas_coordinates(10)
        endY=math_to_canvas_coordinates(intercept)

    plot_line(startX,startY,endX,endY)

    myLabel.configure(text=equationText + " plotted on graph.")

#Converts the cartesian coordinates into canvas/pixel coordinates
#e.g. 5,3 becomes 150,130 e.g. -5,-3 becomes 50,30
#e.g. 0,-5 becomes 100,50 e.g. 0,9 becomes 100,190
def math_to_canvas_coordinates(mathcoordinate):
    return mathcoordinate * 10 + 100

myEntry = Entry(root)
myCanvas = Canvas(root)
myButton = Button(root, text="Go!", command=button_click)
myLabel = Label(root)

myEntry.grid(row=0, column=0)
myButton.grid(row=0, column=1)
myCanvas.grid(row=1, columnspan=2, padx=50, pady=50)
myLabel.grid(row=2,columnspan=2)

myCanvas.create_line(0,100, 200,100, fill="#000000")
myCanvas.create_line(100,0, 100,200, fill="#000000")

#0,0 IS THE TOP LEFT OF THE CANVAS WIDGET, 200,200 IS THE BOTTOM RIGHT
myCanvas.create_line(0,0, 10,10, fill="#ffffff")


for i in range(-10,10, 2):
    #label x axis
    myCanvas.create_text(math_to_canvas_coordinates(i),math_to_canvas_coordinates(0),text=str(i), font="Consolas 10")
    #label y axis
    myCanvas.create_text(math_to_canvas_coordinates(0),math_to_canvas_coordinates(i),text=str(i), font="Consolas 10")

root.mainloop()
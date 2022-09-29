import tkinter as tk
from tkinter import *
from random import *
from turtle import fillcolor
from PIL import Image, ImageTk, ImageDraw
""" 
def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

root = tk.Tk()
root.geometry('1000x1000')

bgimg = Image.open('rsz_mappagrande.jpg') # load the background image
wid = bgimg.width
hei = bgimg.height
tot = str(wid)+"x"+str(hei)

l = tk.Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

root.mainloop() """

""" window = Tk()
window.title('Game Of Life')
def create_grid(window):
    width = 800
    height = 600
    canvas = Canvas(window, background='white', width=width, height=height)
    image = ImageTk.PhotoImage(file = "rsz_mappagrande.jpg")
    canvas.create_image(10, 10, image = image, anchor = NW)

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)

create_grid(window)
window.mainloop() """

""" import tkinter
from tkinter import *
from PIL import Image, ImageTk

class Cell():
    FILLED_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, master, x, y, size):
        #Constructor of the object called by Cell(...) 
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False

    def _switch(self):
        #Switch if the cell is filled or not.
        self.fill= not self.fill

    def draw(self):
        #order to the cell to draw its representation on the canvas
        if self.master != None :
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER
            
            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)

class CellGrid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize
        
        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()



    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        print("(w pos"+str(row)+"_"+str(column)+")")
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        #add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)


if __name__ == "__main__" :
    app = Tk()
# Create a photoimage object of the image in the path
    
    image = Image.open("rsz_mappagrande.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    
    label.image = photo # keep a reference!
    
    grid = CellGrid(app, 30, 30, 20)
    grid.pack()
    app.mainloop() """



import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Position text in frame
Label(root, text = 'Position image on button', font =('<font_name>', <font_size>)).pack(side = TOP, padx = <x_coordinate#>, pady = <y_coordinate#>)

# Create a photoimage object of the image in the path
photo = PhotoImage(file = "</path/image_name>")

# Resize image to fit on button
photoimage = photo.subsample(1, 2)

# Position image on button
Button(root, image = photoimage,).pack(side = BOTTOM, pady = <y_coordinate#>)
mainloop()
from tkinter import *
import time
import threading



class Pacman:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 35, 35, fill = color)
        self.canvas.move(self.id, 400, 350)
        self.x = 0
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.go_up)
        self.canvas.bind_all('<KeyPress-Down>', self.go_down)

    def turn_left(self, evt):
        self.x = -5

    def turn_right(self, evt):
        self.x = 5

    def go_up(self, evt):
        self.y = -5

    def go_down(self, evt):
        self.y = 5

    def draw(self):
        #self.canvas.delete('all')
        #root.update()
        self.canvas.move(self.id, self.x, self.y)
        

class Maze:
    def __init__(self, canvas):
        self.canvas = canvas

    def drawSquareWall(self, x0, y0, x1, y1, width = 2, color = '#4169e1'):
        canvas.create_rectangle(x0, y0, x1, y1, fill = color)
        canvas.create_line(x0, y0, x1, y0, width = width, fill = 'yellow')
        canvas.create_line(x1, y0, x1, y1, width = width, fill = 'yellow')
        canvas.create_line(x1, y1, x0, y1, width = width, fill = 'yellow')
        canvas.create_line(x0, y1, x0, y0, width = width, fill = 'yellow')

    def drawWall(self, x0, y0, x1, y1, width = 3, color = 'blue'):
        canvas.create_line(x0, y0, x1, y1, width = width, fill = color)

    def BuildGhostBase(self):
        for wall in BaseOfGhost:
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])
        canvas.create_line(350, 270, 450, 270, width = 5, fill = 'yellow')

    def BuildRectangleWalls(self):
        for wall in outerWall: 
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])

    def BuildOuterWall(self):
        for wall in outerWall: 
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])

    def draw(self):
        self.BuildOuterWall()
        self.BuildGhostBase()
        self.BuildRectangleWalls


outerWall = [ [5, 5, 5, 200], [5, 5, 400, 5], [20, 20, 20, 200],
                [20, 20, 385, 20], [5, 200, 5, 215], [20, 200, 150, 200], 
                [5, 215, 135, 215], [135, 215, 135, 275],
                [150, 200, 150, 290], [135, 215, 135, 275], [150, 290, 5, 290]
                , [135, 275, 5, 275], [5, 350, 150, 350], [5, 365, 135, 365],
                [150, 350, 150, 440] , [135, 365, 135, 425], [150, 440, 20, 440], [135, 425, 5, 425], [5, 425, 5, 695], [20, 440, 20, 545], [20, 575, 20, 680], [20, 545, 60, 545], [20, 575, 60, 575], [60, 545, 60, 575], [5, 695, 795, 695], [385, 20, 385, 110], [385, 110, 400, 110], [20, 680, 780, 680]
                    ]

squareWalls = [[60, 60, 150, 90], [190, 60, 345, 90], [60, 130, 150, 150]]



BaseOfGhost = [[300, 270, 300, 370], [310, 280, 310, 360], [300, 270, 350, 270], [300, 370, 400, 370], [310, 360, 400, 360], [310, 280, 350, 280],[350, 280, 350, 270] ]

root = Tk()
root.title("Pacman")
canvas = Canvas (width = 800, height = 700, bg = 'black')
canvas.pack()
pcMaze = Maze(canvas)
pacman = Pacman(canvas, 'yellow')


#root.update_idletasks()
#root.update()
#time.sleep(0.0000000001)

root.after(20, pacman.draw())
root.after(20, pcMaze.draw())
root.mainloop()
from tkinter import *
import time
import threading

class Game:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pac-man")
        self.canvas = Canvas(self.tk, width = 800, height = 700, bg = 'black')
        for wall in outerWall: 
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])

        for wall in WierdWalls: 
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])

        for wall in BaseOfGhost:
            self.drawWall(wall[0], wall[1], wall[2], wall[3])
            self.drawWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])
        self.canvas.create_line(350, 270, 450, 270, width = 5, fill = 'yellow')

        for wall in squareWalls: 
            self.drawSquareWall(wall[0], wall[1], wall[2], wall[3])
            self.drawSquareWall(800 - wall[0], wall[1], 800 - wall[2], wall[3])

        self.canvas.pack()
        self.tk.update
        self.running = True

    def drawWall(self, x0, y0, x1, y1, width = 3, color = 'blue'):
        self.canvas.create_line(x0, y0, x1, y1, width = width, fill = color)

    def drawSquareWall(self, x0, y0, x1, y1, width = 2, color = '#4169e1'):
        self.canvas.create_rectangle(x0, y0, x1, y1, fill = color)
        self.canvas.create_line(x0, y0, x1, y0, width = width, fill = 'yellow')
        self.canvas.create_line(x1, y0, x1, y1, width = width, fill = 'yellow')
        self.canvas.create_line(x1, y1, x0, y1, width = width, fill = 'yellow')
        self.canvas.create_line(x0, y1, x0, y0, width = width, fill = 'yellow')

    def mainloop(self):
        while 1:
            if self.running:
                pass #ghosts moving
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

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
        
outerWall = [ [5, 5, 5, 200], [5, 5, 400, 5], [20, 20, 20, 200],
                [20, 20, 385, 20], [5, 200, 5, 215], [20, 200, 150, 200], 
                [5, 215, 135, 215], [135, 215, 135, 275],
                [150, 200, 150, 290], [135, 215, 135, 275], [150, 290, 5, 290]
                , [135, 275, 5, 275], [5, 350, 150, 350], [5, 365, 135, 365],
                [150, 350, 150, 440] , [135, 365, 135, 425], [150, 440, 20, 440], [135, 425, 5, 425], [5, 425, 5, 695], [20, 440, 20, 545], [20, 575, 20, 680], [20, 545, 60, 545], [20, 575, 60, 575], [60, 545, 60, 575], [5, 695, 795, 695], [385, 20, 385, 90], [385, 90, 400, 90], [20, 680, 780, 680]
                    ]

squareWalls = [[60, 60, 140, 90], [200, 60, 340, 90], [60, 130, 140, 150], [200, 350, 240, 440], [200, 490, 340, 510]]

BaseOfGhost = [[300, 270, 300, 370], [310, 280, 310, 360], [300, 270, 350, 270], [300, 370, 400, 370], [310, 360, 400, 360], [310, 280, 350, 280],[350, 280, 350, 270] ]

WierdWalls = [[300, 140, 500, 140], [500, 140, 500, 160], [500, 160, 410, 160],
                [300, 140, 300, 160], [300, 160, 390, 160], [390, 160, 390, 220], [410, 160, 410, 220], [390, 220, 410, 220], [560, 140, 560, 200], [600, 140, 600, 290], [560, 200, 480, 200], [480, 200, 480, 220], [480, 220, 560, 220], [560, 220, 560, 290], [560, 290, 600, 290], [560, 140, 600, 140], [150, 480, 150, 575], [150, 480, 60, 480], [60, 480, 60, 500], [60, 500, 130, 500], [130, 500, 130, 575], [130, 575, 150, 575],
                    [300, 440, 390, 440 ], [300, 440, 300, 420], [300, 420, 500, 420], [390, 440, 390, 510], [390, 510, 410, 510],
                    [300, 580, 390, 580 ], [300, 580, 300, 550], [300, 550, 500, 550], [390, 580, 390, 640], [390, 640, 410, 640], [60, 640, 340, 640], [60, 640, 60, 620], [60, 620, 200, 620], [200, 620, 200, 550], [200, 550, 220, 550,],
                    [220, 550, 220, 620], [220, 620, 340, 620], [340, 620, 340, 640] ] 

g = Game()
g.mainloop()
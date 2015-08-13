from tkinter import *
import time
import threading

points = []

matrix = []



class Game:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pac-man")
        self.canvas = Canvas(self.tk, width = 800, height = 700, bg = 'black')
        self.Pac = Pacman(self.canvas, 'yellow')
        '''i = 0 
        while i <= 800:
            j = 0
            while j <= 800:
                matrix.append ([j, i, j + 30, i + 30])
                j = j + 30
            i += 30

        #self.drawSquareWall(110, 110, 180, 180)

        for square in matrix:
            self.drawSquareWall(square[0], square[1], square[2], square[3])'''
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

        for key in graph:
            self.canvas.create_oval(key[0], key[1], key[0] + 10, key[1] + 10, fill = 'green')

        self.drawPoints()
        self.Pac.draw()
        self.canvas.pack()
        self.tk.update
        self.running = True

    def drawWall(self, x0, y0, x1, y1, width = 3, color = 'blue'):
        self.canvas.create_line(x0, y0, x1, y1, width = width, fill = color)

    def drawSquareWall(self, x0, y0, x1, y1, width = 2, color = 'black'):
        self.canvas.create_rectangle(x0, y0, x1, y1, fill = color)
        self.canvas.create_line(x0, y0, x1, y0, width = width, fill = 'blue')
        self.canvas.create_line(x1, y0, x1, y1, width = width, fill = 'blue')
        self.canvas.create_line(x1, y1, x0, y1, width = width, fill = 'blue')
        self.canvas.create_line(x0, y1, x0, y0, width = width, fill = 'blue')

    def drawPoints(self):
        self.BuildHorizontalPath(40, 40, 13, 26)
        self.BuildVerticalPath(40, 40, 9, 16)
        self.BuildHorizontalPath(66, 168, 4, 26)
        self.BuildHorizontalPath(66, 104, 4, 26)
        self.BuildVerticalPath(170, 56, 8, 16)
        self.BuildVerticalPath(170, 192, 18, 24)
        self.BuildHorizontalPath(196, 104, 8, 26)
        self.BuildVerticalPath(352, 56, 3, 16)
        self.BuildHorizontalPath(40, 456, 5, 26)
        self.BuildHorizontalPath(40, 600, 5, 26)
        self.BuildVerticalPath(40, 472, 4, 16)
        self.BuildHorizontalPath(66, 520, 2, 26)
        self.BuildVerticalPath(92, 536, 4, 16 )
        self.BuildVerticalPath(40, 600, 4, 18)
        self.BuildHorizontalPath(66, 654, 12, 27)
        self.BuildHorizontalPath(200, 527, 7, 27)
        self.BuildHorizontalPath(200, 456, 7, 27)
        self.BuildVerticalPath (362, 472, 3, 18)

    def BuildHorizontalPath(self, val1, val2, number, increment = 25, delta = 8):
        x, y = val1, val2
        for i in range(number):
            deltax = x + delta
            deltay = y + delta
            self.canvas.create_oval(x, y, deltax, deltay, fill = 'white')
            self.canvas.create_oval(800-x, y, 800-deltax, deltay, fill = 'white')
            x += increment
            points.append([x, y])

    def BuildVerticalPath(self, val1, val2, number, increment = 30, delta = 8):
        for i in range(number):
            x, y = val1, val2
            deltax = x + delta
            deltay = y + delta
            self.canvas.create_oval(x, y, deltax, deltay, fill = 'white')
            self.canvas.create_oval(800-x, y, 800-deltax, deltay, fill = 'white')
            val2 += increment
            points.append([x, y])

    def mainloop(self):
        while 1:
            if self.running:
                self.Pac.canvas.move(self.Pac.id, self.Pac.x, self.Pac.y)
                if self.Pac.hitwall():
                    self.Pac.stop()
                    time.sleep()
                if self.Pac.eaten:
                    self.canvas.grid()
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
        self.canvas.bind_all('<KeyRelease>', self.stop)

    def eaten(self):
        for point in points:
            if self.x == point[0] and self.y == point[1]:
                return True
        return False

    def stop(self, event):
        self.x = 0
        self.y = 0

    def turn_left(self, event):
        self.x = -2
        
        #print("Huy")

    def turn_right(self, event):
        self.x = 2
        

    def go_up(self, event):
        self.y = -2

    def go_down(self, event):
        self.y = 2

    def draw(self):
        #self.canvas.delete('all')
        #root.update()
        self.canvas.move(self.id, self.x, self.y)
        if self.hitwall():
            self.stop()

    def hitwall(self):
        for wall in outerWall:
            if self.x >= wall[0] and self.x <= wall[2] and self.y >= wall[1] and self.y >=wall[3]:
                return True
        return False
        
outerWall = [ [5, 5, 5, 200], [5, 5, 400, 5], [20, 20, 20, 200],
                [20, 20, 385, 20], [5, 200, 5, 215], [20, 200, 150, 200], 
                [5, 215, 135, 215], [135, 215, 135, 275],
                [150, 200, 150, 290], [135, 215, 135, 275], [150, 290, 5, 290]
                , [135, 275, 5, 275], [5, 350, 150, 350], [5, 365, 135, 365],
                [150, 350, 150, 440] , [135, 365, 135, 425], [150, 440, 20, 440], [135, 425, 5, 425], [5, 425, 5, 695], [20, 440, 20, 545], [20, 575, 20, 680], [20, 545, 60, 545], [20, 575, 60, 575], [60, 545, 60, 575], [5, 695, 795, 695], [385, 20, 385, 90], [385, 90, 400, 90], [20, 680, 780, 680]
                    ]

squareWalls = [[60, 60, 150, 90], [200, 60, 340, 90], [60, 130, 150, 150], [200, 350, 240, 440], [200, 490, 340, 510]]

BaseOfGhost = [[300, 270, 300, 370], [310, 280, 310, 360], [300, 270, 350, 270], [300, 370, 400, 370], [310, 360, 400, 360], [310, 280, 350, 280],[350, 280, 350, 270] ]

WierdWalls = [[300, 140, 500, 140], [500, 140, 500, 160], [500, 160, 410, 160],
                [300, 140, 300, 160], [300, 160, 390, 160], [390, 160, 390, 220], [410, 160, 410, 220], [390, 220, 410, 220], [560, 140, 560, 200], [600, 140, 600, 290], [560, 200, 480, 200], [480, 200, 480, 220], [480, 220, 560, 220], [560, 220, 560, 290], [560, 290, 600, 290], [560, 140, 600, 140], [150, 480, 150, 575], [150, 480, 60, 480], [60, 480, 60, 500], [60, 500, 130, 500], [130, 500, 130, 575], [130, 575, 150, 575],
                    [300, 440, 390, 440 ], [300, 440, 300, 420], [300, 420, 500, 420], [390, 440, 390, 510], [390, 510, 410, 510],
                    [300, 580, 390, 580 ], [300, 580, 300, 550], [300, 550, 500, 550], [390, 580, 390, 640], [390, 640, 410, 640], [60, 640, 340, 640], [60, 640, 60, 620], [60, 620, 200, 620], [200, 620, 200, 550], [200, 550, 220, 550,],
                    [220, 550, 220, 620], [220, 620, 340, 620], [340, 620, 340, 640] ] 


graph = {(40,40):[[175, 40], [40, 110]],
         (175, 40):[[175, 110], [40, 40] ],
         (175, 110): [[175, 40], [40, 110]],
         (40, 110):[[40, 40], [175, 110]]
    }   

g = Game()  
g.mainloop()

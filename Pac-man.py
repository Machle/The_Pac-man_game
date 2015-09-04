from tkinter import *
import time
import threading
from threading import Timer
from PIL import Image, ImageTk
import random
from tkinter import messagebox

points = []
matrix = []

class Game:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pac-man")
        self.canvas = Canvas(self.tk, width = 800, height = 700, bg = 'black')
        self.Pac = Pacman(self.canvas, 'yellow')
        self.Blinky = Ghost(self.canvas, 'red', 320, 220, -2, 0)
        self.Pinky = Ghost(self.canvas, 'pink', 360, 280, 0, 2 )
        self.Inky = Ghost(self.canvas, 'blue', 380, 280, 0, 2)
        self.Clyde = Ghost(self.canvas, 'brown', 410, 280, 0, -2)
        self.score = 0
        self.scoreid = Label(self.tk,
                        text = "SCORE: {0}".format(self.score), bg = 'yellow', fg = 'black')
        self.scoreid.pack()
        self.frame = Frame(self.tk)
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

        self.drawPoints()
        self.Pac.draw()
        self.canvas.pack()
        self.running = True
        self.tk.update

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
        self.BuildVerticalPath (274, 135, 3, 20)
        self.BuildHorizontalPath (292, 175, 4, 18)
        self.BuildVerticalPath (254, 550, 3, 20)
        self.BuildHorizontalPath (274, 591, 5, 22)
        self.BuildVerticalPath (363, 611, 2, 20)

    def BuildHorizontalPath(self, val1, val2, number, increment = 25, 
                                    delta = 8):
        x, y = val1, val2
        itemid1 = 0
        itemid2 = 0
        for i in range(number):
            deltax = x + delta
            deltay = y + delta
            itemid1 = self.canvas.create_oval(x, y, deltax, deltay,
                fill = 'white')
            itemid2 = self.canvas.create_oval(800-x, y, 800-deltax, deltay, fill = 'white')
            points.append([(deltax + x)/2, (deltay + y)/2, itemid1])
            points.append([800-(deltax + x)/2, (deltay+y)/2, itemid2])
            x += increment

    def BuildVerticalPath(self, val1, val2, number, increment = 30, delta = 8):
        itemid1 = 0
        itemid2 = 0
        for i in range(number):
            x, y = val1, val2
            deltax = x + delta
            deltay = y + delta
            itemid1 = self.canvas.create_oval(x, y, deltax, deltay,
                                        fill = 'white')
            itemid2 = self.canvas.create_oval(800-x, y, 800-deltax, deltay, 
                                        fill = 'white')
            points.append([(deltax + x)/2, (deltay + y)/2, itemid1])
            points.append([800-(deltax + x)/2, (deltay + y)/2, itemid2])
            val2 += increment

    def spawn_ghost(self):
        if self.score == 200:
            self.Pinky.canvas.move(self.Pinky.id, -345, -255)
        if self.score == 400:
            self.Inky.canvas.move(self.Inky.id, 350, 360)
        if self.score == 800:
            self.Clyde.canvas.move(self.Clyde.id, -300, 360)

    def hit_pac(self, ghost):
        pac_pos = self.Pac.canvas.coords(self.Pac.id)
        pos = ghost.canvas.coords(ghost.id)
        if pos[0] >= pac_pos[0] and pos[0] <= pac_pos[2]:
            if pos[1] >= pac_pos[1] and pos[1] <= pac_pos[3]:
                return True
            elif pos[3] >= pac_pos[1] and pos[3] <= pac_pos[3]:
                return True
        elif pos[2] >= pac_pos[0] and pos[2] <= pac_pos[2]:
            if pos[1] >= pac_pos[1] and pos[1] <= pac_pos[3]:
                return True
            elif pos[3] >= pac_pos[1] and pos[3] <= pac_pos[3]:
                return True
        elif pos[1] >= pac_pos[1] and pos[1] <= pac_pos[3]:
            if pos[0] >= pac_pos[0] and pos[0] <= pac_pos[2]:
                return True
            elif pos[2] >= pac_pos[0] and pos[2] <= pac_pos[2]:
                return True
        elif pos[3] >= pac_pos[1] and pos[3] <= pac_pos[3]:
            if pos[0] >= pac_pos[0] and pos[0] <= pac_pos[2]:
                return True
            elif pos[2] >= pac_pos[0] and pos[2] <= pac_pos[2]:
                return True
        return False

    def game_over(self):
        self.window = Tk()
        self.window.title("Game over")
        image1 = Image.open("/home/tano/The_Pac-man_game/game_over.png")
        photo = ImageTk.PhotoImage(image1)
        label = Label(self.window, text = "Your score: {0}".format(self.score), image = photo)
        label.image = photo
        label.pack()
        button1 = Button(self.window, text = "Play again", 
                            command = self.play_again).pack()
        button2 = Button(self.window, text = "Exit", 
                            command = self.exit).pack()

    def play_again(self):
        new_game = Game()
        self.window.destroy()
        new_game.animate()

    def exit(self):
        self.window.destroy()

    def win(self):
        self.window = Tk()
        self.window.title("You win!")
        label2 = Label(self.window, text = "Congratulations! You've won the game!")
        label2.pack()
        button1 = Button(self.window, text = "Play again", 
                            command = self.play_again).pack()
        button2 = Button(self.window, text = "Exit", 
                            command = self.exit).pack()

    def animate(self):
        if self.running:
            if not self.Pac.hitwall():
                self.Pac.canvas.move(self.Pac.id, self.Pac.x, self.Pac.y)
                if self.Pac.feed():
                    self.score = self.score + 10
                    self.spawn_ghost()
                    self.scoreid.config(text = "SCORE: {0}".format(self.score))
                if self.Pac.first_teleport():
                    self.Pac.canvas.move(self.Pac.id, 760, 0)
                elif self.Pac.second_teleport():
                    self.Pac.canvas.move(self.Pac.id, -760, 0)
            if not self.Blinky.hitwall():
                self.Blinky.canvas.move(self.Blinky.id, self.Blinky.x, self.Blinky.y)
            else:
                self.Blinky.change_direction()
            if self.hit_pac(self.Blinky):
                self.tk.destroy()
                self.game_over()
            if not self.Pinky.hitwall():
                self.Pinky.canvas.move(self.Pinky.id, self.Pinky.x, self.Pinky.y)
            else:
                self.Pinky.change_direction()
            if self.hit_pac(self.Pinky):
                self.tk.destroy()
                self.game_over()
            if not self.Inky.hitwall():
                self.Inky.canvas.move(self.Inky.id, self.Inky.x, self.Inky.y)
            else:
                self.Inky.change_direction()
            if self.hit_pac(self.Inky):
                self.tk.destroy()
                self.game_over()
            if not self.Clyde.hitwall():
                self.Clyde.canvas.move(self.Clyde.id, self.Clyde.x, self.Clyde.y)
            else:
                self.Clyde.change_direction()
            if self.hit_pac(self.Clyde):
                self.tk.destroy()
                self.game_over()
            if not points:
                self.tk.destroy()
                self.win()
            self.frame.after(10, self.animate)

class Pacman:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 35, 35, fill = color)
        self.canvas.move(self.id, 400, 375)
        self.x = 0
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.go_up)
        self.canvas.bind_all('<KeyPress-Down>', self.go_down)
        self.canvas.bind_all('<KeyRelease>', self.stop)

    def feed(self):
        pos = self.canvas.coords(self.id)
        for point in points:
            if  point[0] >= pos[0] and point[0] <= pos[2]:
                if point[1] >= pos[1] and point[1] <= pos[3]:
                    self.canvas.delete(point[2])
                    points.remove(point)
                    return True
            if  point[1] >= pos[1] and point[1] <= pos[3]:
                if point[0] >= pos[0] and point[0] <= pos[2]:
                    self.canvas.delete(point[2])
                    points.remove(point)
                    return True
        return False

    def stop(self, event):
        self.x = 0
        self.y = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2
        
    def go_up(self, event):
        self.y = -2

    def go_down(self, event):
        self.y = 2

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

    def hitwall(self):
        pos = self.canvas.coords(self.id)
        pos[0] += self.x
        pos[1] += self.y
        pos[2] += self.x
        pos[3] += self.y
        for wall in squareWalls:
            if pos[1] in range(wall[1], wall[3]):
                if pos[0] in range(wall[0], wall[2]):
                    return True
                elif pos[2] in range(wall[0], wall[2]):
                    return True
                elif pos[0] >= 800 - wall[2] and pos[0]<= 800 - wall[0]:
                    return True
                elif pos[2] >= 800 - wall[2] and pos[2]<= 800 - wall[0]:
                    return True
            elif pos[3] in range(wall[1], wall[3]):
                if pos[0] in range(wall[0], wall[2]):
                    return True
                elif pos[2] in range(wall[0], wall[2]):
                    return True
                elif pos[0] >= 800 - wall[2] and pos[0]<= 800 - wall[0]:
                    return True
                elif pos[2] >= 800 - wall[2] and pos[2]<= 800 - wall[0]:
                    return True
        for wall in outerWall:
            if pos[1] > 90 and pos[3] < 680:
                if pos[0] <= wall[0] and pos[0] <= wall[2]:
                    if pos[1] in range(wall[1], wall[3]):
                        return True
                    elif pos[3] in range(wall[1], wall[3]):
                        return True
                elif pos[2] <= wall[0] and pos[2] <=wall[2]:
                    if pos[3] in range(wall[1], wall[3]):
                        return True
                    elif pos[1] in range(wall[1], wall[3]):
                        return True
                elif pos[0] >= 800 - wall[0] and pos[0] >= 800 - wall[2]:
                    if pos[1] in range(wall[1], wall[3]):
                        return True
                    elif pos[3] in range(wall[1], wall[3]):
                        return True
                elif pos[2] >= 800 - wall[0] and pos[2] >= 800 - wall[2]:
                    if pos[3] in range(wall[1], wall[3]):
                        return True
                    elif pos[1] in range(wall[1], wall[3]):
                        return True
        if pos[3] > 680 or pos[1] < 20:
            return True
        elif pos[1] > 18 and pos[1] < 90:
            if pos[0] < 20:
                return True
            elif pos[2] > 778:
                return True
            elif pos[2] > 385 and pos[2] < 415:
                return True
            elif pos[0] > 385 and pos[0] < 415:
                return True
        elif pos[2] > 780 and pos[3] > 670:
            return True
        elif pos[2] < 20 and pos[3] > 670:
            return True
        elif pos[2] > 780 and pos[3] < 30:
            return True
        elif pos[2] < 20 and pos[3] < 30:
            return True
        for wall in list_of_walls:
            if pos[1] in range(wall[1], wall[3]):
                if pos[0] in range(wall[0], wall[2]):
                    return True
                elif pos[2] in range(wall[0], wall[2]):
                    return True
                elif pos[0] >= 800 - wall[2] and pos[0]<= 800 - wall[0]:
                    return True
                elif pos[2] >= 800 - wall[2] and pos[2]<= 800 - wall[0]:
                    return True
            elif pos[3] in range(wall[1], wall[3]):
                if pos[0] in range(wall[0], wall[2]):
                    return True
                elif pos[2] in range(wall[0], wall[2]):
                    return True
                elif pos[0] >= 800 - wall[2] and pos[0]<= 800 - wall[0]:
                    return True
                elif pos[2] >= 800 - wall[2] and pos[2]<= 800 - wall[0]:
                    return True
        return False 

    def first_teleport(self):
        pos = self.canvas.coords(self.id)
        if pos[1] > 290 and pos[1] < 350:
            if pos[0] < 0:
                return True
        return False

    def second_teleport(self):
        pos = self.canvas.coords(self.id)
        if pos[3] > 290 and pos[3] < 350:
            if pos[2] > 800:
                return True
        return False
     
class Menu():

    def __init__(self):
        self.m = Tk()
        self.m.title("Pac-man")
        image1 = Image.open("/home/tano/The_Pac-man_game/pacman.jpg")
        photo = ImageTk.PhotoImage(image1)
        label1 = Label(self.m, image = photo)
        label1.image = photo
        label1.pack()
        play_button = Button(self.m, text="Play", command = self.play).pack()
        exit_button = Button(self.m, text="Exit", command = self.exit).pack()

    def play(self):
        self.m.destroy()
        g = Game()
        g.animate()

    def exit(self):
        self.m.destroy()

class Ghost(Pacman):

    def __init__(self, canvas, color, xcoord,  ycoord, incr1, incr2):
        self.canvas = canvas
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.id = canvas.create_oval(10, 10, 35, 35, fill = color)
        self.canvas.move(self.id, xcoord, ycoord)
        self.x = incr1
        self.y = incr2

    def movement(self):
        if self.x > 0:
            self.turn_right
        if self.x < 0:
            self.turn_left
        if self.y > 0:
            self.go_down
        if self.y < 0:
            self.go_up

    def change_direction(self):
        rand = random.randrange(1, 16)
        if rand % 4 == 1:
            self.x = 0
            self.y = 2
        elif rand % 4 == 2:
            self.x = 2
            self.y = 0
        elif rand % 4 == 3:
            self.x = 0
            self.y = -2
        elif rand % 4 == 4:
            self.x = -2
            self.y = 0

    def hit_other_ghost(self, ghost):
        pos = self.canvas.coords(self.id)
        pos_other = ghost.canvas.coords(ghost.id)
        if pos[0] >= pos_other[0] and pos[0] <= pos_other[2]:
            if pos[1] >= pos_other[1] and pos[1] <= pos_other[3]:
                return True
            elif pos[3] >= pos_other[1] and pos[3] <= pos_other[3]:
                return True
        elif pos[2] >= pos_other[0] and pos[2] <= pos_other[2]:
            if pos[1] >= pos_other[1] and pos[1] <= pos_other[3]:
                return True
            elif pos[3] >= pos_other[1] and pos[3] <= pos_other[3]:
                return True
        elif pos[1] >= pos_other[1] and pos[1] <= pos_other[3]:
            if pos[0] >= pos_other[0] and pos[0] <= pos_other[2]:
                return True
            elif pos[2] >= pos_other[0] and pos[2] <= pos_other[2]:
                return True
        elif pos[3] >= pos_other[1] and pos[3] <= pos_other[3]:
            if pos[0] >= pos_other[0] and pos[0] <= pos_other[2]:
                return True
            elif pos[2] >= pos_other[0] and pos[2] <= pos_other[2]:
                return True
        return False
        
outerWall = [ [5, 5, 5, 200], [5, 5, 400, 5], [20, 20, 20, 200],
                [20, 20, 385, 20], [5, 200, 5, 215], [20, 200, 150, 200], 
                [5, 215, 135, 215], [135, 215, 135, 275],
                [150, 200, 150, 290], [135, 215, 135, 275], [5, 290, 150, 290]
                , [5, 275, 135, 275], [5, 350, 150, 350], [5, 365, 135, 365],
                [150, 350, 150, 440] , [135, 365, 135, 425], [20, 440, 150, 440], [5, 425, 135, 425], [5, 425, 5, 695], [20, 440, 20, 545], [20, 575, 20, 680], [20, 545, 60, 545], [20, 575, 60, 575], [60, 545, 60, 575], [5, 695, 795, 695], [385, 20, 385, 90], [385, 90, 400, 90], [20, 680, 780, 680]
                    ]

squareWalls = [[60, 60, 150, 90], [200, 60, 340, 90], [60, 130, 150, 150], [200, 350, 240, 440], [200, 490, 340, 510]]

BaseOfGhost = [[300, 270, 300, 370], [310, 280, 310, 360], [300, 270, 350, 270], [300, 370, 400, 370], [310, 360, 400, 360], [310, 280, 350, 280],[350, 280, 350, 270] ]

WierdWalls = [[300, 140, 500, 140], [500, 140, 500, 160], [500, 160, 410, 160],
                [300, 140, 300, 160], [300, 160, 390, 160], [390, 160, 390, 220], [410, 160, 410, 220], [390, 220, 410 , 220], [560, 140, 560, 200], [600, 140, 600, 290], [560, 200, 480, 200], [480, 200, 480, 220], [480, 220, 560, 220], [560, 220, 560, 290], [560, 290, 600, 290], [560, 140, 600, 140], [150, 480, 150, 575], [150, 480, 60, 480], [60, 480, 60, 500], [60, 500, 130, 500], [130, 500, 130, 575], [130, 575, 150, 575],
                    [300, 440, 390, 440 ], [300, 440, 300, 420], [300, 420, 500, 420], [390, 440, 390, 510], [390, 510, 410, 510],
                    [300, 580, 390, 580 ], [300, 580, 300, 550], [300, 550, 500, 550], [390, 580, 390, 640], [390, 640, 410, 640], [60, 640, 340, 640], [60, 640, 60, 620], [60, 620, 200, 620], [200, 620, 200, 550], [200, 550, 220, 550,],
                    [220, 550, 220, 620], [220, 620, 340, 620], [340, 620, 340, 640] ] 

list_of_walls = [[300,140,500,160],[390,160,410,220], [560,140,600,290],[560,200,480,220], [240,200,320,220],[240,140,200,290],[150,480,130,575], [650,480,670,575], [150,480,60,500], [650,480,740,500], [300,420,500,440], [390,440,410,510], [300,550,500,580], [390,580,410,640], [60,620,340,640], [460,620,740,640], [200,550,220,620], [580,550,600, 620], [300, 270, 400, 370]]

my_menu = Menu()
my_menu.m.mainloop()
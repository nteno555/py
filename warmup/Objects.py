from tkinter import *
import random
import time

WIDTH = 1000
HEIGHT = 900

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Bouncing Ball")
canvas.pack()

class Ball:
    def __init__(self, start_x, start_y, xspeed, yspeed, fill_color):
        self.shape = canvas.create_oval(start_x, start_x, start_y, start_y, fill=fill_color)
        self.xspeed = random.randrange(2, 15)
        self.yspeed = random.randrange(1, 13)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        self.pos = canvas.coords(self.shape)
        if self.pos[3] >= HEIGHT or self.pos[1] <=0:
            self.yspeed = -self.yspeed
        if self.pos [2] >= WIDTH or self.pos[0] <=0:
             self.xspeed = -self.xspeed

balls = []
for i in range(100):
    balls.append(Ball(60, 130, 6, 8, "blue"))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)
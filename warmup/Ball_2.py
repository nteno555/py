from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

class Ball:
    def __init__(self, start_x, start_y, xs, ys, fill_color):
        self.shape = canvas.create_oval(start_x, start_x, start_y, start_y, fill=fill_color)
        self.xspeed = xs
        self.yspeed = ys

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        self.pos = canvas.coords(self.shape)
        if self.pos[3] >= HEIGHT or self.pos[1] <=0:
            self.yspeed = -self.yspeed
        if self.pos [2] >= WIDTH or self.pos[0] <=0:
             self.xspeed = -self.xspeed
       
newball = Ball(10, 60, 20, 18, "purple")
didiball = Ball(90, 120, 10, 9, "blue")
niuniuball = Ball(20, 80, 14, 15, "green")

while True:
    newball.move()
    didiball.move()
    niuniuball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop

#Lol spam


from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

#I am making a canvas 500 pixels wide and 400 pixels tall
#I named the drawing "Drawing"
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

#This is making a variable telling the computer a ball is an orange circle with
#a radius of 25 pixels
co = "orange"
ball = canvas.create_oval(10, 10, 60, 60, fill=co)

#The first thing in the move command is what you want to move, then a
#number for how many pixels to the x direction, then a number for how many pixels
#you want to move it in the y direction
xspeed = 4
yspeed = 5
colorlist = ["green", "orange", "blue", "purple", "red", "yellow"]

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <=0:
        yspeed = -yspeed
        
    if pos [2] >= WIDTH or pos[0] <=0:
         xspeed = -xspeed
    tk.update()
    time.sleep(0.01)

tk.mainloop()
#Lol spam

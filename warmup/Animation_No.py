from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

canvas.create_line(0,0, 500, 400)
canvas.create_rectangle(0, 100, 200, 150, fill="blue")
canvas.create_oval(100, 100, 150, 150, fill="red")
canvas.create_line(500, 400, 10, 10)
canvas.create_oval(30, 30, 150, 150, fill="yellow")
canvas.create_rectangle(90, 90, 200, 200, fill="green")
canvas.create_polygon(10, 60, 110, 160, 210, 260, fill="purple")

colorlist = ["purple", "green", "yellow", "blue", "orange"]

canvas.create_oval(10, 10, 100, 100, fill=colorlist[0-4])

for i in range(100):
    x1 = random.randrange(500)
    y1 = random.randrange(400)
    x2 = random.randrange(500)
    y2 = random.randrange(400)
    canvas.create_rectangle(x1, y1, x2, y2, fill=colorlist[0-4])
    
canvas.mainloop

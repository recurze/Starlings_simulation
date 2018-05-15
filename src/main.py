from Tkinter import *
import time
import frame
import os
from constants import WIDTH, HEIGHT, BOID_RADIUS
f = frame.Frame()

tk = Tk()
tk.title("Boid Simulation")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT,
                bg="grey", cursor="fleur")

def toggle_c():
    f.option_c ^= 1
    if f.option_c:
        tk.cohesion_button["text"]="On"
    else:
        tk.cohesion_button["text"]="Off"

def toggle_s():
    f.option_s ^= 1
    if f.option_s:
        tk.separation_button["text"]="On"
    else:
        tk.separation_button["text"]="Off"

def toggle_a():
    f.option_a ^= 1
    if f.option_a:
        tk.alignment_button["text"]="On"
    else:
        tk.alignment_button["text"]="Off"

Label(tk, text="Cohesion").grid(row=0, column=0)
tk.cohesion_button = Button(tk, text="On", command=toggle_c)
tk.cohesion_button.grid(row=0, column=1)

Label(tk, text="Separation").grid(row=1, column=0)
tk.separation_button = Button(tk, text="On", command=toggle_s)
tk.separation_button.grid(row=1, column=1)

Label(tk, text="Alignment").grid(row=2, column=0)
tk.alignment_button = Button(tk, text="On", command=toggle_a)
tk.alignment_button.grid(row=2, column=1)

def draw():
    canvas.delete("all")
    for i in xrange(f.n):
        x, y = f.boids[i].posx, f.boids[i].posy
        canvas.create_oval(x-BOID_RADIUS,
                           y-BOID_RADIUS,
                           x+BOID_RADIUS,
                           y+BOID_RADIUS,
                           fill="black")

def callback(event):
    f.addBoid(event.x, event.y)

canvas.grid(row=3, column=3)
canvas.bind("<Button-1>", callback)

count = 0
def go():
    global count
    energyx = momentumx = 0.0
    energyy = momentumy = 0.0
    count += 1
    f.run()
    if count == 100:
        count = 0
        for i in f.boids:
            energyx += 0.5*i.velx*i.velx
            energyy += 0.5*i.vely*i.vely
            momentumx += i.velx
            momentumy += i.vely
        l = len(f.boids)
        if l:
            energyx /= l
            energyy /= l
            momentumx /= l
            momentumy /= l
        print "Average Energy: ", energyx + energyy
        print "Average momentum: ", momentumx , momentumy
    draw()
    canvas.after(1, go)

go()
tk.mainloop()

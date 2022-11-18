from tkinter import Tk as makescreen, Canvas, PhotoImage
from random import randint

screen = makescreen()
screen.title("Light Game")
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

canvas = Canvas(screen, width=700, height=500)
canvas.create_rectangle(0, 0, 700, 500, fill = 'black')
canvas.pack()
screen.update()

redimage = PhotoImage(file = 'red.png')
blueimage = PhotoImage(file = 'blue.png')
greenimage = PhotoImage(file = 'green.png')
blackimage = PhotoImage(file = 'black.png')

leftled = canvas.create_image(200, 250, image = blackimage)
rightled = canvas.create_image(500, 250, image = blackimage)
LEDlist = [redimage, blueimage, greenimage]


leftLED = greenimage
rightLED = blueimage

time = 1000
light = 'off'

score = 0
label = canvas.create_text(350, 50, text='score : 0', font=('consolas', 20), fill = 'white')
def setscore(number) :
    global score
    score += number
    canvas.itemconfig(label, text='score : '+str(score))

def running() :
    global left, right, light
    if light == 'off' :
        light = 'on'
        left = LEDlist[randint(0, 2)]
        right = LEDlist[randint(0, 2)]
        canvas.itemconfig(leftled, image = left)
        canvas.itemconfig(rightled, image = right)
    else :
        light = 'off'
        left = -1
        right = -2
        canvas.itemconfig(leftled, image = blackimage)
        canvas.itemconfig(rightled, image = blackimage)
    canvas.after(time-score, running)
running()

def differ(event) :
    if light == 'on' :
        if left != right :
            setscore(10)
        else :
            setscore(-10)

def equal(event) :
    if light == 'on' :
        if left == right :
            setscore(10)
        else :
            setscore(-10)

canvas.bind_all('<KeyRelease-d>', differ)
canvas.bind_all('<KeyRelease-s>', equal)
screen.mainloop()

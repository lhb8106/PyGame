from tkinter import Tk as makescreen, Canvas, PhotoImage
from random import randint

screen = makescreen()
screen.title("Pacman Game 1")
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

canvas = Canvas(screen, width=800, height=800)
canvas.create_rectangle(0, 0, 800, 800, fill = 'green')
canvas.pack()
screen.update()

right0image = PhotoImage(file = 'right0.png')
right1image = PhotoImage(file = 'right1.png')
left0image = PhotoImage(file = 'left0.png')
left1image = PhotoImage(file = 'left1.png')
up0image = PhotoImage(file = 'up0.png')
up1image = PhotoImage(file = 'up1.png')
down0image = PhotoImage(file = 'down0.png')
down1image = PhotoImage(file = 'down1.png')
ghostimage = PhotoImage(file = 'ghost.png')

pacman = canvas.create_image(400, 400, image = right0image)

rightlist = [right0image, right1image]
leftlist = [left0image, left1image]
uplist = [up0image, up1image]
downlist = [down0image, down1image]

score = 0
label = canvas.create_text(400, 100, text='', font=('consolas', 15))
def setscore(number) :
    global score
    score = number
    canvas.itemconfig(label, text='score : '+str(score))

rotate = 'right'
index = 0
def animation() :
    global index
    index += 1
    if rotate == 'right' :
        canvas.itemconfig(pacman, image = rightlist[index%2])
    elif rotate == 'left' :
        canvas.itemconfig(pacman, image = leftlist[index%2])
    elif rotate == 'up' :
        canvas.itemconfig(pacman, image = uplist[index%2])
    elif rotate == 'down' :
        canvas.itemconfig(pacman, image = downlist[index%2])
    setscore(score+1)
    canvas.after(300, animation)
animation()


ghost = canvas.create_image(50, 50, image = ghostimage)

def iscrush() :
    ghostpos = canvas.coords(ghost)
    pacpos = canvas.coords(pacman)
    if ghostpos[0]-75 < pacpos[0]+75 and ghostpos[0]+75 > pacpos[0]-75 :
        if ghostpos[1]-75 < pacpos[1]+75 and ghostpos[1]+75 > pacpos[1]-75 :
            return True
    return False

def ghostmove() :
    ghostpos = canvas.coords(ghost)
    pacpos = canvas.coords(pacman)
    x = (pacpos[0]-ghostpos[0])/3
    y = (pacpos[1]-ghostpos[1])/3
    canvas.move(ghost, x, y)
    if iscrush() :
        setscore(0)
    canvas.after(1000, ghostmove)
ghostmove()

def right(event) :
    global rotate
    rotate = 'right'
    canvas.move(pacman, 50, 0)
    
def left(event) :
    global rotate
    rotate = 'left'
    canvas.move(pacman, -50, 0)
    
def up(event) :
    global rotate
    rotate = 'up'
    canvas.move(pacman, 0, -50)
    
def down(event) :
    global rotate
    rotate = 'down'
    canvas.move(pacman, 0, 50)
    
canvas.bind_all('<KeyRelease-Right>', right)
canvas.bind_all('<KeyRelease-Left>', left)
canvas.bind_all('<KeyRelease-Up>', up)
canvas.bind_all('<KeyRelease-Down>', down)

screen.mainloop()

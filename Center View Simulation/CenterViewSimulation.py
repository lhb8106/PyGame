from tkinter import Tk as makescreen, Canvas, PhotoImage

screen = makescreen()
screen.title("Center View Game")
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

canvas = Canvas(screen, width=600, height=600) 
canvas.pack()
screen.update()

bgimage = PhotoImage(file='background.png')
walk0image = PhotoImage(file='walk0.png')
walk1image = PhotoImage(file='walk1.png')
walk2image = PhotoImage(file='walk2.png')
walk3image = PhotoImage(file='walk3.png')
walk4image = PhotoImage(file='walk4.png')
standimage = PhotoImage(file='stand.png')
tree0image = PhotoImage(file='tree0.png')
tree1image = PhotoImage(file='tree1.png')
flower0image = PhotoImage(file='flower0.png')
flower1image = PhotoImage(file='flower1.png')
boy0image = PhotoImage(file='boy0.png')
boy1image = PhotoImage(file='boy1.png')

canvas.create_image(300, 300, image = bgimage)

iswalk = False

tree0 = canvas.create_image(150, 190, image = tree0image)
def tree0move() :
    treepos = canvas.coords(tree0)
    if iswalk :
        if treepos[0] < 800 :
            canvas.move(tree0, 1, 0)
        else :
            canvas.coords(tree0, -200, 190)
    canvas.after(20, tree0move)
tree0move()

tree1 = canvas.create_image(300, 150, image = tree1image)
def tree1move() :
    treepos = canvas.coords(tree1)
    if iswalk :
        if treepos[0] < 800 :
            canvas.move(tree1, 2, 0)
        else :
            canvas.coords(tree1, -200, 150)
    canvas.after(20, tree1move)
tree1move()

flower0 = canvas.create_image(100, 380, image = flower0image)
def flower0move() :
    flowerpos = canvas.coords(flower0)
    if iswalk :
        if flowerpos[0] < 800 :
            canvas.move(flower0, 3, 0)
        else :
            canvas.coords(flower0, -200, 380)
    canvas.after(20, flower0move)
flower0move()

flower1 = canvas.create_image(400, 380, image = flower1image)
def flower1move() :
    flowerpos = canvas.coords(flower1)
    if iswalk :
        if flowerpos[0] < 800 :
            canvas.move(flower1, 4, 0)
        else :
            canvas.coords(flower1, -200, 380)
    canvas.after(20, flower1move)
flower1move()

boy = canvas.create_image(90, 300, image = boy0image)
def boymove() :
    boypos = canvas.coords(boy)
    if iswalk :
        if boypos[0] < 800 :
            canvas.move(boy, 4, 0)
        else :
            canvas.coords(boy, -200, 300)
    if boypos[0] > 100 and boypos[0] < 500 :
        canvas.itemconfig(boy, image = boy1image)
    else :
        canvas.itemconfig(boy, image = boy0image)
    canvas.after(20, boymove)
boymove()

girl = canvas.create_image(300, 330, image = walk0image)
walklist = [ walk0image, walk1image, walk2image, walk3image,
             walk4image, walk3image, walk2image, walk1image ]
index = 0
def walk() :
    global index
    if iswalk :
        index += 1
        canvas.itemconfig(girl, image = walklist[index%8])
    else :
        canvas.itemconfig(girl, image = standimage)
    canvas.after(200, walk)
walk()

def left(event) :
    global iswalk
    iswalk = True

def stop(event) :
    global iswalk
    iswalk = False

canvas.bind_all("<KeyPress-Left>", left)
canvas.bind_all("<KeyRelease-Left>", stop)

screen.mainloop()

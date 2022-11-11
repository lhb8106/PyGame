from tkinter import Tk as makescreen, Canvas, PhotoImage
from random import randint

screen = makescreen()
screen.title("Hurdling Game")
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

# load image
bgimage = PhotoImage(file='background.png')
jumpimage = PhotoImage(file='jump.png')
run0image = PhotoImage(file='run0.png')
run1image = PhotoImage(file='run1.png')
run2image = PhotoImage(file='run2.png')
hurdleimage = PhotoImage(file='hurdle.png')
brokenimage = PhotoImage(file='broken.png')

# create canvas
canvas = Canvas(screen, width=800, height=500)
canvas.pack()
screen.update()


# create background
canvas.create_image(400, 250, image = bgimage)

# create text
label = canvas.create_text(600, 250, text='score : 0, level : 0', font =('consolas', 20), fill = 'black')

# make human
runlist = [run0image, run1image, run2image,run1image]
index = 0
human = canvas.create_image(200, 350, image = runlist[index])
jump = False

jumpspeed = -30
gravity = 2
def jumping() :
      global jump, jumpspeed, gravity
      jump = True
      pos = canvas.coords(human)
      if pos[1] > 351 :
            jump = False
            jumpspeed = -30
            canvas.coords(human, 200, 350)
            return
      else :
            canvas.move(human, 0, jumpspeed)
            jumpspeed += gravity
            canvas.after(50, jumping)
            

      
def running() :
      global index
      if jump :
            canvas.itemconfig(human, image = jumpimage)
      else :
            index += 1
            canvas.itemconfig(human, image = runlist[index % 4])            
      canvas.after(300, running)
def jumpevent(event) :
      jumping()      
canvas.bind_all("<KeyRelease-s>", jumpevent)
running()

# make hurdle
hurdle = canvas.create_image(800, 450, image = hurdleimage)

def iscrush() :
      humanpos = canvas.coords(human)
      hurdlepos= canvas.coords(hurdle)
      if (humanpos[0]+100) > hurdlepos[0] and (humanpos[0]-100) < hurdlepos[0] and humanpos[1] > hurdlepos[1]-200:
            return True
      else :
            return False
      
def isright() :
      global score, speed
      hurdlepos= canvas.coords(hurdle)
      if hurdlepos[0] < 0 :
            return True
      else :
            return False

score = 0
speed = -3
level = 0
def move() :
      global speed, score, level
      if iscrush() :
            canvas.itemconfig(hurdle, image = brokenimage)
            score -= 1
      elif isright() :
            canvas.coords(hurdle, 800, 450)
            canvas.itemconfig(hurdle, image = hurdleimage)
            score += 5
            if score > 15 :
                  level += 1
                  score = 0
      canvas.itemconfig(label, text='score : ' + str(score) + ', level : ' + str(level))            
      canvas.move(hurdle, speed-level, 0)
      canvas.after(10, move)
move()

screen.mainloop()



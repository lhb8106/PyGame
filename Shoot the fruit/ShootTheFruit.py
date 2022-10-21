import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
score = 0
game_over = False
apple = Actor('apple')


def on_mouse_down(pos):
    global score

    if not game_over:
        if apple.collidepoint(pos):
            print("Good shot!")
            score = score + 100
            update_apple()
        else:
            print("You missed!")
            score = score - 50


def update_apple():
    apple.x = randint(10, 400)
    apple.y = randint(10, 400)


def end_the_game():
    global game_over
    game_over = True
    

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score : "+str(score), topleft=(10, 10))

    if game_over:
        screen.fill((147, 114, 229))
        screen.draw.text("Final Score : "+str(score), topleft=(10, 10), fontsize=60)


clock.schedule(end_the_game, 10.0)
clock.schedule_interval(update_apple, 1.0)
update_apple()

pgzrun.go()

#How to start?: cmd - pgzrun CoinCollector.py
from random import randint

WIDTH = 400 
HEIGHT = 400 

score = 0

game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin") 
coin.pos = 200, 200

 
def draw():
	screen.fill("lightgreen") 
	fox.draw() 
	coin.draw()
	screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))


	# Game Over Screeb
	if game_over:
		screen.fill("pink") # Change background to pink.
		screen.draw.text("Times Up! :( ", topleft=(10,60), fontsize=60) 
		screen.draw.text("Final Score: " + str(score), color="black", topleft=(10,10), fontsize=60) 




def place_coin():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True
	place_coin()



def update():
	global score

	speed = 5
	if keyboard.left:
		fox.x = fox.x - speed
		fox.image = "fox"

	if keyboard.right:
		fox.x = fox.x + speed
		fox.image = "fox"


	if keyboard.up:
		fox.y = fox.y - speed

	if keyboard.down:
		fox.y = fox.y + speed

	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		place_coin()
		speed = speed - .2



clock.schedule(time_up, 16.0)
place_coin()


import pgzrun
import random


#폰트 색깔 = white
FONT_COLOR = (255,255,255)

#화면 크기 결정
WIDTH = 800
HEIGHT = 600

#CENTER 좌표 구하기
CENTER_X = WIDTH /2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X, CENTER_Y)


FINAL_LEVEL = 6	#6단계까지 존재
START_SPEED = 10	#시작할 때 speed = 10
COLORS = ["green", "blue"]  #color 리스트에 green, blue 존재


#초기화
game_over = False
game_complete = False
current_level = 1
stars = []
animations = []


#객체 그리기
#game over & game complete : 해당 메시지
#그 외: 별들
def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0,0))     #space를 0,0에 그려라 (표시할 객체, 위치)
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        for star in stars:
            star.draw()

#star에 아무것도 없다면 make_stars호출
def update():
    global stars
    if len(stars) ==0:
        stars = make_stars(current_level)


def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars


def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create


def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) +1
    gap_size = WIDTH/ number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration = duration, on_finished=handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level +1
        stars = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize = 30, center = (CENTER_X, CENTER_Y + 30),
                     color = FONT_COLOR)


pgzrun.go()

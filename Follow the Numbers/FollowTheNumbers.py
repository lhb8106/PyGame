import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

#리스트 dots, lines 빈 리스트로 선언을 해 둠. 왜?
# 이거를 나중에 코드로 채워요. 안에 어떤 것들이 있는지
# 그거를 기반으로 그림을 그린다.
dots = []
lines = []

# 초기화
# 다음에 오는 점을 알기위해서 0~9 총 10개의 점을 그렸는데 그거를 알기위해서 선언을 해 둠.
next_dot = 0


#for문이라는 반복문
# 0~9까지 돈다. 10
for dot in range(0,10):
    # images폴더에 있는 이름 사용 (dot) -> 이름을 abc라고 바꾼다면 actor = Actor("abc")
    actor = Actor("dot")

    #랜덤으로 x, y 좌표를 가져옵니다. 그게 pos
    actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT - 20)

    
    dots.append(actor)
    #10개의 점이 저장이 되겠지?
    #dot = 0
    # 이미지를 찾아요
    # x,y 좌표를 찾아서 pos 찾아서 저장(dots라는 리스트에)



def draw():
    screen.fill("black") #screen 전체 색깔이 black

    #처음 숫자가  1이라고 이야기해주는거야 . 파이썬한테
    number = 1

    #int(number)
    
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number +1
        
    for line in lines:
        screen.draw.line(line[0], line[1], "red")


def on_mouse_down(pos):
    #전역변수 -> 변수를 선언
    global next_dot
    global lines

    
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
           # print(dots[next_dot -1].pos)
           # print(dots[next_dot].pos)
        next_dot = next_dot +1
    else :
        lines = []
        next_dot = 0

pgzrun.go()

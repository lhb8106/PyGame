import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

PI = 3.141592653

#새로운 창 screen 크기 선언 및 display
size = (400,500)
screen = pygame.display.set_mode(size)

#게임 타이틀 지정
pygame.display.set_caption("TEST GAME TITLE")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():    #유저가 어떤 행동을 했을 때
        if event.type == pygame.QUIT:   #유저 클릭 시 창 닫기
            done = True

    screen.fill(WHITE)

    #(0,0)에서 (100,100)으로 두께는 5
    pygame.draw.line(screen,GREEN, [0,0], [100,100], 5)

    #10간격으로 y축 늘리며 (0,10,20,30,40,50,60,70,80,90)
    for y_offset in range(0,100,10):
        pygame.draw.line(screen,RED,[0,10 + y_offset], [100,110 + y_offset], 5)

    #사각형 그리기 (학생 예제)
    pygame.draw.rect(screen, GREEN, [0,400,500,100],0)

    #원 0,1,2,3 총 4개 그리기
    for i in range(0,20,5):
        pygame.draw.ellipse(screen, BLACK, [20,20+i,250,100],2)

    #시작점, 끝나는 점 PI = 180
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI/2,2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

    #삼각형
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    #객체 생성(filename, size)
    #font = pygame.font.SysFont('Calibri', 25, True, False)
    font = pygame.font.SysFont(None, 25)

    #(text, antialias, color) antialias -> true면 smooth edge
    text = font.render("My text", True, BLACK)

    screen.blit(text, [250, 250])

    #디스플레이 갱신 및 화면표시
    pygame.display.flip()

    #초당 60프레임으로 제한
    clock.tick(60)

#프로그램 종료
pygame.quit()
        

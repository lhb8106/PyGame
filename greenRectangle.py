import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255,0,0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    numberOfRows = 60
    numberOfColumns = 70

    stepBetweenRects = 10

    for y in range(0, numberOfRows * stepBetweenRects, stepBetweenRects):
        for x in range(0, numberOfColumns * stepBetweenRects, stepBetweenRects):
            pygame.draw.rect(screen, GREEN, (x, y, 5, 5), 0)
    
    pygame.display.flip()
    clock.tick(60)
    


pygame.quit()

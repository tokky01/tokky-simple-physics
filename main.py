import pygame
import sys


pygame.init()


frames_per_second = 30
window_height = 600
window_width = 400


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

display = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

while True:
    clock.tick(frames_per_second)

    display.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

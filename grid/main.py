import pygame
from constants import *

# Initialize the PyGame GUI.
WIN = pygame.display.set_mode(
    (WIN_PIXEL_WIDTH, WIN_PIXEL_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption(APP_NAME)
WIN.fill(WHITE)
pygame.display.flip()


def main():
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    main()

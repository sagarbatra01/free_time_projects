import pygame
from constants import *

# Initialize the PyGame GUI.
WIN = pygame.display.set_mode(
    # (WIN_PIXEL_WIDTH, WIN_PIXEL_HEIGHT), pygame.FULLSCREEN)
    (WIN_PIXEL_WIDTH, WIN_PIXEL_HEIGHT))
pygame.display.set_caption(APP_NAME)


def drawGrid(old_selected):
    for x in range(0, WIN_PIXEL_WIDTH, BLOCK_SIZE):
        for y in range(0, WIN_PIXEL_HEIGHT, BLOCK_SIZE):
            block = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(WIN, BLOCK_COLOR, block, 1)
            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_block = pygame.Rect(
                mouseX, mouseY, CURSOR_RECT_SIZE, CURSOR_RECT_SIZE)
            if block.contains(mouse_block):
                selected = (x, y)
                if selected != old_selected:
                    pygame.mixer.Sound.play(HOVER_SOUND)
                highlight_block = pygame.Rect(
                    x + 1, y + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2)
                pygame.draw.rect(WIN, HIGHLIGHT_COLOR,
                                 highlight_block, 0)
    return selected


def main():
    selected = (0, 0)
    while(True):
        WIN.fill(BACKGROUND_COLOR)
        selected = drawGrid(selected)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(pygame.mouse.get_pos())


if __name__ == "__main__":
    main()

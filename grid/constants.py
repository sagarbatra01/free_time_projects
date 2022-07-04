import pygame

# Window Settings
APP_NAME = "Algorithm Visualizer"
BLOCK_SIZE = 40
ROWS = 25
COLS = 45
WIN_PIXEL_WIDTH = COLS * BLOCK_SIZE
WIN_PIXEL_HEIGHT = ROWS * BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (199, 208, 238)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (125, 125, 125)
YELLOW = (255, 255, 0)

GRID_COLOR = BLACK
BACKGROUND_COLOR = WHITE
BLOCK_COLOR = BLACK
HIGHLIGHT_COLOR = BLUE
FREE_COLOR = WHITE
WALL_COLOR = BLACK
START_COLOR = GREEN
END_COLOR = RED
# Sounds
pygame.mixer.init()
HOVER_SOUND = pygame.mixer.Sound(
    "D:\GitProjects\\free_time_projects\grid\hover.wav")
pygame.mixer.Sound.set_volume(HOVER_SOUND, 0.5)

# Game Settings
CURSOR_RECT_SIZE = 1
ALGO = "BFS"

import pygame

# Window Settings
APP_NAME = "Algorithm Visualizer"
WIN_PIXEL_WIDTH = 1200
WIN_PIXEL_HEIGHT = 720

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (199, 208, 238)

# Sounds
pygame.mixer.init()
HOVER_SOUND = pygame.mixer.Sound(
    "D:\GitProjects\\free_time_projects\grid\hover.wav")
pygame.mixer.Sound.set_volume(HOVER_SOUND, 0.5)

# Game Settings
BLOCK_SIZE = 40
BACKGROUND_COLOR = WHITE
BLOCK_COLOR = BLACK
HIGHLIGHT_COLOR = BLUE
CURSOR_RECT_SIZE = 1

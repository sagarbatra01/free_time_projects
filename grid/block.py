from tkinter import END
from pygame import GL_GREEN_SIZE
from constants import *


class Block:
    def __init__(self, row, col, size) -> None:
        self.row = row
        self.col = col
        self.size = size
        self.x = col * size
        self.y = row * size
        self.neighbors = []
        self.color = WHITE
        self.visited = False
        self.parent = None

    def display(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.size, self.size))

    def get_pos(self):
        return (self.row, self.col)

    def get_neighbors(self):
        return self.neighbors

    def set_pos(self, pos):
        self.row, self.col = pos

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_free(self):
        self.color = FREE_COLOR

    def is_free(self):
        return self.color == FREE_COLOR

    def set_wall(self):
        self.color = WALL_COLOR

    def is_wall(self):
        return self.color == WALL_COLOR

    def set_start(self):
        self.color = START_COLOR

    def is_start(self):
        return self.color == START_COLOR

    def set_end(self):
        self.color = END_COLOR

    def is_end(self):
        return self.color == END_COLOR

    def is_visited(self):
        return self.visited

    def set_visited(self, boolean):
        self.visited = boolean
        if not (self.is_start() or self.is_end() or self.is_wall()):
            if boolean:
                self.color = BLUE
            else:
                self.color = WHITE

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_path(self):
        self.color = YELLOW

    def is_path(self):
        return self.color == YELLOW

    def is_start_or_end(self):
        return self.color == GREEN or self.color == RED

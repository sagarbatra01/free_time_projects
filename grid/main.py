from block import *
from constants import *
import pygame
from collections import deque


def find_path(start, end):
    if ALGO == "BFS":
        q = deque()
        q.appendleft(start)
        start.set_visited(True)
        start.parent = None
        done = False
        while q:
            curr = q.pop()
            curr
            for n in curr.get_neighbors():
                if not n.is_visited() and not n.is_wall():
                    q.appendleft(n)
                    n.set_visited(True)
                    n.set_parent(curr)
                    if n == end:
                        done = True
                        break
            if done:
                break
        path = []
        curr = end
        while curr.get_parent() != None:
            path.append(curr.get_pos())
            curr = curr.get_parent()
            if curr != start:
                curr.set_path()

        path.reverse()
        return path


def is_within_borders(coord, MATRIX):
    return 0 <= coord[1] < len(MATRIX) and 0 <= coord[0] < len(MATRIX[0])


def find_neighbors(MATRIX, r, c):
    neighbors = set()
    for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        coord = c + offset[0], r + offset[1]
        if is_within_borders(coord, MATRIX):
            neighbors.add(MATRIX[coord[1]][coord[0]])
    return neighbors


def add_neighbors(MATRIX):
    for r in range(len(MATRIX)):
        for c in range(len(MATRIX[0])):
            MATRIX[r][c].set_neighbors(find_neighbors(MATRIX, r, c))


def createMatrix(rows, cols, size):
    matrix = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            block = Block(r, c, size)
            matrix[r].append(block)
    return matrix


def drawGrid(window, rows, cols, size):
    for r in range(rows):
        pygame.draw.line(window, GRID_COLOR, (0, r * size),
                         (cols * size, r * size))
        for c in range(cols):
            pygame.draw.line(window, GRID_COLOR, (c * size, 0),
                             (c * size, rows * size))


def clear_grid(MATRIX):
    for row in MATRIX:
        for block in row:
            block.color = WHITE
            block.set_visited(False)
            block.set_parent(None)
            block.neighbors.clear()
    add_neighbors(MATRIX)


def clear_path(MATRIX):
    for row in MATRIX:
        for block in row:
            if block.is_path():
                block.set_free()
            block.set_visited(False)
            block.set_parent(None)
            block.neighbors.clear()
    add_neighbors(MATRIX)


def drawBlocks(matrix, window):
    for row in matrix:
        for block in row:
            block.display(window)


def get_block(matrix, position, size):
    return matrix[position[1]//size][position[0]//size]


def main():
    pygame.init()
    WINDOW = pygame.display.set_mode(
        (WIN_PIXEL_WIDTH, WIN_PIXEL_HEIGHT))
    pygame.display.set_caption(APP_NAME)
    start, end = None, None
    MATRIX = createMatrix(ROWS, COLS, BLOCK_SIZE)
    add_neighbors(MATRIX)
    running = False
    while(True):
        if running:
            clear_path(MATRIX)
            find_path(start, end)
        WINDOW.fill(BACKGROUND_COLOR)
        drawBlocks(MATRIX, WINDOW)
        drawGrid(WINDOW, ROWS, COLS, BLOCK_SIZE)
        pygame.display.flip()
        block = get_block(
            MATRIX, pygame.mouse.get_pos(), BLOCK_SIZE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if start and end:
                        running = True

                elif event.key == pygame.K_c:
                    running = False
                    clear_grid(MATRIX)
                    start, end = None, None

            if pygame.mouse.get_pressed()[0]:
                if block.is_start():
                    if not running:
                        start = None
                        block.set_wall()
                elif block.is_end():
                    if not running:
                        end = None
                        block.set_wall()
                else:
                    block.set_wall()
                pygame.mixer.Sound.play(HOVER_SOUND)

            elif pygame.mouse.get_pressed()[1]:
                if block.is_start():
                    start = None
                if block.is_end():
                    end = None
                if start == None:
                    start = block
                    block.set_start()
                elif end == None:
                    end = block
                    block.set_end()
                else:
                    start.set_free()
                    start = block
                    block.set_start()
                pygame.mixer.Sound.play(HOVER_SOUND)

            elif pygame.mouse.get_pressed()[2]:
                if block.is_start():
                    if not running:
                        start = None
                        block.set_free()
                elif block.is_end():
                    if not running:
                        end = None
                        block.set_free()
                else:
                    block.set_free()

                pygame.mixer.Sound.play(HOVER_SOUND)


if __name__ == "__main__":
    main()

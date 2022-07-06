from block import *
from constants import *
import pygame
from collections import deque
import random


def is_edge(c, r, MATRIX):
    return (r in (0, len(MATRIX) - 1) or
            c in (0, len(MATRIX[0]) - 1))


def create_borders(MATRIX):
    for r in range(len(MATRIX)):
        for c in range(len(MATRIX[0])):
            if is_edge(c, r, MATRIX) and not MATRIX[r][c].is_start_or_end():
                MATRIX[r][c].set_wall()


def fill_walls(MATRIX, WINDOW):
    for r in range(len(MATRIX)):
        for c in range(len(MATRIX[0])):
            MATRIX[r][c].set_wall()
            MATRIX[r][c].display(WINDOW)


def is_within_borders(coord, MATRIX):
    return 0 <= coord[1] < len(MATRIX) and 0 <= coord[0] < len(MATRIX[0])


def find_neighbors(MATRIX, r, c, d):
    neighbors = []
    for offset in [(-d, 0), (d, 0), (0, -d), (0, d)]:
        coord = c + offset[0], r + offset[1]
        if is_within_borders(coord, MATRIX):
            neighbors.append(MATRIX[coord[1]][coord[0]])
    return neighbors


def add_neighbors(MATRIX, d=1):
    for r in range(len(MATRIX)):
        for c in range(len(MATRIX[0])):
            MATRIX[r][c].set_neighbors(find_neighbors(MATRIX, r, c, d))


def create_Matrix(rows, cols, size):
    matrix = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            block = Block(r, c, size)
            matrix[r].append(block)
    return matrix


def draw_grid(window, rows, cols, size):
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
            block.neighbors = []
    add_neighbors(MATRIX)


def clear_path(MATRIX, WINDOW):
    for row in MATRIX:
        for block in row:
            if block.is_path():
                block.set_free()
            block.set_visited(False)
            block.set_parent(None)
            block.neighbors = []
            block.display(WINDOW)
    add_neighbors(MATRIX)


def draw_blocks(matrix, window):
    for row in matrix:
        for block in row:
            block.display(window)


def get_block(matrix, position, size):
    return matrix[position[1]//size][position[0]//size]


def find_path(algo, start, end, WINDOW, show_grid):
    if algo == "BFS":
        q = deque()
        q.appendleft(start)
        start.set_visited(True)
        start.parent = None
        done = False
        while q:
            curr = q.pop()
            for n in curr.get_neighbors():
                if not n.is_visited() and not n.is_wall():
                    q.appendleft(n)
                    n.set_visited(True)
                    n.display(WINDOW)
                    n.set_parent(curr)
                    if n == end:
                        done = True
                        break
            show_grid = False
            if show_grid:
                draw_grid(WINDOW, ROWS, COLS, BLOCK_SIZE)
            pygame.display.update()
            if done:
                break
        path = []
        curr = end
        while curr.get_parent() != None:
            path.append(curr)
            curr = curr.get_parent()

        path.reverse()

        for block in path[:-1]:
            block.set_path()
            block.display(WINDOW)
            #draw_grid(WINDOW, ROWS, COLS, BLOCK_SIZE)
            pygame.display.update()
            pygame.time.delay(DELAY)


def generate_maze(algo, MATRIX, WINDOW):
    clear_path(MATRIX, WINDOW)
    add_neighbors(MATRIX, 2)
    if algo == "recursive_backtracking":
        fill_walls(MATRIX, WINDOW)
        pygame.display.update()
        start = MATRIX[1][1]
        end = MATRIX[len(MATRIX)-2][len(MATRIX[0])-2]
        s = deque()
        s.appendleft(start)
        curr = start
        while s:
            if not curr.is_start_or_end():
                curr.set_free()
                curr.display(WINDOW)
            random.shuffle(curr.get_neighbors())
            for n in curr.get_neighbors():
                if not n.is_visited():
                    break
            else:
                curr = s.popleft()
                continue
            s.appendleft(n)
            n.set_visited(True)
            middle = MATRIX[(n.get_pos()[0]+curr.get_pos()[0]) //
                            2][(n.get_pos()[1]+curr.get_pos()[1])//2]
            middle.set_free()
            middle.display(WINDOW)
            curr = n

            #draw_grid(WINDOW, ROWS, COLS, BLOCK_SIZE)
            pygame.display.update()
            pygame.time.delay(DELAY)
        start.set_start()
        end.set_end()
        return start, end

    create_borders(MATRIX)


def main():
    pygame.init()
    WINDOW = pygame.display.set_mode(
        (WIN_PIXEL_WIDTH, WIN_PIXEL_HEIGHT))
    pygame.display.set_caption(APP_NAME)
    start, end = None, None
    MATRIX = create_Matrix(ROWS, COLS, BLOCK_SIZE)
    add_neighbors(MATRIX)
    running = False
    show_grid = True
    update = False
    while(True):
        draw_blocks(MATRIX, WINDOW)
        pygame.display.update()
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
                        clear_path(MATRIX, WINDOW)
                        find_path("BFS", start, end, WINDOW, show_grid)

                elif event.key == pygame.K_c:
                    running = False
                    clear_grid(MATRIX)
                    start, end = None, None

                elif event.key == pygame.K_g:
                    show_grid = not show_grid

                elif event.key == pygame.K_w:
                    create_borders(MATRIX)
                    if running:
                        update = True

                elif event.key == pygame.K_m:
                    if not running:
                        start, end = generate_maze(
                            "recursive_backtracking", MATRIX, WINDOW)
            elif event.type == pygame.MOUSEBUTTONUP:
                if update:
                    clear_path(MATRIX, WINDOW)
                    find_path("BFS", start, end, WINDOW, show_grid)
                    update = False
            if pygame.mouse.get_pressed()[0]:
                if not block.is_wall():
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

                    block.display(WINDOW)

                    if running:
                        update = True

            elif pygame.mouse.get_pressed()[1]:
                if not block.is_start_or_end():
                    if start and not end:
                        end = block
                        block.set_end()
                    else:
                        if start:
                            start.set_free()
                        start = block
                        block.set_start()
                    if running:
                        update = True

            elif pygame.mouse.get_pressed()[2]:
                if not (block.is_free() or block.is_visited()):
                    if block.is_start_or_end():
                        if not running:
                            block.set_free()
                            if block.is_start():
                                start = None
                            if block.is_end():
                                end = None
                    else:
                        block.set_free()
                    if running:
                        update = True


if __name__ == "__main__":
    main()

import pygame
from node import Node
import gruvbox_colors as Colors


def heuristic(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    return abs(x1 - x2) + abs(y1 - y2)


def genGrid(rows, size):
    grid = []
    gap = size // rows
    for x in range(rows):
        grid.append([])
        for y in range(size):
            node = Node(x, y, gap, rows)
            grid[x].append(node)

    return grid


def drawGrid(window, rows, size):
    gap = size // rows
    col = Colors.GREY
    for x in range(rows):
        pygame.draw.line(window, col, (0, x * gap), (size, x * gap))
        for y in range(rows):
            pygame.draw.line(window, col, (y * gap, 0), (y * gap, size))


def draw(window, grid, rows, size):
    window.fill(Colors.WHITE)

    for row in grid:
        for block in row:
            block.draw(window)

    drawGrid(window, rows, size)
    pygame.display.update()


def getClickedPos(pos, rows, size):
    gap = size // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

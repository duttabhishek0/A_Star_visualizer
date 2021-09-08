import pygame as Game
import gruvbox_colors as Colors


class Node:
    def __init__(self, row, col, size, rowCount):
        self.row = row
        self.col = col
        self.size = size
        self.rowCount = rowCount

        self.x = row * size
        self.y = col * size
        self.color = Colors.WHITE
        self.neighbors = []

    def getPos(self):
        return (self.row, self.col)

    def isClosed(self):
        return self.color == Colors.RED

    def isOpen(self):
        return self.color == Colors.GREEN

    def isWall(self):
        return self.color == Colors.BLACK

    def isStart(self):
        return self.color == Colors.ORANGE

    def isEnd(self):
        return self.color == Colors.PURPLE

    def reset(self):
        self.color = Colors.WHITE

    def setStart(self):
        self.color = Colors.ORANGE

    def setEnd(self):
        self.color = Colors.AQUA

    def setClosed(self):
        self.color = Colors.RED

    def setOpen(self):
        self.color = Colors.GREEN

    def setWall(self):
        self.color = Colors.BLACK

    def setPath(self):
        self.color = Colors.PURPLE

    def draw(self, win):
        Game.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def __lt__(self, other):
        return False

    def getNeighbors(self, grid):
        self.neighbors = []
        row = self.row
        col = self.col
        netRows = self.rowCount

        # Get Down
        if row < netRows - 1 and not grid[row + 1][col].isWall():
            self.neighbors.append(grid[row + 1][col])
        # Get Up
        if row > 0 and not grid[row - 1][col].isWall():
            self.neighbors.append(grid[row - 1][col])
        # Get Right
        if col < netRows - 1 and not grid[row][col + 1].isWall():
            self.neighbors.append(grid[row][col + 1])
        # Get Left
        if col > 0 and not grid[row][col - 1].isWall():
            self.neighbors.append(grid[row][col - 1])

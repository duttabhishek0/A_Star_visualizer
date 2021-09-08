import pygame
import astar_draw as graph
import node
from queue import PriorityQueue


def astar(draw, grid, start, end):
    count = 0
    openQueue = PriorityQueue()
    cameFrom = {}
    gScr = {node: float("inf") for row in grid for node in row}
    fScr = {node: float("inf") for row in grid for node in row}

    gScr[start] = 0
    fScr[start] = graph.heuristic(start.getPos(), end.getPos())
    openQueue.put((0, count, start))
    openHash = {start}

    while not openQueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = openQueue.get()[2]
        openHash.remove(curr)

        if curr == end:
            buildPath(cameFrom, end, draw)
            end.setEnd()
            return True

        for nbh in curr.neighbors:
            tmp = gScr[curr] + 1

            if tmp < gScr[nbh]:
                cameFrom[nbh] = curr
                gScr[nbh] = tmp
                fScr[nbh] = tmp + graph.heuristic(nbh.getPos(), end.getPos())
                if nbh not in openHash:
                    count += 1
                    openQueue.put((fScr[nbh], count, nbh))
                    openHash.add(nbh)
                    nbh.setOpen()

        draw()

        if curr != start:
            curr.setClosed()

    return False


def buildPath(cameFrom, curr, draw):
    while curr in cameFrom:
        curr.setPath()
        curr = cameFrom[curr]
        draw()

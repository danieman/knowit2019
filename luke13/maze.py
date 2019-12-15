# Note to self: 
# Aldri vis denne dritten til noen
# Rewrite fullstendig en vakker dag


import json
import sys
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v):
        if not v.visited:
            self.visited += 1
        if v.pos == (499, 499):
            print(self.visited)
            sys.exit(0)
        v.visited = True
        for i in self.graph[v]:
            if not i.visited:
                self.DFSUtil(i)

    def DFS(self):
        global d
        start = d[(0, 0)]
        self.DFSUtil(start)


class Cell:
    def __init__(self, pos, n, w, s, e):
        self.pos = pos
        self.north = n
        self.west = w
        self.south = s
        self.east = e
        self.visited = False


def arthur():
    sys.setrecursionlimit(5000)
    global d
    g = Graph()
    for pos, cell in d.items():
        x, y = pos
        if not cell.south:
            g.addEdge(cell, d[(x, y+1)])
        if not cell.east:
            g.addEdge(cell, d[(x+1, y)])
        if not cell.west:
            g.addEdge(cell, d[(x-1, y)])
        if not cell.north:
            g.addEdge(cell, d[(x, y-1)])
    g.DFS()


def isaac():
    sys.setrecursionlimit(5000)
    global d
    g = Graph()
    for pos, cell in d.items():
        x, y = pos
        if not cell.east:
            g.addEdge(cell, d[(x+1, y)])
        if not cell.south:
            g.addEdge(cell, d[(x, y+1)])
        if not cell.west:
            g.addEdge(cell, d[(x-1, y)])
        if not cell.north:
            g.addEdge(cell, d[(x, y-1)])
    g.DFS()


maze = json.load(open('MAZE.TXT'))
d = {}

for row in maze:
    for cell in row:
        x, y = cell['x'], cell['y']
        d[(x, y)] = Cell((x, y),
                         cell['nord'],
                         cell['vest'],
                         cell['syd'],
                         cell['aust'])

# Run one at a time:
#arthur()
isaac()



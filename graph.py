import numpy as np
import queue_implementation
import stack

class Graph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.graph = 0
        self.connectedComponensClass = []
        self.connectedComponens = []
        

    def bfs(self, s):
        self.bfsVector = np.zeros(self.n, dtype=object)
        self.bfsTree = np.zeros(self.n, dtype=object)
        self.bfsQueue = queue_implementation.Queue()
        self.bfsVector[s - 1] = 1
        self.bfsQueue.enqueue(s)
        self.levels = {s: 0}

        

    def dfs(self, s):
        self.dfsVector = np.zeros(self.n, dtype=object)
        self.dfsStack = stack.Stack()
        self.dfsStack.push(s)
        self.prev = s
        self.levels = {}

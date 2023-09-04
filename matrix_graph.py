import numpy as np
import queue
import stack

class MatrixGraph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.myGraph = 0

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.myGraph = np.zeros((self.n, self.n), dtype=int)
            for linha in f:
                self.m += 1
                i, j = map(int, linha.split())
                self.myGraph[i - 1][j - 1] = 1
                self.myGraph[j - 1][i - 1] = 1

    def bfs(self, s):
        bfsVector = np.zeros(self.n, dtype=object)
        bfsTree = np.zeros(self.n, dtype=object)
        bfsQueue = queue.Queue()
        bfsVector[s - 1] = 1
        bfsQueue.enqueue(s)
        while not bfsQueue.isEmpty():
            v = bfsQueue.dequeue()
            i = 1
            for isNeighbor in self.myGraph[v - 1]:
                if isNeighbor == 1:
                    if bfsVector[i - 1] == 0:
                        bfsVector[i - 1] = 1
                        bfsTree[i-1] = v
                        print("pai de", i, v)
                        bfsQueue.enqueue(i)
                i += 1
        return bfsTree

    def dfs(self, s):
        dfsVector = np.zeros(self.n, dtype=object)
        dfsStack = stack.Stack()
        dfsStack.push(s)
        prev = s
        while not dfsStack.isEmpty():
            v = dfsStack.pop()
            if dfsVector[v - 1] == 0:
                dfsVector[v - 1] = 1
                print("pai de", v, prev)
                i = 1
                for isNeighbor in self.myGraph[v - 1]:
                    if isNeighbor == 1:
                        w = i
                        dfsStack.push(w)
                    i += 1
            prev = v

    def graphInfo(self, file):
        with open(file, 'w') as f:
            f.write(str(self.n)+'\n')
            f.write(str(self.m))

    def dist(self, u, v):
        tree = self.bfs(u)
        if tree[v] != 0:
            c = 1
            dad = tree[v-1]
            while c < self.n:
                if u == dad:
                    return c
                else: 
                    dad = tree[dad-1]
                    c+=1
        return "u and v are equal or there is no path between them"
    
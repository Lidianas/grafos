import numpy as np
import queue_implementation
import stack
from graph import Graph

class MatrixGraph(Graph):

    def __init__(self):
        super().__init__()

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.graph = np.zeros((self.n, self.n), dtype=int)
            self.connectedComponentsClass = np.zeros(self.n)
            for linha in f:
                self.m += 1
                i, j = map(int, linha.split())
                self.graph[i - 1][j - 1] = 1
                self.graph[j - 1][i - 1] = 1

    def bfs(self, s, output_file_dir):

        super().bfs(s)
        with open(output_file_dir, "w") as file:
            file.write(f"Vértice {s}: Pai = {s}, Nível = {0}\n")
            while not self.bfsQueue.isEmpty():
                v = self.bfsQueue.dequeue()
                i = 1
                for isNeighbor in self.graph[v - 1]:
                    if isNeighbor == 1:
                        if self.bfsVector[i - 1] == 0:
                            self.bfsVector[i - 1] = 1
                            self.bfsTree[i - 1] = v
                            self.levels[i] = self.levels[v] + 1 if v in self.levels else 0
                            file.write(f"Vértice {i}: Pai = {v}, Nível = {self.levels[i]}\n")
                            self.bfsQueue.enqueue(i)
                    i += 1
        return self.bfsTree, self.bfsVector, v

    def dfs(self, s, output_file_dir):

        super().dfs(s)
        with open(output_file_dir, "w") as file:
            while not self.dfsStack.isEmpty():
                v = self.dfsStack.pop()
                if self.dfsVector[v - 1] == 0:
                    self.dfsVector[v - 1] = 1
                    self.levels[v] = self.levels[self.prev] + 1 if self.prev in self.levels else 0
                    file.write(f"Vértice {v}: Pai = {self.prev}, Nível = {self.levels[v]}\n")
                    i = 1
                    for isNeighbor in self.graph[v - 1]:
                        if isNeighbor == 1:
                            w = i
                            self.dfsStack.push(w)
                        i += 1
                selfprev = v

    def graphInfo(self, file):

        self.arrDegree = []
        
        if len(self.graph) != 0:
            for incident in self.graph:
                self.arrDegree.append(np.count_nonzero(incident == 1))
        
        super().graphInfo(file)




import numpy as np
import linked_list
import queue_implementation
import stack
from graph import Graph

class ListGraph(Graph):

    def __init__(self):
        super().__init__()

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.graph = np.empty(self.n, dtype=object)
            self.connectedComponentsClass = np.zeros(self.n)
            for i in range(self.n):
                self.graph[i] = linked_list.LinkedList()
            for linha in f:
                self.m += 1
                i, j = map(int, linha.split())
                self.graph[i - 1].append(j)
                self.graph[j - 1].append(i)

    def bfs(self, s, output_file_dir):

        super().bfs(s)
        with open(output_file_dir, "w") as file:
            file.write(f"Vértice {s}: Pai = {s}, Nível = {0}\n")
            while not self.bfsQueue.isEmpty():
                v = self.bfsQueue.dequeue()
                neighbor = self.graph[v - 1].head
                while neighbor is not None:
                    if self.bfsVector[neighbor.data - 1] == 0:
                        self.bfsVector[neighbor.data - 1] = 1
                        self.bfsTree[neighbor.data - 1] = v
                        self.levels[neighbor.data] = self.levels[v] + 1 if v in self.levels else 0
                        file.write(f"Vértice {neighbor.data}: Pai = {v}, Nível = {self.levels[neighbor.data]}\n")
                        self.bfsQueue.enqueue(neighbor.data)
                    neighbor = neighbor.next
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
                    neighbor = self.graph[v - 1].head
                    while neighbor is not None:
                        self.dfsStack.push(neighbor.data)
                        neighbor = neighbor.next
                self.prev = v

    def getIncidenceByVertice(self, v):
        neighbor = self.graph[v].head
        arrIncidence = []
        while neighbor is not None:
            arrIncidence.append(neighbor.next)
            neighbor = neighbor.next

        return arrIncidence

    def graphInfo(self, file):

        self.arrDegree = []

        if len(self.graph) != 0:
            for incident in range(len(self.graph)):
                tmp_incidents = self.getIncidenceByVertice(incident)
                self.arrDegree.append(len(tmp_incidents))
        
        super().graphInfo(file)
 
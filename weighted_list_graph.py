import math

import numpy as np

from linked_list import WeightedLinkedList
from distStructures import distHeap, distVector


class WeightedListGraph:

    def __init__(self, id):
        self.n = 0
        self.m = 0
        self.graph = 0
        self.negativeWeights = False
        self.dist_s = 0
        self.path_s = 0
        self.dijType = id

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.graph = np.empty(self.n, dtype=object)
            for i in range(self.n):
                self.graph[i] = WeightedLinkedList()
            for linha in f:
                self.m += 1
                i, j, w = map(float, linha.split())
                i = int(i)
                j = int(j)
                if not self.negativeWeights and w < 0:
                    self.negativeWeights = True
                self.graph[i - 1].append(j, w)
                self.graph[j - 1].append(i, w)
        if self.dijType == 1:
            self.dist_s = distVector(self.n)
        elif self.dijType == 2:
            self.dist_s = distHeap(self.n)
        self.path_s = [[] for _ in range(self.n)]

    def dijkstra(self, s):
        count = 0
        self.dist_s.updateDist(s, 0)
        while count != self.n:
            u = self.dist_s.getMinDist()
            count += 1
            neighbor = self.graph[u - 1].head
            while neighbor is not None:
                viz = neighbor.data
                weight = neighbor.peso
                if self.dist_s.checkDist(viz) > self.dist_s.checkDist(u) + weight:
                    self.dist_s.updateDist(viz, self.dist_s.checkDist(u) + weight)
                    self.path_s[viz - 1] = []
                    if self.path_s[u-1] != []:
                        self.path_s[viz - 1].extend(self.path_s[u-1])
                    self.path_s[viz - 1].append(u)
                neighbor = neighbor.next
        print(self.dist_s.checkDist(2))
        return self.dist_s, self.path_s

    def minDistPath(self, s):
        if self.negativeWeights:
            raise Exception("Caminhos negativos não implementados")
        else:
            return self.dijkstra(s)

import numpy as np

from linked_list import WeightedLinkedList


class WeightedListGraph:

    def __init__(self):
        self.n = 0
        self.m = 0
        self.graph = 0
        self.negativeWeights = False

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

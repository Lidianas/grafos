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
            self.ccClass = np.zeros(self.n)
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
                    self.levels[v] = self.levels[prev] + 1 if prev in self.levels else 0
                    file.write(f"Vértice {v}: Pai = {prev}, Nível = {self.levels[v]}\n")
                    i = 1
                    for isNeighbor in self.graph[v - 1]:
                        if isNeighbor == 1:
                            w = i
                            self.dfsStack.push(w)
                        i += 1
                prev = v

    def graphInfo(self, file):

        arrDegree = []
        if len(self.graph) != 0:
            for incident in self.graph:
                arrDegree.append(np.count_nonzero(incident == 1))

        minDegree = min(arrDegree)
        maxDegree = max(arrDegree)
        meanDegree = sum(arrDegree) / len(arrDegree)

        arrDegreeOrdered = sorted(arrDegree)
        if len(arrDegree) % 2 != 0:
            medianDegree = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2)]
        else:
            middle1 = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2)]
            middle2 = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2 - 1)]
            medianDegree = (middle1 + middle2) / 2

        with open("saida/" + file, 'w') as f:
            f.write("Vértices: " + str(self.n) + '\n')
            f.write("Arestas: " + str(self.m) + '\n')
            f.write("Grau mínimo: " + str(minDegree) + '\n')
            f.write("Grau máximo: " + str(maxDegree) + '\n')
            f.write("Média dos graus: " + str(meanDegree) + '\n')
            f.write("Mediana gos graus: " + str(medianDegree) + '\n')
            f.write("Número de componentes conexas: " + str(len(self.cc) - 1) + '\n')
            f.write("Tamanho da maior componente conexa: " + str(len(self.cc[0])) + '\n')
            f.write("Tamanho da menor componente conexa: " + str(len(self.cc[-1])) + '\n')

    def dist(self, u, v):
        tree = self.bfs(u)[0]
        if tree[v - 1] != 0:
            c = 1
            dad = tree[v - 1]
            while c < self.n:
                if u == dad:
                    return c
                else:
                    dad = tree[dad - 1]
                    c += 1
            return "there is no path between them \n"
        else:
            return "they do not belong to the same component \n"

    def approxDiameter(self):
        maxCC = []
        if len(self.cc) == 0:
            cc = self.connectedComponents()[1]
            maxCC = cc[0]
        else:
            maxCC = self.cc[0]

        firstbfs = self.bfs(maxCC[0])[2]
        secbfs = self.bfs(firstbfs)[2]
        d = self.dist(firstbfs, secbfs)
        return d

    def connectedComponents(self):

        tmp_cc = True
        cc = 1
        v = 1
        missingVertice = 0
        
        while tmp_cc:

            tmp_elCC = []
            tree, visitedVertices = self.bfs(v)[0:2]
            first = True
            for u in range(len(visitedVertices)):
                if visitedVertices[u] == 1 and self.ccClass[u] == 0:
                    self.ccClass[u] = cc
                    tmp_elCC.append(u + 1)
                elif visitedVertices[u] == 0 and self.ccClass[u] == 0 and first:
                    missingVertice = u + 1
                    first = False
                elif u==self.n-1 and first:
                    tmp_cc = False
            v = missingVertice
            cc += 1
            self.cc.append(tmp_elCC)

        self.cc = sorted(self.cc, key=len, reverse=True)
        return self.ccClass, self.cc



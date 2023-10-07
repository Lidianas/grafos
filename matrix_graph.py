from cmath import nan
import numpy as np
import queue_implementation
import stack


class MatrixGraph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.myGraph = 0
        self.ccClass = []
        self.cc = []

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.myGraph = np.zeros((self.n, self.n), dtype=int)
            self.ccClass = np.zeros(self.n)
            for linha in f:
                self.m += 1
                i, j = map(int, linha.split())
                self.myGraph[i - 1][j - 1] = 1
                self.myGraph[j - 1][i - 1] = 1

    def bfs(self, s):
        bfsVector = np.zeros(self.n, dtype=object)
        bfsTree = np.zeros(self.n, dtype=object)
        bfsQueue = queue_implementation.Queue()
        bfsVector[s - 1] = 1
        bfsQueue.enqueue(s)
        levels = {s: 0}
        v=None
        with open("saida/arvore_busca_bfs_matrix.txt", "w") as file:
            file.write(f"Vértice {s}: Pai = {s}, Nível = {0}\n")
            while not bfsQueue.isEmpty():
                v = bfsQueue.dequeue()
                i = 1
                for isNeighbor in self.myGraph[v - 1]:
                    if isNeighbor == 1:
                        if bfsVector[i - 1] == 0:
                            bfsVector[i - 1] = 1
                            bfsTree[i - 1] = v
                            levels[i] = levels[v] + 1 if v in levels else 0
                            file.write(f"Vértice {i}: Pai = {v}, Nível = {levels[i]}\n")

                            bfsQueue.enqueue(i)
                    i += 1
        return bfsTree, bfsVector, v

    def dfs(self, s):
        dfsVector = np.zeros(self.n, dtype=object)
        dfsStack = stack.Stack()
        dfsStack.push(s)
        prev = s
        levels = {}
        with open("saida/arvore_busca_dfs_matrix.txt", "w") as file:
            while not dfsStack.isEmpty():
                v = dfsStack.pop()
                if dfsVector[v - 1] == 0:
                    dfsVector[v - 1] = 1
                    levels[v] = levels[prev] + 1 if prev in levels else 0
                    file.write(f"Vértice {v}: Pai = {prev}, Nível = {levels[v]}\n")
                    i = 1
                    for isNeighbor in self.myGraph[v - 1]:
                        if isNeighbor == 1:
                            w = i
                            dfsStack.push(w)
                        i += 1
                prev = v

    def graphInfo(self, file):

        arrDegree = []
        if len(self.myGraph) != 0:
            for incident in self.myGraph:
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
    
    def diameter(self):
        maxDiam = 0
        for v in self.myGraph:
            for u in self.myGraph:
                tmp_maxDiameter = self.dist(v,u)
                if maxDiam > tmp_maxDiameter:
                    maxDiam = tmp_maxDiameter
        return maxDiam

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



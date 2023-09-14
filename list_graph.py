import numpy as np
import linked_list
import queue_implementation
import stack

class ListGraph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.myGraph = 0
        self.ccClass = []
        self.cc = []
        self.max = []
        self.min = []

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.myGraph = np.empty(self.n, dtype=object)
            for i in range(self.n):
                self.myGraph[i] = linked_list.LinkedList()
            for linha in f:
                self.m += 1
                i, j = map(int, linha.split())
                self.myGraph[i - 1].append(j)
                self.myGraph[j - 1].append(i)

    def bfs(self, s):
        bfsVector = np.zeros(self.n, dtype=object)
        bfsTree = np.zeros(self.n, dtype=object)
        bfsQueue = queue_implementation.Queue()
        bfsVector[s - 1] = 1
        bfsQueue.enqueue(s)
        levels = {s: 0}
        with open("arvore_busca_bfs_list.txt", "w") as file:
            file.write(f"Vértice {s}: Pai = {s}, Nível = {0}\n")
            while not bfsQueue.isEmpty():
                v = bfsQueue.dequeue()
                neighbor = self.myGraph[v - 1].head
                while neighbor is not None:
                    if bfsVector[neighbor.data - 1] == 0:
                        bfsVector[neighbor.data - 1] = 1
                        bfsTree[neighbor.data - 1] = v
                        levels[neighbor.data] = levels[v] + 1 if v in levels else 0
                        file.write(f"Vértice {neighbor.data}: Pai = {v}, Nível = {levels[neighbor.data]}\n")
                        bfsQueue.enqueue(neighbor.data)
                    neighbor = neighbor.next
        return bfsTree, bfsVector

    def dfs(self, s):
        dfsVector = np.zeros(self.n, dtype=object)
        dfsStack = stack.Stack()
        dfsStack.push(s)
        prev = s
        levels = {}
        with open("arvore_busca_dfs_list.txt", "w") as file:
            while not dfsStack.isEmpty():
                v = dfsStack.pop()
                if dfsVector[v - 1] == 0:
                    dfsVector[v - 1] = 1
                    levels[v] = levels[prev] + 1 if prev in levels else 0
                    file.write(f"Vértice {v}: Pai = {prev}, Nível = {levels[v]}\n")
                    neighbor = self.myGraph[v - 1].head
                    while neighbor is not None:
                        dfsStack.push(neighbor.data)
                        neighbor = neighbor.next
                prev = v

    def getIncidenceByVertice(self, v):
        neighbor = self.myGraph[v].head
        arrIncidence = []
        while neighbor is not None:
            arrIncidence.append(neighbor.next)
            neighbor = neighbor.next

        return arrIncidence

    def graphInfo(self, file):

        arrDegree = []
        if len(self.myGraph) != 0:
            for incident in range(len(self.myGraph)):
                tmp_incidents = self.getIncidenceByVertice(incident)
                arrDegree.append(len(tmp_incidents))

        minDegree = min(arrDegree)
        maxDegree = max(arrDegree)
        meanDegree = sum(arrDegree)/len(arrDegree)

        arrDegreeOrdered = sorted(arrDegree)
        if len(arrDegree) % 2 != 0:
            medianDegree = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2)]
        else:
            middle1 = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2)]
            middle2 = arrDegreeOrdered[int(len(arrDegreeOrdered) // 2 - 1)]
            medianDegree = (middle1 + middle2) / 2

        with open(file, 'w') as f:
            f.write("Vértices: " + str(self.n) + '\n')
            f.write("Arestas: " + str(self.m) + '\n')
            f.write("Grau mínimo: " + str(minDegree) + '\n')
            f.write("Grau máximo: " + str(maxDegree) + '\n')
            f.write("Média dos graus: " + str(meanDegree) + '\n')
            f.write("Mediana gos graus: " + str(medianDegree) + '\n')
            f.write("Número de componentes conexas: " + str(len(self.cc) - 1) + '\n')
            f.write("Tamanho da maior componente conexa: " + str(len(self.max)) + '\n')
            if len(self.min) != 0:
                f.write("Tamanho da menor componente conexa: " + str(len(self.min)) + '\n')

    def dist(self, u, v):
        tree = self.bfs(u)[0]
        if tree[v-1] != 0:
            c = 1
            dad = tree[v-1]
            while c < self.n:
                if u == dad:
                    return c
                else: 
                    dad = tree[dad-1]
                    c+=1
            return "there is no path between them \n"
        else: 
            return "u and v are equal \n"

    def diameter(self):
        biggerDistancePerVertice = []
        actual_dist = 0
        tmp_dist = 0

        for u in range(1, self.n+1):
            for v in range(1, self.n+1):
                if u != v: 
                    tmp_dist = self.dist(u, v)
                    if type(tmp_dist) == int:
                        if tmp_dist > actual_dist: 
                            actual_dist = tmp_dist
            biggerDistancePerVertice.append(actual_dist)

        return max(biggerDistancePerVertice)

    def connectedComponents(self):

        tmp_cc = True
        cc = 1
        v = 1
        self.ccClass = np.zeros(self.n)
        missingVertice = 0
        while tmp_cc:

            tmp_elCC = []
            tree, visitedVertices = self.bfs(v)
            for u in range(len(visitedVertices)):
                if visitedVertices[u] == 1 and self.ccClass[u] == 0:
                    self.ccClass[u] = cc
                    tmp_elCC.append(u + 1)
                elif visitedVertices[u] == 0 and self.ccClass[u] == 0:
                    missingVertice = u
                else:
                    tmp_cc = False
            v = missingVertice
            cc += 1
            self.cc.append(tmp_elCC)
        return self.ccClass, self.cc

    def max_min_cc(self):
        for i in self.cc:
            if len(i) > 0:
                if len(i) >= len(self.max):
                    self.max = i
                if len(i) <= len(self.min):
                    self.min = i
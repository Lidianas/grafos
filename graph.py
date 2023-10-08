import numpy as np
import queue_implementation
import stack

class Graph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.graph = 0
        self.connectedComponentsClass = []
        self.arrConnectedComponents = []
        

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

    def graphInfo(self, file):

        
        minDegree = min(self.arrDegree)
        maxDegree = max(self.arrDegree)
        meanDegree = sum(self.arrDegree)/len(self.arrDegree)

        arrDegreeOrdered = sorted(self.arrDegree)
        if len(self.arrDegree) % 2 != 0:
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
            f.write("Número de componentes conexas: " + str(len(self.arrConnectedComponents) - 1) + '\n')
            f.write("Tamanho da maior componente conexa: " + str(len(self.arrConnectedComponents[0])) + '\n')
            f.write("Tamanho da menor componente conexa: " + str(len(self.arrConnectedComponents[-2])) + '\n')

    def dist(self, u, v):

        tree = self.bfs(u, "grafos/tmp_bfs.txt")[0]
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
        maxConnectedComponent = []
        if len(self.arrConnectedComponents) == 0:
            counterConnectedComponent = self.connectedComponents()[1]
            maxConnectedComponent = counterConnectedComponent[0]
        else:
            maxConnectedComponent = self.counterConnectedComponent[0]

        firstbfs = self.bfs(maxConnectedComponent[0], "grafos/tmp_bfs.txt")[2]
        secbfs = self.bfs(firstbfs, "grafos/tmp_bfs.txt")[2]
        d = self.dist(firstbfs, secbfs)
        return d

    def connectedComponents(self):

        hasConnectedComponent = True
        counterConnectedComponent = 1
        v = 1
        missingVertice = 0
        
        while hasConnectedComponent:

            actualConnectedComponent = []
            tree, visitedVertices = self.bfs(v, "grafos/tmp_bfs.txt")[0:2]
            first = True
            for u in range(len(visitedVertices)):
                if visitedVertices[u] == 1 and self.connectedComponentsClass[u] == 0:
                    self.connectedComponentsClass[u] = counterConnectedComponent
                    actualConnectedComponent.append(u + 1)
                elif visitedVertices[u] == 0 and self.connectedComponentsClass[u] == 0 and first:
                    missingVertice = u + 1
                    first = False
                elif u==self.n-1 and first:
                    hasConnectedComponent = False
            v = missingVertice
            counterConnectedComponent += 1
            self.arrConnectedComponents.append(actualConnectedComponent)

        self.arrConnectedComponents = sorted(self.arrConnectedComponents, key=len, reverse=True)
        return self.connectedComponentsClass, self.arrConnectedComponents
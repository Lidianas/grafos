from cmath import nan
import numpy as np
import queue
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
                        #print("pai de", i, v)
                        bfsQueue.enqueue(i)
                i += 1
        return bfsTree, bfsVector

    def dfs(self, s):
        dfsVector = np.zeros(self.n, dtype=object)
        dfsStack = stack.Stack()
        dfsStack.push(s)
        prev = s
        while not dfsStack.isEmpty():
            v = dfsStack.pop()
            if dfsVector[v - 1] == 0:
                dfsVector[v - 1] = 1
                #print("pai de", v, prev)
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
        meanDegree = sum(arrDegree)/len(arrDegree)
        
        arrDegreeOrdered = sorted(arrDegree)
        if len(arrDegree)%2 != 0: medianDegree = arrDegreeOrdered[int((len(arrDegreeOrdered)+1)/2)]
        else: medianDegree = (arrDegreeOrdered[(len(arrDegreeOrdered))/2] + arrDegreeOrdered[(len(arrDegreeOrdered)+1)/2])/2


        with open(file, 'w') as f:
            f.write("Vértices: " + str(self.n) + '\n')
            f.write("Arestas: " + str(self.m) + '\n')
            f.write("Grau mínimo: " + str(minDegree) + '\n')
            f.write("Grau máximo: " + str(maxDegree) + '\n')
            f.write("Média dos graus: " + str(meanDegree) + '\n')
            f.write("Mediana gos graus: " + str(medianDegree) + '\n')

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
             "u and v are equal \n"
    
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
                    tmp_elCC.append(u+1)
                elif visitedVertices[u] == 0 and self.ccClass[u] ==  0:
                    missingVertice = u
                else:
                    tmp_cc = False
            v = missingVertice
            cc+=1
            self.cc.append(tmp_elCC)
        return self.ccClass, self.cc
        
        
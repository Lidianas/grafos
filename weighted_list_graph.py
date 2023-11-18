import numpy as np
from graph import Graph
from linked_list import DirectedWeightedLinkedList
from distStructures import distHeap, distVector
from list_graph import ListGraph
from residual_list_graph import ResidualGraph


class WeightedListGraph(ListGraph):

    def __init__(self, id, oriented):
        self.n = 0
        self.m = 0
        self.graph = 0
        self.negativeWeights = False
        self.dist_s = 0
        self.path_s = 0
        self.dijType = id
        self.oriented = oriented

    def readGraph(self, file):
        with open(file, 'r') as f:
            self.n = int(f.readline())
            self.graph = np.empty(self.n, dtype=object)
            for i in range(self.n):
                self.graph[i] = DirectedWeightedLinkedList()
            for linha in f:
                self.m += 1
                i, j, w = map(float, linha.split())
                i = int(i)
                j = int(j)
                if not self.negativeWeights and w < 0:
                    self.negativeWeights = True
                self.graph[i - 1].append(j, w, 0)
                if not self.oriented:
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
        return self.dist_s, self.path_s

    def minDistPath(self, s):
        if self.negativeWeights:
            raise Exception("Caminhos negativos não implementados")
        else:
            return self.dijkstra(s)
        
    def fordFulkerson(self, source, target):
        currentBottleneck=0
        residualGraph = ResidualGraph(self.n)
        residualGraph.setResidualGraph(self.graph)
        path = [0]
        maxF = 0
        while len(path) != 0:
            tree = residualGraph.bfs(source, "dg_output.txt")[0]
            bottleneck, path = self.bottleneck(tree, target, residualGraph)
            if len(path) != 0: 
                currentBottleneck = bottleneck
            self.augment(currentBottleneck, path, target)
            residualGraph.updateResidualGraph(self.graph)
        
        arrFlowAlloc = self.flowAlloc()
        v = self.graph[0].head
        while v is not None:
            maxF += v.currentFlow
            v = v.next
        return maxF, arrFlowAlloc

    def bottleneck(self, tree, target, residualGraph):
        b = np.inf
        actual = target
        path = []

        node = tree[actual - 1]
        while (node != 0):
            v = residualGraph.graph[node-1].head
            while v.data != actual:
                v = v.next
            
            p = v.capacity
            if p < b:
                b = p

            path.append((node, p, v.isOriginal))
            actual = node
            node = tree[actual - 1]
            
        return b, path
    
    def augment(self, b, path, target):
        tmp = target
        maxF = 0
        tmp_maxF = 0
        for p in path:
            v = self.graph[p[0]-1].head
            while v is not None:
                if v.data == tmp:
                    break
                else:
                    v = v.next 

            if p[2] is True:
                v.currentFlow += b
                tmp_maxF = v.currentFlow
            else:
                v.currentFlow -= b
                tmp_maxF = v.currentFlow
            tmp = p[0]
            
            if tmp_maxF > maxF:
                maxF = tmp_maxF
        return maxF

    def flowAlloc(self):
        arrFlowAlloc = []
        for v in range(len(self.graph)):
            u = self.graph[v].head
            while u is not None:
                arrFlowAlloc.append((v+1, u.data, u.currentFlow))
                u = u.next
            
        return arrFlowAlloc


                

        






            

        

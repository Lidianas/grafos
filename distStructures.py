import numpy as np


class distVector:
    def __init__(self, n):
        self.distV = np.full(n, np.inf)
        self.visited = np.zeros(n)

    def getMinDist(self):
        currMinDist = float('inf')
        currMinVertex = -1
        for i in range(len(self.distV)):
            if self.distV[i] < currMinDist and self.visited[i] == 0:
                currMinVertex = i + 1
                currMinDist = self.distV[i]
        self.visited[currMinVertex - 1] = 1
        return currMinVertex

    def checkDist(self, v):
        return self.distV[v - 1]

    def updateDist(self, v, val):
        self.distV[v - 1] = val


class heapNode:
    def __init__(self, v, d):
        self.v = v
        self.dist = d


def leftVertexIndex(index):
    return int(2 * index + 1)


def parentIndex(index):
    return int((index - 1) / 2)


def rightVertexIndex(index):
    return int(2 * (index + 1))


class distHeap:
    def __init__(self, n):
        self.n = n
        self.heap = np.empty(self.n, dtype=object)
        self.mappingVector = np.full(self.n, -1)
        self.distVector = np.full(self.n, float("inf"))
        self.tail = -1
        for i in range(1, self.n+1):
            self.insert(i, float("inf"))

    def insert(self, v, d):
        newNode = heapNode(v, d)
        self.tail += 1
        self.heap[self.tail] = newNode
        self.mappingVector[v-1] = self.tail
        i = self.tail
        while i > 0 and self.heap[parentIndex(i)].dist > self.heap[i].dist:
            aux = self.heap[i]
            pai = self.heap[parentIndex(i)].v
            self.heap[i] = self.heap[parentIndex(i)]
            self.heap[parentIndex(i)] = aux
            self.mappingVector[v] = parentIndex(i)
            self.mappingVector[pai] = i
            i = parentIndex(i)

    def getMinDist(self):
        minVertex = self.heap[0].v
        self.heap[0] = self.heap[self.tail]
        self.mappingVector[self.heap[0].v - 1] = 0
        self.tail -= 1
        self.rebalance(0)
        return minVertex

    def rebalance(self, index):
        if not self.isLeaf(index) and self.isValid(index):
            if (self.getDist(self.heap[index]) > self.getDist(self.heap[leftVertexIndex(index)]) or
                    self.getDist(self.heap[index]) > self.getDist(self.heap[rightVertexIndex(index)])):

                if self.getDist(self.heap[leftVertexIndex(index)]) < self.getDist(self.heap[rightVertexIndex(index)]):
                    self.swap(index, leftVertexIndex(index))
                    self.rebalance(leftVertexIndex(index))

                else:
                    self.swap(index, rightVertexIndex(index))
                    self.rebalance(rightVertexIndex(index))

    def getDist(self, p):
        if isinstance(p, heapNode):
            return p.dist
        else:
            return float("inf")

    def isLeaf(self, index):
        return parentIndex(self.tail) < index <= self.tail

    def isValid(self, index):
        return index < self.tail

    def swap(self, heapIndex1, heapIndex2):
        if isinstance(self.heap[heapIndex1], heapNode) and self.isValid(heapIndex1):
            vertex1 = self.heap[heapIndex1].v
            self.mappingVector[vertex1 - 1] = heapIndex2

        if isinstance(self.heap[heapIndex2], heapNode) and self.isValid(heapIndex2):
            vertex2 = self.heap[heapIndex2].v
            self.mappingVector[vertex2 - 1] = heapIndex1

        aux = self.heap[heapIndex1]
        self.heap[heapIndex1] = self.heap[heapIndex2]
        self.heap[heapIndex2] = aux

    def checkDist(self, vertex):
        return self.distVector[vertex - 1]
    def updateDist(self, vertex, newDist):
        heapIndex = self.mappingVector[vertex - 1]
        if heapIndex != -1:
            # Atualize a distância do vértice
            self.distVector[vertex - 1] = newDist
            self.heap[heapIndex].dist = newDist

            # Verifique se é necessário fazer ajustes na heap
            parent = parentIndex(heapIndex)
            while heapIndex > 0 and self.heap[heapIndex].dist < self.heap[parent].dist:
                # Faça uma troca com o pai
                self.swap(heapIndex, parent)
                heapIndex = parent
                parent = parentIndex(heapIndex)
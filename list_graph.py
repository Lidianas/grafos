import numpy as np
import linked_list
import queue
import stack

class ListGraph():

    def __init__(self):
        self.n = 0
        self.m = 0
        self.myGraph = 0

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
        bfsQueue = queue.Queue()
        bfsVector[s - 1] = 1
        bfsQueue.enqueue(s)
        while not bfsQueue.isEmpty():
            v = bfsQueue.dequeue()
            neighbor = self.myGraph[v - 1].head
            while neighbor is not None:
                if bfsVector[neighbor.data - 1] == 0:
                    bfsVector[neighbor.data - 1] = 1
                    print("pai de", neighbor.data, v)
                    bfsQueue.enqueue(neighbor.data)
                neighbor = neighbor.next

    def dfs(self, s):
        dfsVector = np.zeros(self.n, dtype=object)
        dfsStack = stack.Stack()
        dfsStack.push(s)
        prev = s
        while not dfsStack.isEmpty():
            v = dfsStack.pop()
            if dfsVector[v - 1] == 0:
                dfsVector[v - 1] = 1
                print("pai de", v, prev)
                neighbor = self.myGraph[v - 1].head
                while neighbor is not None:
                    dfsStack.push(neighbor.data)
                    neighbor = neighbor.next
            prev = v

    def graphInfo(self, file):
        with open(file, 'w') as f:
            f.write(str(self.n)+'\n')
            f.write(str(self.m))

    def dist(u,v):
        pass
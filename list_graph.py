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
        bfsTree = np.zeros(self.n, dtype=object)
        bfsQueue = queue.Queue()
        bfsVector[s - 1] = 1
        bfsQueue.enqueue(s)
        while not bfsQueue.isEmpty():
            v = bfsQueue.dequeue()
            neighbor = self.myGraph[v - 1].head
            while neighbor is not None:
                if bfsVector[neighbor.data - 1] == 0:
                    bfsVector[neighbor.data - 1] = 1
                    bfsTree[neighbor.data-1] = v
                    print("pai de", neighbor.data, v)
                    bfsQueue.enqueue(neighbor.data)
                neighbor = neighbor.next
        return bfsTree

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

    def dist(self, u,v):
        tree = self.bfs(u)
        if tree[v] != 0:
            c = 1
            dad = tree[v-1]
            while c < self.n:
                if u == dad:
                    return c
                else: 
                    dad = tree[dad-1]
                    c+=1
        return "u and v are equal or there is no path between them"
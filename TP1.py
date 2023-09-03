import numpy as np

nameFile = "exemplo.txt"
global isMatrixType
global n
global m
n = 0  # Número de vértices
m = 0  # Número de arestas
isMatrixType = 0  # Representação escolhida ( 0 = lista, 1 = matriz)
myGraph = 0


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


class Queue:
    def __init__(self):
        self.itens = []

    def isEmpty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.itens.pop(0)
        else:
            raise IndexError("Empty queue")

    def size(self):
        return len(self.itens)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("The stack is empty")

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("The stack is empty")

    def size(self):
        return len(self.items)


def readGraph(i, file):
    if i == 0:
        global isMatrixType
        isMatrixType = 1
        return matrixGraph(file)
    else:
        return listGraph(file)


def matrixGraph(file):
    with open(file, 'r') as f:
        global n
        global m
        global myGraph
        n = int(f.readline())
        myGraph = np.zeros((n, n), dtype=int)
        for linha in f:
            m += 1
            i, j = map(int, linha.split())
            myGraph[i - 1][j - 1] = 1
            myGraph[j - 1][i - 1] = 1

    return myGraph


def listGraph(file):
    with open(file, 'r') as f:
        global n
        global m
        global myGraph
        n = int(f.readline())
        myGraph = np.empty(n, dtype=object)
        for i in range(n):
            myGraph[i] = LinkedList()
        for linha in f:
            m += 1
            i, j = map(int, linha.split())
            myGraph[i - 1].append(j)
            myGraph[j - 1].append(i)

    return myGraph


def BFS_Matrix(s):
    bfsVector = np.zeros(n, dtype=object)
    bfsQueue = Queue()
    bfsVector[s - 1] = 1
    bfsQueue.enqueue(s)
    while not bfsQueue.isEmpty():
        v = bfsQueue.dequeue()
        i = 1
        for isNeighbor in myGraph[v - 1]:
            if isNeighbor == 1:
                w = i
                if bfsVector[w - 1] == 0:
                    bfsVector[w - 1] = 1
                    print("pai de", w, v)
                    bfsQueue.enqueue(w)
            i += 1


def BFS_List(s):
    bfsVector = np.zeros(n, dtype=object)
    bfsQueue = Queue()
    bfsVector[s - 1] = 1
    bfsQueue.enqueue(s)
    while not bfsQueue.isEmpty():
        v = bfsQueue.dequeue()
        neighbor = myGraph[v - 1].head
        while neighbor is not None:
            if bfsVector[neighbor.data - 1] == 0:
                bfsVector[neighbor.data - 1] = 1
                print("pai de", neighbor.data, v)
                bfsQueue.enqueue(neighbor.data)
            neighbor = neighbor.next


def DFS_Matrix(s):
    dfsVector = np.zeros(n, dtype=object)
    dfsStack = Stack()
    dfsStack.push(s)
    prev = s
    while not dfsStack.isEmpty():
        v = dfsStack.pop()
        if dfsVector[v - 1] == 0:
            dfsVector[v - 1] = 1
            print("pai de", v, prev)
            i = 1
            for isNeighbor in myGraph[v - 1]:
                if isNeighbor == 1:
                    w = i
                    dfsStack.push(w)
                i += 1
        prev = v

def DFS_List(s):
    dfsVector = np.zeros(n, dtype=object)
    dfsStack = Stack()
    dfsStack.push(s)
    prev = s
    while not dfsStack.isEmpty():
        v = dfsStack.pop()
        if dfsVector[v - 1] == 0:
            dfsVector[v - 1] = 1
            print("pai de", v, prev)
            neighbor = myGraph[v - 1].head
            while neighbor is not None:
                dfsStack.push(neighbor.data)
                neighbor = neighbor.next
        prev = v

readGraph(1, nameFile)
DFS_List(1)

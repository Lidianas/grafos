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
        self.visited[currMinVertex-1] = 1
        return currMinVertex

    def checkDist(self, v):
        return self.distV[v - 1]

    def updateDist(self, v, val):
        self.distV[v - 1] = val


class heapNode:
    def __init__(self, v, dist):
        self.v = v
        self.dist = dist
        self.left = None
        self.right = None
        self.parent = None


class distHeap:
    def __init__(self, n):
        self.root = heapNode(1, float("inf"))
        self.n = n
        self.mappingVector = np.zeros(self.n, dtype=object)
        self.mappingVector[0] = self.root
        self.dist = np.full(n, np.inf)
        for i in range(2, self.n + 1):
            self.insert(i, float("inf"))

    def insert(self, v, dist):
        lastRight = self.root
        while lastRight.right is not None:
            lastRight = lastRight.right
        lastRight.right = heapNode(v, dist)
        lastRight.right.parent = lastRight
        self.mappingVector[v - 1] = lastRight.right
        self.rebalance(lastRight.right)

    def getMinDist(self):
        root = self.root.v
        lastRight = self.root
        while lastRight.right is not None:
            lastRight = lastRight.right
        self.root.v = lastRight.v
        self.root.dist = lastRight.dist
        if lastRight.parent:
            lastRight.parent.right = None
        self.rebalance(self.root)
        return root

    def rebalance(self, startNode):
        def swap_nodes(node1, node2):
            node1.v, node2.v = node2.v, node1.v
            node1.dist, node2.dist = node2.dist, node1.dist

        node = startNode

        while node.parent is not None:
            parent = node.parent
            if node.dist < parent.dist:
                swap_nodes(node, parent)
            else:
                break

            node = parent

        while node.left is not None:
            left_child = node.left
            right_child = node.right
            min_child = left_child

            if right_child is not None and right_child.dist < left_child.dist:
                min_child = right_child

            if node.dist > min_child.dist:
                swap_nodes(node, min_child)
                node = min_child
            else:
                break

    def updateDist(self, v, newDist):
        self.mappingVector[v - 1].dist = newDist
        self.rebalance(self.mappingVector[v - 1])
        self.dist[v-1] = newDist
    def checkDist(self, v):
        print(v)
        print(self.mappingVector[v-1].v)
        print(self.mappingVector[v-1].dist)
        print(self.dist[v-1])
        print("lol")
        return self.dist[v - 1]

    def printHeap(self):
        # Helper function for in-order traversal and printing
        def in_order_traversal(node):
            if node is not None:
                # Recursively visit left subtree
                in_order_traversal(node.left)
                # Print the current node
                print(f"Value: {node.v}, Distance: {node.dist}")
                # Recursively visit right subtree
                in_order_traversal(node.right)

        print("Heap Elements (Ordered by Distance):")
        in_order_traversal(self.root)

import numpy as np


class distVector:
    def __init__(self, n):
        self.distV = np.full(n, np.inf)
        self.distAux = np.full(n, np.inf)

    def getMinDist(self):
        currMin = float('inf')
        for i in range(len(self.distAux)):
            if self.distAux[i] < currMin:
                currMin = i
        self.distAux[currMin] = float('inf')
        return currMin+1

    def checkDist(self, v):
        return self.distV[v - 1]

    def updateDist(self, v, val):
        self.distV[v - 1] = val
        self.distAux[v - 1] = val


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
        for i in range(2, self.n + 1):
            self.insert(i, float("inf"))
        self.dist = distVector(self.n)
    def insert(self, v, dist):
        lastRight = self.root
        while lastRight.right is not None:
            lastRight = lastRight.right
        lastRight.right = heapNode(v, dist)
        lastRight.right.parent = lastRight
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
        def find_and_update(node, value, new_dist):
            if node is None:
                return
            if node.v == value:
                node.dist = new_dist
                self.rebalance(node)  # Rebalance the heap after updating the distance
                return
            find_and_update(node.left, value, new_dist)
            find_and_update(node.right, value, new_dist)

        find_and_update(self.root, v, newDist)
        self.dist.updateDist(v, newDist)

    def checkDist(self, v):
        return self.dist.checkDist(v)

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
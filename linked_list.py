import list_node
from list_node import ListNodeWithWeight, ListNodeDirectedWithWeight, ListNodeResidual

class LinkedList:
    """Implement a linked list"""

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = list_node.ListNode(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


class WeightedLinkedList:
    """Implement a linked list with nodes containing weight"""

    def __init__(self):
        self.head = None

    def append(self, data, peso):
        new_node = ListNodeWithWeight(data, peso)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class DirectedWeightedLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data, flowCapacity, currentFlow):
        new_node = ListNodeDirectedWithWeight(data, flowCapacity, currentFlow)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class ResidualLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data, capacity, isOriginal):
        new_node = ListNodeResidual(data, capacity, isOriginal)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
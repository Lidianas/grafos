import numpy as np
from list_graph import ListGraph
from linked_list import ResidualLinkedList


class ResidualGraph(ListGraph):

    def __init__(self, n):
        super().__init__()
        self.n = n
        self.graph = np.empty(self.n, dtype=object)
    
    def setResidualGraph(self, input_graph):
        print("residual graph set")
        reverseCapacity = 0
        for i in range(self.n):
            self.graph[i] = ResidualLinkedList()
        for u in range(self.n):
            neighbor = input_graph[u].head
            if neighbor is not None:
                print("origem ", u+1)
            while neighbor is not None:
                originalCapacity = neighbor.flowCapacity
                print("target", neighbor.data)
                if int(originalCapacity) != 0:
                    print("capacidade ", originalCapacity, "para par ",u+1,neighbor.data)
                    self.graph[u].append(neighbor.data, originalCapacity, True)
                    self.graph[neighbor.data - 1].append(u + 1, reverseCapacity, False)
                    neighbor = neighbor.next
        print("residual graph set end")

    def updateResidualGraph(self, input_graph):
        
        reverseCapacity = 0
        for i in range(self.n):
            self.graph[i] = ResidualLinkedList()
        for u in range(self.n):
            neighbor = input_graph[u].head
            while neighbor is not None:
                originalCapacity = neighbor.flowCapacity - neighbor.currentFlow
                #reverseCapacity = neighbor.currentFlow
                if originalCapacity != 0:
                    self.graph[u].append(neighbor.data, originalCapacity, True)
                    self.graph[neighbor.data - 1].append(u + 1, reverseCapacity, False)
                neighbor = neighbor.next


        
        

        

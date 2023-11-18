class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNodeWithWeight(ListNode):
    def __init__(self, data, peso):
        super().__init__(data)
        self.peso = peso

class ListNodeDirectedWithWeight(ListNode):
    def __init__(self, data, flowCapacity, currentFlow):
        super().__init__(data)
        self.flowCapacity = flowCapacity
        self.currentFlow = currentFlow

class ListNodeResidual(ListNode):
    def __init__(self, data, capacity, isOriginal):
        super().__init__(data)
        self.capacity = capacity
        self.isOriginal = isOriginal
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNodeWithWeight(ListNode):
    def __init__(self, data, peso):
        super().__init__(data)
        self.peso = peso

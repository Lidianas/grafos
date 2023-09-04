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
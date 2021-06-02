class Stack():
    def __init__(self):
        self.items = []

    def push(self, num):
        self.items.append(num)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
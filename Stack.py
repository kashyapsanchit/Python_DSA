class Stack():
    def __init__(self):
        self.items = []

    def push(self, num):
        self.items.append(num)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
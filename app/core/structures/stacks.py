

class Stack:
    def __init__(self, size) -> None:
        self.data = []
        self.size = size

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return self.data == [] or len(self.data) == 0
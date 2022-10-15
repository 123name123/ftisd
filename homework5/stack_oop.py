class Stack:
    def __init__(self):
        self.data_ = list()

    def size(self) -> int:
        return len(self.data_)

    def empty(self) -> int:
        return len(self.data_) == 0

    def top(self):
        if self.empty():
            return None
        return self.data_[-1]

    def push(self, val) -> None:
        self.data_.append(val)

    def pop(self):
        if self.empty():
            return None
        val = self.top()
        self.data_.pop()
        return val

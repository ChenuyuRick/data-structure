class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = None

    def push(self, x: int) -> None:
        if len(self.items) == 0:
            self.items.append(x)
            self.min = x
        elif x >= self.min:
            self.items.append(x)
        else:
            self.items.append(2*x - self.min)
            self.min = x
        

    def pop(self) -> None:
        if len(self.items) == 0:
            return None
        elif self.items[-1] >= self.min:
            return self.items.pop()
        else:
            min_item = self.min
            self.min = 2 * min_item - self.items.pop()
            return min_item
        

    def top(self) -> int:
        if len(self.items) == 0:
            return None
        elif self.items[-1] >= self.min:
            return self.items[-1]
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

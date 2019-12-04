# Time: O(1) We find the min by looking at the top of a stack.
# Space: O(n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        prev_min = self.getMin()

        if prev_min is None:
            self.min.append(x)
        else:
            self.min.append(min(prev_min, x))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
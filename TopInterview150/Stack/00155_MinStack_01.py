class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        pop_value = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == pop_value:
            self.min_stack.pop()
        return pop_value

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        # if self.min_stack:
        #     return self.min_stack[-1]
        # elif self.stack:
        #     return self.stack[-1]
        if not self.min_stack and self.stack:
            return self.stack[-1]
        return self.min_stack[-1]

class MinStack2:
    def __init__(self):
        self.stack = []
        self.MAX_VALUE = 2 ** 31 -1
        self.min_value = self.MAX_VALUE

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        pop_value = self.stack.pop()
        if self.min_value == pop_value:
            if self.stack:
                self.min_value = min(self.stack)
            else:
                self.min_value = self.MAX_VALUE
        return pop_value

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_value    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print("getMin(): ", obj.getMin())
# print("pop(): ", obj.pop())
# print("top(): ", obj.top())
# print("getMin(): ", obj.getMin())

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print("getMin(): ", obj.getMin())
print("pop(): ", obj.pop())
print("getMin(): ", obj.getMin())

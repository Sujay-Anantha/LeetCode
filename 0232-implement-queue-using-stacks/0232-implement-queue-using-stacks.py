class MyQueue:

    def __init__(self):
        self.addStack, self.popStack = [], []

    def push(self, x: int) -> None:
        while self.popStack:
            self.addStack.append(self.popStack.pop())
        self.addStack.append(x)

    def pop(self) -> int:
        while self.addStack:
            self.popStack.append(self.addStack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        return self.popStack[-1] if self.popStack else self.addStack[0]

    def empty(self) -> bool:
        return True if not self.addStack and not self.popStack else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
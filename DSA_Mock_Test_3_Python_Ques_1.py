class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

stack = Stack()

print(stack.isEmpty())  

stack.push(1) # Pussing 1 to the Stack
stack.push(2) # then 2
stack.push(3) # then 3

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.isEmpty())  # False
print(stack.pop())  # 1
print(stack.isEmpty())  # True

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()
print(queue.isEmpty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # 1
print(queue.dequeue())  # 2

print(queue.isEmpty())  # False

print(queue.dequeue())  # 3
print(queue.isEmpty())  # True

class CircularQueue:
    def __init__(self):
        self.queue = {}
        self.max_length = 5
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if len(self.queue) == self.max_length:
            del self.queue[self.front]
            self.front = (self.front + 1) % self.max_length
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_length

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
            return
        idx = self.front
        print("Circular Queue:", end=" ")
        for _ in range(len(self.queue)):
            print(self.queue[idx], end=" ")
            idx = (idx + 1) % self.max_length
        print()



cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  

cq.enqueue(6)  
cq.display()  

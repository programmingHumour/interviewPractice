class QueueUsingStacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return  self.stack2.pop()

q = QueueUsingStacks()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.stack1)
print(q.dequeue())

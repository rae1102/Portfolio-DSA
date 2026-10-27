class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = new_node
            self.next = None
        elif self.front:
            new_node = self.rear
            self.rear.next = None

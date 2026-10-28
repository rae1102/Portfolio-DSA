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
            self.rear = self.front
        elif self.front:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        if self.front == None:

            return None
        else:
            dequeued_node = self.front
            self.front = self.front.next
            dequeued_node.next = None
            if self.front == None:
                self.rear = None
            return dequeued_node.data

    def get_values(self):
        values = []
        current_node = self.front
        while current_node:
            values.append(current_node.data)
            current_node = current_node.next
        return values

    def peek(self):
        if self.front:
            return self.front.data
        else:
            return None
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(4)
    q.dequeue()
    print(q.get_values())
    print(q.peek())
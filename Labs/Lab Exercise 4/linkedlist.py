# Lab exercies 3: Linked List - starter file

# Keep every name exactly as written. A renamed class or method counts as a
# missing answer, even if the code inside it is correct.

# Put your own experiments inside the `if __name__ == "__main__":` block at the
# bottom. Code at the top level of this file runs when your work is marked, so
# a stray print() or input() up there will show up in your feedback.




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def get_values(self):
        values = []
        current_node = self.head

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values

    # TODO a: remove the FIRST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_beginning(self):
        
        if not self.head:
            return None
        elif self.head == self.tail:
                removed_head_data = self.head.data
                self.head = None
                self.tail = None
                return removed_head_data
                    
        elif self.head:
            removed_head_data = self.head.data
            self.head = self.head.next
            return removed_head_data
        


    # TODO b: remove the LAST node and return its data (not the Node).
    # If the list is empty, return None.
   
    def remove_at_end(self):
        current_node = self.head

        if not self.head:
            return None
        elif self.head == self.tail:
            removed_node_data = self.tail.data
            self.head = None
            self.tail = None
            return removed_node_data
        else:
            while current_node:
                removed_node_data = self.tail.data
                if current_node.next == self.tail:
                    self.tail = current_node
                    current_node.next = None
                    return removed_node_data
                current_node = current_node.next

    # TODO c: remove the first node holding `data` and return its data.
    # If no node holds `data`, return None and leave the list unchanged.
    def remove_at(self, data):
        if not self.head:
            return None

        if self.head.data == data:
            return self.remove_beginning()

        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == data:
                removed_node_data = current_node.data
                previous_node.next = current_node.next

                if current_node == self.tail:
                    self.tail = previous_node

                return removed_node_data

            previous_node = current_node
            current_node = current_node.next

        return None

    # TODO d: insert a new node holding `data` right after the first node
    # holding `nodedata`.
    # If no node holds `nodedata`, return None and leave the list unchanged.
    def insert_after(self, nodedata, data):
        if not self.head:
            return None
        else:
            current_node = self.head
            while current_node:
                if current_node.data == nodedata:
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    if current_node == self.tail:
                        self.tail = new_node
                    break 
                current_node = current_node.next
            return None




from Node import Node


class LinkedList:

    def __init__(self):
        self.head = Node()
        self.last = self.head
        self.size = 1

    def get_head(self):
        return self.head

    def __len__(self):
        return self.size

    def get_elem(self, index):
        temp = self.head
        for i in range(self.size):
            if i == index:
                return temp
            temp = temp.get_next()

    def get_index(self, node):
        temp = self.head
        for i in range(self.size):
            if node.get_val() == temp.get_val():
                return i
            temp = temp.get_next()

    def insert(self, node):
        self.last.set_next(node)
        self.last = node
        self.size += 1

    def insert_at_head(self, node):
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def remove(self, node):
        temp = self.head
        prev = self.head
        prev.set_next(self.head)
        for i in range(self.size):
            if temp.get_val() == node.get_val():
                if i == 0:
                    self.head = self.head.get_next()
                    temp.next = None
                else:
                    prev.set_next(temp.get_next())
                    temp.set_next(None)
            prev = temp
            temp = temp.get_next()
        self.size -= 1

class Node:

    def __init__(self):
        self.next = None
        self.value = None

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

    def set_next(self, nextnode):
        self.next = nextnode

    def get_next(self):
        return self.next

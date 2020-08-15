class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLL(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        start = self.head
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            if self.tail is None:
                self.tail = self.head
            else:
                self.head = Node(data)
                self.head.next = start
                start.previous = self.head

    def display(self):
        if self.head is None:
            print('list is empty')
        else:
            start = self.head
            while start:
                print(start.data)
                start = start.next

    def display_rev(self):
        if self.head is None:
            print('list is empty')
        else:
            while self.tail:
                print(self.tail.data)
                self.tail = self.tail.previous

    
        

class Node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
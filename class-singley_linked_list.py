class Node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def inserAtEnd(self, value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def inserAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def inserInMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):
            if (t1.info == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def printLL(self):
        t1 = self.head
        while (t1 != None):
            print(t1.info)
            t1 = t1.next
        print()  # This will print a newline at the end

obj = SinglyLinkedList()
obj.inserAtEnd(10)
obj.inserAtEnd(20)
obj.inserAtEnd(30)
obj.inserAtBeg(5)
obj.inserInMid(15, 20) 
obj.printLL()  # Expected output: 5 10 15 20 30
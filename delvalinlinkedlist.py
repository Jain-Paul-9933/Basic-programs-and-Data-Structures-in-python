class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.tail = None
        self.head = None

    def display(self):
        if self.head is None:
            print("Liked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
        print()

    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def Del(self, target):
        if self.head.data == target:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        else:
            temp = self.head.next
            prev = self.head
            while temp.next:
                if temp.data == target and temp != self.tail:
                    prev.next = temp.next
                temp = temp.next
                prev = prev.next
            if target == temp.data:
                prev.next = None
                prev = self.tail


sll = SLL()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)
sll.insert(50)
sll.insert(60)
sll.display()
sll.Del(60)
sll.display()

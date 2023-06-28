class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
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

    def insert_beg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_end(self, data):
        newnode = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def insert_pos(self, pos, data):
        newnode = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        newnode.data = data
        newnode.next = temp.next
        temp.next = newnode

    def del_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def del_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def del_pos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None


sll = SLL()
node1 = Node(10)
sll.head = node1
node2 = Node(20)
node1.next = node2
node3 = Node(30)
node2.next = node3
node4 = Node(40)
node3.next = node4
sll.display()
sll.insert_beg(50)
sll.insert_beg(60)
sll.display()
sll.insert_end(70)
sll.insert_end(80)
sll.display()
sll.insert_pos(3, 15)
sll.insert_pos(5, 25)
sll.display()
sll.del_beg()
sll.display()
sll.del_end()
sll.display()
sll.del_pos(5)
sll.display()

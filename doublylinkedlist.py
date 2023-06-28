class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty Double Linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
        print()

    def insertbeg(self, data):
        newnode = Node(data)
        temp = self.head
        temp.prev = newnode
        newnode.next = temp
        self.head = newnode

    def insertend(self, data):
        newnode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        newnode.prev = temp
        temp.next = newnode

    def insertpos(self, pos, data):
        newnode = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        newnode.prev = temp
        newnode.next = temp.next
        temp.next = newnode
        temp.next.prev = newnode

    def delbeg(self):

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delend(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        temp.prev = None
        before.next = None

    def delpos(self, pos):
        temp = self.head.next
        before = self.head
        for i in range(1, pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None


dll = DLL()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)
dll.head = node1
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node6.next = node7
node7.prev = node6
dll.display()
dll.insertbeg(5)
dll.insertbeg(15)
dll.display()
dll.insertend(25)
dll.insertend(35)
dll.display()
dll.insertpos(3, 45)
dll.insertpos(6, 55)
dll.display()
dll.delbeg()
dll.display()
dll.delend()
dll.display()
dll.delpos(6)
dll.display()

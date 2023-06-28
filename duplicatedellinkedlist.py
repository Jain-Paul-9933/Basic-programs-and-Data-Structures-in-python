class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
        print()

    def insert_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
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

    def duplicatedel(self):
        temp1 = self.head
        while temp1:
            count = 0
            target = temp1.data
            temp2 = self.head
            while temp2:
                if temp2.data == target and count > 0:
                    temp2.data = -1
                elif temp2.data == target:
                    count += 1
                temp2 = temp2.next
            temp1 = temp1.next
            sll.Del(-1)


sll = SLL()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(20)
sll.insert_end(20)
sll.insert_end(50)
sll.insert_end(20)
sll.insert_end(70)
sll.insert_end(20)
sll.insert_end(80)
sll.insert_end(20)
sll.insert_end(90)
sll.insert_end(20)
sll.insert_end(100)
sll.display()
sll.duplicatedel()
sll.display()

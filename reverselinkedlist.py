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

    def reverse(self):
        prev = None
        current = self.head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insert_after(self, target, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            while temp:
                if temp.data == target:
                    newnode.next = temp.next
                    temp.next = newnode
                self.tail = newnode
                temp = temp.next


sll = SLL()
sll.insert_after(5, 10)
sll.insert_after(10, 20)
sll.insert_after(20, 30)
sll.insert_after(30, 40)
sll.insert_after(40, 50)
sll.insert_after(50, 60)
sll.display()
sll.reverse()
sll.display()

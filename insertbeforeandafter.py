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

    # def insert_after(self, target, data):
    #     newnode = Node(data)
    #     if self.head is None:
    #         self.head = newnode
    #         self.tail = newnode
    #     else:
    #         temp = self.head
    #         while temp:
    #             if temp.data == target:
    #                 newnode.next = temp.next
    #                 temp.next = newnode
    #             self.tail = newnode
    #             temp = temp.next
    def insert_before(self, target, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if self.head.data == target:
                newnode.next = self.head
                self.head = newnode
            else:
                temp = self.head.next
                prev = self.head
                while temp:
                    if temp.data == target:
                        newnode.next = temp
                        prev.next = newnode
                    self.tail = temp
                    temp = temp.next


sll = SLL()
# sll.insert_after(5, 10)
# sll.insert_after(10, 20)
# sll.insert_after(10, 30)
sll.insert_before(5, 10)
sll. insert_before(10, 20)
sll.insert_before(10, 30)
sll.insert_before(20, 50)
sll.display()

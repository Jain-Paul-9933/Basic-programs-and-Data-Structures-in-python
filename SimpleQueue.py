class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def Enqueue(self, data):
        newnode = Node(data)
        print(f"Entered {newnode.data}")
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def Dequeue(self):
        if self.front is None:
            self.rear = None
            print("No elements to delete")
        else:
            print(f"Removed {self.front.data}")
            self.front = self.front.next

    def Display(self):
        if self.front is None:
            print("Empty Queue")
        else:
            current = self.front
            while current:
                print(f" | {current.data}", end="")
                current = current.next


queue = Queue()
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
queue.Enqueue(50)
# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()
# queue.Dequeue()
queue.Display()
# ...

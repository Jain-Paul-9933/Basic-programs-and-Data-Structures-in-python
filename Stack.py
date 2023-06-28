class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def Push(self, data):
        newnode = Node(data)
        print(f"Pushed {newnode.data}")
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def Pop(self):
        if self.top is None:
            print("Stack has no elements to pop")
        else:
            print(f"Popped {self.top.data}")
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Empty Stack")
        else:
            current = self.top
            while current:
                print("[", current.data, "]")
                current = current.next


stack = Stack()
stack.Push(10)
stack.Push(20)
stack.Push(30)
stack.Push(40)
stack.Push(50)
stack.Pop()
# stack.Pop()
# stack.Pop()
# stack.Pop()
# stack.Pop()
# stack.Pop()
stack.display()
# ...

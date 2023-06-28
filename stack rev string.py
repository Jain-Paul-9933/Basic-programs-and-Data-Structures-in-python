class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def Push(self, data):
        newnode = Node(data)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def Pop(self):
        if self.top is None:
            print("Stack has no elements to pop")
        else:
            temp = self.top.data
            self.top = self.top.next
        return temp

    def stringrev(self, string, len):
        for i in string:
            stack.Push(i)
        string = ""
        for i in range(len):
            string += stack.Pop()
        print(string)


stack = Stack()
string = "We will conquere COVID-19"
len = len(string)
stack.stringrev(string, len)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(self):
    if self:
        inorder(self.left)
        print(str(self.data)+"-->", end="")
        inorder(self.right)


def preorder(self):
    if self:
        print(str(self.data)+"-->", end=" ")
        preorder(self.left)
        preorder(self.right)


def postorder(self):
    if self:
        postorder(self.left)
        postorder(self.right)
        print(str(self.data)+"-->", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)
print()
preorder(root)
print()
postorder(root)

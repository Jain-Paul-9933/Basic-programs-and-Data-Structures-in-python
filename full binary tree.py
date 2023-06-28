class Node:
    def __init__(self, item):
        self.item = item
        self.leftchild = None
        self.rightchild = None


def isFullTree(self):
    if self is None:
        return True
    if self.leftchild is None and self.rightchild is None:
        return True
    if self.leftchild is not None and self.rightchild is not None:
        return isFullTree(self.leftchild) and isFullTree(self.rightchild)
    return False


root = Node(1)
root.leftchild = Node(2)
root.rightchild = Node(3)
root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)
root.leftchild.rightchild.leftchild = Node(6)
root.leftchild.rightchild.rightchild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")

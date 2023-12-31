class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def count_nodes(root):
    if root is None:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)


def is_complete(root, index, numberNodes):
    if root is None:
        return True
    if index >= numberNodes:
        return False
    return is_complete(root.left, 2 * index+1, numberNodes) and is_complete(root.right, 2*index+2, numberNodes)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
node_count = count_nodes(root)
index = 0
if is_complete(root, index, node_count):
    print("The tree is a complete binary tree ")
else:
    print("The tree is not a complete binary tree")

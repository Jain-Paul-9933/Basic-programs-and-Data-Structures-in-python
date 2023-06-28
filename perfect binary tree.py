class newNode:
    def __init__(self, data):
        self.data = data
        self.right = self.right = None


def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d


def is_perfect(root, d, level=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return d == level+1
    if root.left is None and root.right is None:
        return False
    return is_perfect(root.left, d, level+1) and is_perfect(root.right, d, level+1)

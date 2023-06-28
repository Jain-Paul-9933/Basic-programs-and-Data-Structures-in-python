class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def isBST(root, left, right):
    # Base case, if root is NULL
    if (root == None):
        return 1

    # if left is not null then if left is greater than root return false
    if (left != None and root.data <= left.data):
        return 0
       # if right is not null then if right is smaller than root return false
    if (right != None and root.data >= right.data):
        return 0

       # check recursively for left and right subtrees
    return isBST(root.left, left, root) and isBST(root.right, root, right)


def main():

    # Creating a binary tree
    root = Node(10)
    root.left = Node(4)
    root.right = Node(16)
    root.left.left = Node(2)
    root.left.right = Node(5)

    if (isBST(root, None, None)):
        print("Binary Tree is BST")
    else:
        print("Binary Tree is not Bst")

    return 0


# execute main
main()

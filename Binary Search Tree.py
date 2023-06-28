class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self, data):

        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
# to only append the prime numbers of the tree
        count = 0
        for i in range(2, self.data):
            if self.data % i == 0:
                count += 1
        if count == 0:
            elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        print(elements)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        print(elements)
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def minValueNode(self):
        current = self
        while (current.left is not None):
            current = current.left
        return current

    def deletion(self, data):
        if self is None:
            return self
        if data < self.data:
            self.left = self.right.deletion(self.left, data)
        elif data > self.data:
            self.right = self.right.deletion(self.right, data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.minValueNode(self.right)
            self.key = temp.data
            self.right = self.right.deletion(self.right, temp.data)
        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.addchild(elements[i])
    return root


if __name__ == '__main__':
    numbers = [15, 12, 27, 7, 14, 20, 88, 23]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.post_order_traversal())
    # print(numbers_tree.search(5))
    # numbers_tree.deletion(27)
    # print(numbers_tree.in_order_traversal())

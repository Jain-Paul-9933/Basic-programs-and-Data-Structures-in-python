class TreeNode:
    def __init__(self, data):
        self.data = []
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


# def build_product_tree():
#     root = TreeNode("Electronics")
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Lenovo"))
#     laptop.add_child(TreeNode("HP"))
#     laptop.add_child(TreeNode("DELL"))
#     mobile = TreeNode("Mobile")
#     mobile.add_child(TreeNode("Apple"))
#     mobile.add_child(TreeNode("Google"))
#     mobile.add_child(TreeNode("Sammsung"))
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Sony"))
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("Panasonic"))
#     root.add_child(laptop)
#     root.add_child(mobile)
#     root.add_child(tv)
#     return root


# if __name__ == '__main__':
#     root = build_product_tree()
#     root.print_tree()
class Management_Hierarchy(TreeNode):
    def __init__(self, name, designation):
        super().__init__()
        self.name = name
        self.designation = designation


def build_hierarchy_tree():
    nilupul = Management_Hierarchy("Nilupal", "CEO")
    chinmay = Management_Hierarchy("Chinmay", "CTO")
    vishwa = Management_Hierarchy("Vishwa", "Infrastructure Head")
    dhaval = Management_Hierarchy("Dhaval", "Cloud Manager")
    abijit = Management_Hierarchy("Abhijit", "App Manager")
    aamir = Management_Hierarchy("Aamir", "Application Head")
    gels = Management_Hierarchy("Gels", "HR Head")
    peter = Management_Hierarchy("Peter", "Recruitment Manager")
    waqas = Management_Hierarchy("Waqas", "Policy Manager")
    vishwa.add_child(dhaval)
    vishwa.add_child(abijit)
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)
    gels.add_child(peter)
    gels.add_child(waqas)
    nilupul.add_child(chinmay)
    nilupul.add_child(gels)
    return nilupul


if __name__ == '__main__':
    root = build_hierarchy_tree()
    root.print_tree

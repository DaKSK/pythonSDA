class TreeNode:
    def __init__(self, name, size=0, is_directory=True):
        self.data = {"name": name, "size": size, "directory": is_directory}
        self.parent = None
        self.children = []

    def __repr__(self):
        return self.data["name"]

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        seeker = self.parent
        while seeker:
            level += 1
            seeker = seeker.parent
        return level

    def visualize_tree(self):
        prefix = "  " * self.get_level()
        if self.data["directory"]:
            print(f"{prefix}|__ {self} -dir")
        else:
            print(f"{prefix}|__ {self} -file size:{self.data['size']} bytes")
        if self.children:
            for child in self.children:
                child.visualize_tree()

    def get_size(self):
        total_size = 0
        if not self.children:
            return self.data["size"]
        elif self.children:
            for child in self.children:
                total_size += self.data["size"] + child.get_size()
            return total_size


def build_tree():
    # Building the tree from example5.png
    # Creating the root and it's 2 children
    root = TreeNode("Home")
    jakub = TreeNode("jakub")
    var = TreeNode("var")
    root.add_child(jakub)
    root.add_child(var)

    # Adding children to root.children
    jakub.add_child(TreeNode(".bashrc", size=50, is_directory=False))
    jakub.add_child(TreeNode(".vimrc", size=100, is_directory=False))
    jakub.add_child(TreeNode("blob", size=1023, is_directory=False))
    # Creating the grandchild of root
    log = TreeNode("log")
    var.add_child(log)
    # Adding a grandchild to the child of root ("var")
    log.add_child(TreeNode("sys.log", size=10, is_directory=False))

    return root


if __name__ == "__main__":
    dirs = build_tree()
    print(dirs.get_size(), "bytes")
    dirs.visualize_tree()


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
        if not self.children:
            return self.data["size"]
        else:
            return sum(self.data["size"] + child.get_size() for child in self.children)


def build_tree():
    # Building the tree from example5.png
    # Creating the root node and it's 2 children nodes
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
    dirs.visualize_tree()
    print("Home folder size is", dirs.get_size(), "bytes")
    jakub_node_index = dirs.children.index("jakub")
    jakub_folder = dirs.children[jakub_node_index]
    print("home/jakub/ size is", jakub_folder.get_size())



class TreeNode:
    '''
    Data moves down from node to node
        root: A node which has no parent. One per tree.
        parent: A node which references other nodes.
        child: Nodes referenced by other nodes.
        sibling: Nodes which have the same parent.
        leaf: Nodes which have no children.
        level: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.
    '''

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [
            child for child in self.children if child is not child_node]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# first_node = Node("No 1")
# second_node = Node("No 2")
# third_node = Node("No 3")

# first_node.set_next_node(second_node)
# second_node.set_next_node(third_node)

# second_nodes_data = second_node.get_value()
# third_nodes_data = second_node.get_next_node().get_value()

# print(first_node.get_value())
# print(second_nodes_data)
# print(third_nodes_data)

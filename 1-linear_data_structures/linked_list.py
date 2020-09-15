from node import Node


class LinkedList:
    '''
    Are comprised of nodes
    The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
    Can be unidirectional or bidirectional
    Are a basic data structure, and form the basis for many other data structures
    Have a single head node, which serves as the first node in the list
    Require some maintenance in order to add or remove nodes
    The methods we used are an example and depend on the exact use case and/or programming language being used
    '''

    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                if current_node.get_next_node():
                    string_list += str(current_node.get_value()) + " => "
                else:
                    string_list += str(current_node.get_value())
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


# list = LinkedList("node4")
# list.insert_beginning("node3")
# list.insert_beginning("node2")
# list.insert_beginning("node1")
# print(list.stringify_list())

# list.remove_node("node3")
# print(list.stringify_list())

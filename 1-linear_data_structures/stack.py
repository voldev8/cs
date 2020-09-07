from node import Node


class Stack:
    def __init__(self, limit=100):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print(f"Adding {value} to the stack!")
        else:
            print(f"No room for {value}!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Removing " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


# new_stack = Stack(6)

# new_stack.push("#1")
# new_stack.push("#2")
# new_stack.push("#3")
# new_stack.push("#4")
# new_stack.push("#5")
# new_stack.push("#6")

# # Stack overflow
# new_stack.push("#7")

# print("Top of the stack " + new_stack.peek())
# new_stack.pop()
# new_stack.pop()
# new_stack.pop()
# new_stack.pop()
# new_stack.pop()
# new_stack.pop()

# new_stack.pop()

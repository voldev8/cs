
class MinHeap:
    '''
    The root is the minimum value of the dataset.
    Every child’s value is greater than its parent.
    index starting with 1 (first element in list None)
    Adding an Element: Heapify Up if child is smaller then parent they swap
    Removing an Element: Heapify Down if before removing root we swap with the rightmost value and heapifying down the value
    '''

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    ###Idx helper methods ###
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count
    #####

    # retrieve min
    def retrieve_min(self):
        if self.count == 0:
            print('No items')
            return None
        # a sentinel element occupies index 0
        min = self.heap_list[1]
        print(f"Removing: {min} from {self.heap_list}")

        # swapping first and last element
        self.heap_list[1], self.heap_list[-1] = self.heap_list[-1], self.heap_list[1]

        # removing min element which is the last element after the swap
        self.heap_list.pop()
        self.count -= 1
        print(f"Last element moved to first: {self.heap_list}")
        self.heapify_down()
        return min

    def heapify_down(self):
        # initial value of our out of place element is one since we swapped it
        idx = 1
        # while there's at least one child present:
        while self.child_present(idx):
            print("Heapifying down!")
            # get the smallest child's index
            smaller_child_idx = self.get_smaller_child_idx(idx)
            # compare the smallest child with our element
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                # if our element is larger, swap with child
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            # regardless, set our element index to be the child
            idx = smaller_child_idx
        print(f"Heap Restored! {self.heap_list}")

    def get_smaller_child_idx(self, idx):
        # check if we have a right child
        if self.right_child_idx(idx) > self.count:
            # if we don't, return the left child index
            print("There is only a left child")
            return self.left_child_idx(idx)
        # if we do...
        else:
            # return the index of the smaller child
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller")
                return self.right_child_idx(idx)

    # Adding element
    def add(self, element):
        print(f'Adding {element} to {self.heap_list}')
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    # Heapify Up
    def heapify_up(self):
        print('Restoring the heap property')
        # last element
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                print("swapping {0} with {1}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))

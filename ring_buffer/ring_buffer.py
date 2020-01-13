from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.insertNext = None

    def append(self, item):
        # a b c d e
        if self.storage.length >= self.capacity:
            if self.insertNext is None:
                #self.storage.remove_from_head()
                self.storage.head.value = item
                self.insertNext = self.storage.head.next
            else:
                self.insertNext.value = item
                self.insertNext = self.insertNext.next
            #self.storage.move_to_front(self.storage.head.next)
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        currentNode = self.storage.head
        while True:
            list_buffer_contents.append(currentNode.value)
            if currentNode.next is not self.storage.head and currentNode.next is not None:
                currentNode = currentNode.next
            else:
                break

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

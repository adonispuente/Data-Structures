"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

#Using and array


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) < 1:
#             return None
#         else:
#             value = self.storage.pop(0)
#             return value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    """
    Data:
    1. A reference to the Head Node
    2. A ref to the tail node

    Behavior/Methods
    1.Add to tail (Add a new node to the Node referenced by the Tail)
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update head pointer)
    3. Remove Head
    4. Remove Tail
    5.Check if an item is in there(Contains)
    6.Get maximum
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # Empty LL
        if self.head is None:
            return None
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()
        # More than one item
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        current = self.head
        if self.head is None:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.count = 0

    def __len__(self):
        return self.count

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.count += 1

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            self.count -= 1
            removed_item = self.storage.remove_head()
            return removed_item

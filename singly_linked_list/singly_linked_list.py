class Node:
    #     "Stores two peices of data, thevalue, and the pointer to the ext_node

    #     Data:
    #     Stores two pieces of data:
    #     1. The Value
    #     2. the next Node

    # Methods/behaviors/operations
    # 1. get Value
    # 2. set value
    # 3. get next
    # 4. set next
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


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
    5.Check if an item is in there(COntains)
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

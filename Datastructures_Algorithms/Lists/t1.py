class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = self._tail = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop(self):
        if self._head is None:
            return None

        previous_node = None
        current_node = self._head

        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        if self._head == current_node:
            self._head = self._tail = None
        else:
            previous_node.next = None
            self._tail = previous_node

        value = current_node.data
        del current_node
        self._size -= 1
        return value
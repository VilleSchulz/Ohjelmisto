class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, ):
        self._size = 0
        self._front = None
        self._rear = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0


    def enqueue(self, data):
        new_node = ListNode(data)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            new_node.prev = self._rear
            self._rear = new_node

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self._front.data
        if self._front.prev:
            self._front = self._front.prev
        else:
            self._rear = None

        self._size -= 1
        return removed_data

    def __repr__(self):
        values = []
        current = self._front

        while current:
            values.append(current.data)
            current = current.next
        plural = "" if len(values) == 1 else "s"
        return f"<Queue ({self._size} element{plural}): [{', '.join(values)}]>"

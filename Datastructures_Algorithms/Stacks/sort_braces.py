class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._top is None

    def pop(self):
        if self._top is None:
            return None
        removed_node = self._top
        self._top = removed_node.next
        self._size -= 1
        return removed_node.data

    def push(self, data):
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1


def check_balance(text):
    stack = Stack()
    result = 0
    pairs = {"}":"{", ")":"(", "]": "["}

    for index, char in enumerate(text):
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return "Match error at position " + str(index)
            popped_char = stack.pop()
            if popped_char != pairs[char]:
                return "Match error at position " + str(index)
            else:
                result += 1
    return f"Ok - {result}" if stack.is_empty() else "Match error at position " + str(index)


text = "a(b)c(([d][e{f}])g)("
print(check_balance(text))

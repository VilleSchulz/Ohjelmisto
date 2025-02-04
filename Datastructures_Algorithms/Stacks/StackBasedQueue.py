class StackBasedQueue():
    def __init__(self):
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0

    # YOUR CODE HERE

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack][::-1]
        values.extend([c for c in self._OutboundStack])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.append(data)
        self._size += 1



    def dequeue(self):
        """Poistaa ja palauttaa jonon ensimmäisen alkion (FIFO)."""
        if not self._OutboundStack:
            # Siirretään kaikki inbound-pinosta outbound-pinoon käännetyssä järjestyksessä
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())

        if not self._OutboundStack:
            return None  # Jono on tyhjä

        self._size -= 1
        return self._OutboundStack.pop()


queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
print(queue)
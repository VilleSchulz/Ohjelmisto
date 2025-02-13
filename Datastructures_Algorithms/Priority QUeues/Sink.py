class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index - 1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order.
        """
        index = 0

        # Aloitetaan juuresta
        while index < self._size:
            child1_index = index * 2 + 1
            child2_index = index * 2 + 2
            smallest = index
            # Tarkistetaan onko vasenlapsi olemassa ja onko pienempi kuin nykyinen solmu
            if child1_index < self._size and self._heap[child1_index] < self._heap[smallest]:
                smallest = child1_index
            # Tarkistetaan, että oikea lapsi on olemassa ja on pienempi kuin nykyinen tai vasen lapsi
            if child2_index < self._size and self._heap[child2_index] < self._heap[smallest]:
                smallest = child2_index
            # Jos pienin lapsi on pienempi kuin nykyinen solmu, vaihdetaan paikkoja
            if smallest != index:
                self._heap[smallest], self._heap[index] = self._heap[index], self._heap[smallest]
                index = smallest
            else:
                break
    # Esimerkki:


h = Heap()
h._heap = [9, 8]
h._size = 2
h._sink()
print(h._heap)

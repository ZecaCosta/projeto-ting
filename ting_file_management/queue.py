class Queue:
    FIFO = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(self.FIFO)
        return None

    def search(self, index):
        smallest = 0
        highier = self.__len__() - 1
        _type = type(index)

        if _type != int or smallest > index < highier:
            raise IndexError
        return self._data[index]

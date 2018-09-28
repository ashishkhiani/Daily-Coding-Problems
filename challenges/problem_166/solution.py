class Iterator(object):

    def __init__(self, _input):
        self._input = _input
        self.pointers = []

        for i in reversed(range(len(_input))):
            for j in reversed(range(len(_input[i]))):
                self.pointers.append((i, j))

    def next(self):
        if len(self.pointers) == 0:
            raise StopIteration("There are no more elements in the list.")

        pointer = self.pointers.pop()
        return self._input[pointer[0]][pointer[1]]

    def has_next(self):
        return len(self.pointers) > 0



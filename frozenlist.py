from collections import Collection

class ReadOnlyList(Collection):
    '''Don't forget the docstrings'''

    def __init__(self, *args, **kwargs):
        self._l = list(*args, **kwargs)
        self._index = -1

    def __contains__(self, key):
        return self._l.__contains__(key)

    def __getitem__(self, key):
        return self._l[key]

    def __iter__(self):
        return self

    def __len__(self):
        return len(self._l)

    def __next__(self):
        self._index += 1
        if self._index >= len(self):
            self._index = -1
            raise StopIteration
        return self._l[self._index]
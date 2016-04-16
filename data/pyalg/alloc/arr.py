#coding:UTF-8

import sys
sys.path.append(r'..')
from ..object import *

class Array(Object):
    def __init__(self, maxlen = 0):
        assert maxlen >= 0
        super(Array, self).__init__()
        self._items = [None for i in xrange(maxlen)]

    def _compareTo(self, other):
        raise NotImplemented

    @property
    def data(self):
        return self._items

    def __getitem__(self, pos):
        if pos >= len(self._items):
            raise IndexError('out of range!')
        return self._items[pos]

    def __setitem__(self, pos, v):
        if pos >= len(self._items):
            raise IndexError('out of range!')
        self._items[pos] = v

    def __copy__(self):
        result = self.__class__((len(self._items)))
        for i, item in enumerate(self._items):
            result._items[i] = item
        return result

    def __iter__(self): return self

    def next(self):
        len_items = len(self._items)
        pos = 0
        try:
            while True:
                yield self._items[pos]
                pos += 1
        except:
            raise StopIteration

    def __reversed__(self):
        try:
            pos = len(self._items) - 1
            while pos >= 0:
                yield self._items[pos]
                pos -= 1
        except:
            raise StopIteration

    def __len__(self):
        return len(self._items)

    def  __str__(self):
        return "[{0}]".format(", ".join(str(i) for i in self._items))

if __name__ == '__main__':
    array = Array(10)
    array[1] = 100
    print array

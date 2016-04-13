#coding:UTF-8

from pyalg.object import *

class Vector(Object):
    def __init__(self):
        super(Vector, self).__init__()
        self._items = []

    def _compareTo(self, other):
        raise NotImplemented

    @property
    def data(self):
        return self._items

    def push_back(self, item):
        self._items.append(item)

    def pop_back(self):
        len_items = len(self._items)
        if len_items == 0:
            return None
        return self._items.pop()

    def clear(self):
        self._items = []

    def resize(self, size):
        len_items = len(self._items)
        if size <= len_items:
            self._items = self._items[:size]
        else:
            self._items.extend([None for i in xrange(size - len_items)])

    def swap(self, other):
        if type(other) is not Vector:
            raise TypeError("other isn't Vector!")
        self._items, other._Vector__items = other._Vector__items, self._items

    def empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def at(self, pos):
        if pos >= len(self._items):
            raise IndexError('out of range!')
        return self._items[pos]

    def __getitem__(self, pos):
        if pos >= len(self._items):
            raise IndexError('out of range!')
        return self._items[pos]

    def __copy__(self):
        result = Vector(len(self._items))
        for i, item in enumerate(self._items):
            result._items[i] = item
        return result

    def front(self):
        if len(self._items) == 0:
            return None
        return self._items[0]

    def back(self):
        len_items = len(self._items)
        if len_items == 0:
            return None
        return  self._items[len_items - 1]

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
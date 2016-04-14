#coding:UTF-8

from array import *

class Vector(Array):
    def _compareTo(self, other):
        raise NotImplemented

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

    def front(self):
        if len(self._items) == 0:
            return None
        return self._items[0]

    def back(self):
        len_items = len(self._items)
        if len_items == 0:
            return None
        return  self._items[len_items - 1]

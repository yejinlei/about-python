#coding:UTF-8

import sys
sys.path.append(r'..')
from object import *

class Array(Object):
    def __init__(self, maxlen = 0):
        assert maxlen >= 0
        super(Array, self).__init__()
        self._items = []
        self._maxlen = maxlen

    def _compareTo(self, other):
        raise NotImplemented

    @property
    def data(self):
        return self._items

    def __getitem__(self, pos):
        if pos >= len(self._items):
            raise IndexError('out of range!')
        return self._items[pos]

    def __copy__(self):
        result = Array(len(self._items))
        for i, item in enumerate(self._items):
            result._items[i] = item
        return result


#coding:UTF-8

import sys
sys.path.append(r'..')
from ..object import *

class LinkedList(Object):
    class Element(Object):
        def __init__(self):
            super(LinkedList.Element, self).__init__()

    def __init__(self):
        super(LinkedList, self).__init__()
        self._head = None
        self._tail = None

    def purge(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def isEmpty(self):
        return self._head == None




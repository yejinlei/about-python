#coding:UTF-8

import sys
sys.path.append(r'..')
from ..object import *

class Iterator(Object):
    def __init__(self, container):
        super(Iterator, self).__init__()
        self._container = container

    def _compareTo(self, other):
        raise NotImplemented

    def __iter__(self): return self

    @abstractmethod
    def next(self): pass
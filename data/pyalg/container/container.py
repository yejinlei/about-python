#coding:UTF-8

import sys
sys.path.append(r'..')
from object import *
from iterator import *

class Container(Object):
    def __init__(self):
        super(Container, self).__init__()
        self._count = 0
        self._iterator = Container.ContainerIterator(self)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, v):
        self._count = v

    @property
    def isEmpty(self):
        return self._count == 0

    @property
    def isFull(self):
        return False

    @abstractmethod
    def purge(self):    pass

    # @abstractmethod
    # def accept(self, visitor): pass

    class ContainerIterator(Iterator):
        def __init__(self, container):
            super(Container.ContainerIterator, self).__init__(container)

        def next(self): pass

    @staticmethod
    def main():
        class Dummy(Container):
            def _compareTo(self, other): pass
            def purge(self):    pass

        myco = Dummy()
        print myco.count
        myco.count = 100
        print myco.count

if __name__ == '__main__':
    Container.main()

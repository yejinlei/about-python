#coding:UTF-8

__author__  = u"叶金雷"
__date__    = u"4/13/2016"
__version__ = u"1.0"
__credits__ = u""

from abc import *

class Object(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Object, self).__init__()

    def __cmp__(self, other):
        if isinstance(self, other.__class__):
            return self._compareTo(other)
        elif isinstance(other, self.__class__):
            return -other._compareTo(self)
        else:
            return cmp(self.__class__.__name__,
                other.__class__.__name__)

    @abstractmethod
    def _compareTo(self, other):    pass

    @staticmethod
    def main():
        class Myobject(Object):
            def _compareTo(self, other):
                return  True

        myobj1 = Myobject()
        myobj2 = Myobject()
        print cmp(myobj1,myobj2)


if __name__ == '__main__':
    Object.main()
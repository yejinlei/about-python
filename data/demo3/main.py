if __name__ == '__main__':
    import A
    print globals()  #{'A': <module 'A' from 'D:\src\about-python\data\demo3\A.py'>,...}
    from B import *
    print globals()  #{'B_fun': <function B_fun at 0x000000000264D5F8>,...}

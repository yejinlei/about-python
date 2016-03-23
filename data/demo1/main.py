main_gx = 1


def main_fun1():
    global main_gx
    main_gx = 100
    import A
    A.A_fun1()

if __name__ == '__main__':
    main_fun1()
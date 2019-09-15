import os

def chooseOption():
    option = input("Option... ")
    if option == "1":
        f1()
        chooseOption()
    elif option == "2":
        f2()
        chooseOption()
    elif option == "3":
        f3()
        chooseOption()
    elif option == "4":
        f4()
    elif option == "5":
        f5()
        chooseOption()
    elif option == "c":
        os.system("clear")
        chooseOption()
    elif option == "e":
        os.system("clear")
        return
    else:
        chooseOption()


def printOptions():
    print("1 ->  b1 * bn = b2 * bn-1")
    print("2 ->  q = bn / bn-1")
    print("3 -> bn = bn-1 * q")
    print("4 -> bn = bn^2 = bn-1 * bn+1")
    print("5 -> Sn = b1 * (q^n - 1) / (q - 1)")


# b1 * bn = b2 * bn-1
def f1():
    print("b1 * bn = b2 * bn-1")
    b1 = int(input("b1 = "))
    n = int(input("n = "))
    q = int(input("q = "))

    bn = b(n, b1, q)
    bn_min1 = b(n - 1, b1, q)
    b2 = b1 * q

    if b1 * bn == b2 * bn_min1:
        print("b1 * bn == b2 * bn_min1")
    else:
        print("b1 * bn != b2 * bn_min1")


# q = bn / bn-1
def f2():
    print("q = bn / bn-1")
    bn = int(input("bn = "))
    bn_min1 = int(input("bn-1 = "))
    q = bn / bn_min1
    print(q)


# bn = bn-1 * q
def f3():
    print("bn = bn-1 * q")
    bn_min1 = int(input("bn-1 = "))
    q = int(input("q = "))
    bn = bn_min1 * q
    print(bn)


# bn^2 = bn-1 * bn+1
def f4():
    print("bn = bn^2 = bn-1 * bn+1")
    bn_min1 = int(input("bn-1 = "))
    bn_plus1 = int(input("bn+1 = "))
    bn_pow2 = bn_min1 * bn_plus1
    print(bn_pow2)


# Sn = b1 * (q^n - 1) / (q - 1)
def f5():
    print("Sn = b1 * (q^n - 1) / (q - 1)")
    b1 = int(input("b1 = "))
    q = int(input("q = "))
    n = int(input("n = "))

    Sn = b1 * (q**n - 1) / (q - 1)
    print(Sn)


# bn = b1 * q^n-1
def b(n, b1, q):
    return b1 * q**(n - 1)


print("Progresii geometrice\n")
printOptions()    
chooseOption()
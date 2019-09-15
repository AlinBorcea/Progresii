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
    print("1 ->  a1 + an = a2 + an-1")
    print("2 -> r = an - an-1")
    print("3 -> an = an-1 + r")
    print("4 -> an = (an-1 + an+1) / 2")
    print("5 -> Sn = ((a1 + an)n) / 2")


# a1 + an = a2 + a(n-1)
def f1():
    print("a1 + an = a2 + a(n-1)")
    a1 = int(input("a1 = "))
    n = int(input("n = "))
    r = int(input("r = "))

    an = a(n, a1, r)
    an_min1 = a(n - 1, a1, r)
    a2 = a1 + r

    if a1 + an == a2 + an_min1:
        print("a1 + an = a2 + an-1")
    else:
        print("a1 + an != a2 + an-1")


# r = an - an-1
def f2():
    print("r = an - an-1")
    an = int(input("an = "))
    an_min1 = int(input("an-1 = "))
    r = an - an_min1
    print(r)


# an = an-1 + r
def f3():
    print("an = an-1 + r")
    an_min1 = int(input("an-1 = "))
    r = int(input("r = "))
    an = an_min1 + r
    print(an)


# an = (an-1 + an+1) / 2
def f4():
    print("an = (an-1 + an+1) / 2")
    an_min1 = int(input("an-1 = "))
    an_plus1 = int(input("an+1 = "))
    an = (an_min1 + an_plus1) / 2
    print(an)


# Sn = ((a1 + an)n) / 2
def f5():
    print("Sn = ((a1 + an)n) / 2")
    a1 = int(input("a1 = "))
    r = int(input("r = "))
    n = int(input("n = "))

    an = a(n, a1, r)
    Sn = ((a1 + an) * n) / 2
    print(Sn)


# an = a2 + (n - 1)r
def a(n, a1, r):
    return a1 + (n - 1) * r


print("Progresii aritmetice\n")
printOptions()    
chooseOption()
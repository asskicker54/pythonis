import math
def task1():
    film = input()
    cinema = input()
    time = input()

    print("Билет на ", film, " в ", cinema, " на ", time, " забронирован" )

def task2():
    w1 = input()
    w2 = input()

    if (w1.lower() == w2.lower()):
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

def task3():
    login = input()
    email = input()

    if "@" not in login and "@" in email:
        print("Correct")
    else:
        print("Not Correct")

def task4():
    print(input())

def task5():
    line = input()
    if not line:
        print("Yes")
    else:
        print("No")

def task6():
    a = input()
    arr = list(map(int, a))

    a_max = max(arr)
    a_min = min(arr)

    arr.remove(a_max)
    arr.remove(a_min)

    if arr[0] == ((a_max + a_min)//2):
        print("ok")
    else:
        print("not ok")
      

def task7():
    num = int(input())

    n1 = num % 10
    num //= 10
    n2 = num  % 10
    num //= 10
    n3 = num % 10
    num //= 10
    n4 = num

    if n1 > n2:
       n1, n2 = n2, n1;
    
    if n2 > n3:
        n2, n3 = n3, n2

    if n3 > n3:
        n3, n4 = n4, n3

    if n1 > n2:
        n1, n2 = n2, n1

    if n2 > n3:
        n2, n3 = n3, n2

    if n1 > n2:
        n1, n2 = n2, n1

    if n1 == 0 and n2:
        n1, n2 = n2, n1

    elif n1 == 0 and n3:
        n1, n3 = n3, n1

    elif n1 == 0 and n4:
        n1, n4 = n4, n1

    print(n4 + 10 * (n3 + 10 * (n2 + 10 * n1)))

def task8():
    height = ""
    arr = []
    count = 0
    while(height != "!"):
        height = input()
        if(height == "!"):
            break
        else:
            if  150 <= int(height) <= 190:
                height = int(height)
                arr.append(height)
                count += 1
    print(count, arr)
        

def task9():    
    while True:
        p1 = input("p1:")
        p2 = input("p2:")
        if len(p1) < 8:
            print("Короткий!")
        elif "123" in p1:
            print("Простой!")
        elif p1 != p2:
            print("Различаются!")
        else:
            print("OK")
            break 


def task10():
    operation = ""
    while operation != "x":
        x1 = input()
        operation = input()

        if operation == "+":
            print(int(x1) + int(input()), end = "\n\n")
        elif operation == "*":
            print(int(x1) * int(input()), end = "\n\n")
        elif operation == "-":
            print(int(x1) - int(input()), end = "\n\n")
        elif operation == "/":
            x2 = int(input())
            if x2 != 0:
                print(int(x1) / x2, end = "\n\n")
            else:
                print("Error", end = "\n\n")
            del x2
        elif operation == "%":
            x2 = int(input())
            if x2 != 0:
                print(int(x1) % x2, end = "\n\n")
            else:
                print("Error", end = "\n\n")
            del x2
        elif operation == "!":
            print(math.factorial(int(x1), end = "\n\n"))
        elif operation == "x":
            print(x1)
            
def task11():
    h = int(input())
    for i in range(1, 2 * h, 2):
        space = " " * ((2 * h - 1 - i) // 2)
        print(space + "*" * i + space)
    

def task12():
    n = int(input())
    number = 1
    limit = 1
    inLine = 0

    while number <= n:
        print(number, end= " ")
        number += 1
        inLine += 1
        if inLine == limit:
            print("")
            limit += 1
            inLine = 0

def task13():
    n = int(input())
    m = int(input())
    symb = input()

    print(symb * m)
    for i in range(1, n - 1):
        print(symb + " " * (m - 2) + symb)
    print(symb * m)

task13()

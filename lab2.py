import random

def task1():
    s = input()
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:len(s)-2])
    print(s[:len(s):2])
    print(s[1:len(s):2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))

def task2():
    s = input()
    s1 = s[:round(len(s)/2)]
    s2 = s[len(s1):]
    s1, s2 = s2, s1
    final_s = s1 + s2
    print(final_s)

def task3():
    s = input()
    i1 = s.find('h')
    i2 = s[::-1].find('h')
    s_between_h = s[i1 + 1:-i2 - 1]
    print(s[:i1 + 1] + s_between_h[::-1] + s[(-i2 - 1) :len(s)])

def task4():
    s = input()
    count = s.count('f')
    if count >= 2:
        print(s.find('f'), len(s) - (s[::-1].find('f')) - 1)
    elif count == 1:
        print(s.find('f'))
    else:
        return

def task5():
    arr = [random.randint(0, 10) for i in range(10)]
    print(arr)

    for i  in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            print(arr[i])

def task6():
    lenght  = int(input())
    arr = [random.randint(-10, 2) for i in range(lenght)]
    print(arr)

    for i in range(lenght):
        if arr[i] < 0 and arr[i+1] < 0:
            print(arr[i], arr[i+1])
            break

def task7():
    #lenght = random.randint(10, 14)
    lenght  = int(input())
    arr = [random.randint(0, 10) for i in range(lenght)]
    print(arr)

    for i in range(0, lenght, 2):
        if i != lenght - 1:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)

def task8():
    lenght  = int(input())
    arr = [random.randint(0, 10) for i in range(lenght)]
    print(arr)

    for i in arr:
        if arr.count(i) == 1:
            print(i)

def task9():
    a1 = []
    a2 = []
    n = 8
    flag = True

    for i in range(n):
        a1_in, a2_in = [int(s) for s in input().split()]

        a1.append(a1_in)
        a2.append(a2_in)

    for i in range(n):
        for j in range(i + 1, n):
            if a1[i] == a2[j] or a1[i] == a2[j] or abs(a1[i] - a2[j]) == abs(a1[i] - a2[j]):
                flag = False

    if flag:
        print('NO')
    else:
        print('YES')



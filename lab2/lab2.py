import random
def task1():
    a = [random.randint(0,10) for i in range(10)]
    print(a)
    print(len(set(a)))

def task2():
    a = [random.randint(0,10) for i in range(10)]
    m = [random.randint(0,10) for i in range(10)]
    print(a)
    print(m)

    print(len(set(a) & set(m)))

def task3():
    a = [random.randint(0,10) for i in range(10)]
    m = [random.randint(0,10) for i in range(10)]
    print(a)
    print(m)

    print(sorted(list(set(a) & set(m))))

def task4():
    line = input()
    arr = line.split(" ")
    repeats = set()

    for i in arr:
        if i in repeats:
            print("yes")
        else:
            repeats.add(i)
            print('no')

def task5():
    words = set()
    lines = int(input())
    for i in range(lines):
        words.update(input().split())
    print(len(words))

task5()
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
        print("niggers")
      

def task7():
    num = int(input())
    n1 = num % 10
    num //= 10
    n2 = num  % 10
    num //= 10
    n3 = num % 10
    num //= 10
    n4 = num

    mini = 9
    maxi = 0

    if n1 < mini:
        mini = n1
    
    if n2 < mini:
        mini = n2

    if n3 < mini:
        mini = n3

    if n4 < mini:
        mini = n4

    print(mini)

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
        
task8()

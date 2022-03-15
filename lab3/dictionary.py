def task1():
    line = input().split()
    count = dict()
    for word in line:
        if word not in count:
            count.update({word:1})
        else:
            count.update({word: count[word] + 1})
    print(count)

def task2():
    syn = dict()
    for i in range(int(input())):
        s1, s2 = input().split(" ")
        syn.update({s1: s2})
        syn.update({s2: s1})

    print(syn[input()])

def task3():
    res = dict()
    for i in range(int(input())):
        last_name, votes = input().split(" ")
        if last_name not in res:
            res.update({last_name: int(votes)})
        else:
            res.update({last_name: int(votes) + res[last_name]})

    print(sorted(res.items()))

def task4():
    files = dict()
    for n in range(int(input("N = "))):  
        inp = list(input().split(" "))
        files.update({inp[0]: inp[1:]})
    print(files)
    for m in range(int(input("M = "))):
        req_op, req_name = input().split(" ")
        if req_op == "read":
            if "R" in files[req_name]:
                print("OK")
            else:
                print("Acces denied")
        elif req_op == "write":
            if "W" in files[req_name]:
                print("OK")
            else:
                print("Acces denied")
        elif req_op == "execute":
            if "X" in files[req_name]:
                print("OK")
            else:
                print("Acces denied")

def task5():
    count = dict()
    for i in range(int(input())):
        line = input().split(" ")
        for word in line:
            if word not in count:
                count.update({word:1})
            else:
                count.update({word: count[word] + 1})
        
    srt_count = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
    print(srt_count)

task5()


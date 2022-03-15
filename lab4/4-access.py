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
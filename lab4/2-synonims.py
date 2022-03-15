syn = dict()
for i in range(int(input())):
    s1, s2 = input().split(" ")
    syn.update({s1: s2})
    syn.update({s2: s1})

print(syn[input()])
res = dict()
for i in range(int(input())):
    last_name, votes = input().split(" ")
    if last_name not in res:
        res.update({last_name: int(votes)})
    else:
        res.update({last_name: int(votes) + res[last_name]})

print(sorted(res.items()))
def matrix(*args):
    if len(args) == 0:
        return [0]
    elif len(args) == 1:
        return [[0] * args[0] for i in range(args[0])]
    elif len(args) == 2:
        return[[0] * args[1] for i in range(args[0])]
    elif len(args) == 3:
        return [[args[2]] * args[1] for i in range(args[0])]


m = matrix(3, 4, 5)
for row in m:
    print(*row)
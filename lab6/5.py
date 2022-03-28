def factorials(n):
    count = 0
    f = 1
    while count < n:
        count += 1
        f *= count
        yield f 

print(list(factorials(int(input()))))
        
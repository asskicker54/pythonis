def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0: 
        print(res)
    else:
        print(1/res)

power(int(input()), int(input()))
def square_fibonacci(n):
    cur_num = 0
    next_num = 1
    for i in range(n):
        cur_num, next_num = next_num, cur_num + next_num
        yield cur_num ** 2
        

print(list(square_fibonacci(int(input()))))


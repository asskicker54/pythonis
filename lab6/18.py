def check_password(func):
    def wrapped(*args, **kwargs):
        if input("password: ") != 'qwerty':
            print("wrong password")
        else:
            return func(*args, **kwargs)
    return wrapped
    
@check_password    
def calc_fib(n):
    cur_num = 0
    next_num = 1
    for i in range(n):
        cur_num, next_num = next_num, cur_num + next_num
    return cur_num

print(calc_fib(7))


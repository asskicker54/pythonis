def check_password(password):
    def check(func):
        def wrapper(*args, **kwargs):
            if input('password: ') != password:
                print('wrong password')
            else:
                return func(*args, **kwargs)
        return wrapper
    return check
    

@check_password('qwerty')
def func1(*args):
    return sum(args)
@check_password('12345')
def func2(*args):
    return list(args)

print(func1(1, 2, 3))
print(func2(2, 2, 2, 3, 2))
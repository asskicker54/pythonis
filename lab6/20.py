def cached(func):
    cache = {}
    def wrapper(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            nc = func(*args, **kwargs)
            cache[args] = nc
            return nc
        else:
            return cache[args]
    return wrapper

@cached
def calc_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

print(calc_fib(10))
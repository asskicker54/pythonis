def gen_rus_alph():
    l = ord('а') - 1
    while l != ord('я'):
        l += 1
        yield chr(l)

print(list(gen_rus_alph()))
    
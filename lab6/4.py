a = [i for i in range(10, 25)]
print('Data:', a)
print('Result:')
print(list(map(lambda x: x / 2, filter(lambda x: x > 17, a))))
print([el / 2 for el in a if el > 17])
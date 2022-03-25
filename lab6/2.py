a = [i for i in range(1, 11)]
print('Data:', a)
print('Result:')
print(list(map(lambda x: x / 2, a)))
print([el / 2 for el in a])
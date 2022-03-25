a = [i for i in range(1, 11)]
print('Data:', a)
print('Result:')
print(list(filter(lambda x : x < 5, a)))
print([i for i in a if i < 5])
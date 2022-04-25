import numpy as np

arr_1 = np.full((3, 4), 3)
print(f'a)\n{arr_1}\n')

arr_2 = np.random.randint(0, 10, (2, 4))
print(f'b)\n{arr_2}\n')

print(f'c)\narr_1: {arr_1.size}\narr_2:{arr_2.size}\n')

arr_ = np.append(arr_1, arr_2, axis=0)
print(f'd)\n{arr_}\n')

arr_3 = np.array((1, 8, 6, 5, 8, 3))
print(f'e)\n{arr_3}\n')

arr_4 = arr_3 * 3 + 1
print(f'f)\n{arr_4}\n')

arr_5 = arr_3.reshape(2, 3)
print(f'g)\n{arr_5}\n')

print('h)', np.min(arr_5, 1))

print('i)', np.mean(arr_5))

arr_6 = np.square(np.arange(11))
print('j)\n', arr_6)

print('k)\n', arr_6[::2])

print('l)\n', arr_6[::-1])

arr_6[::2] = 2
print('m)\n', arr_6)

print('n)\n', 49 in arr_6)

A = np.random.randint(-10, 11, (4, 4))
B = A[A < 0]
print(f'o)\nA:{A}\nB:{B}\n')





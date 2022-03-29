data = [3, 6, -8, 2, -78, 1, 23, -45, 9]
print(f'data: {data}')
print(f'result: {sorted(data, key=abs, reverse=True)}')

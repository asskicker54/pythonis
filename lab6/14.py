data = [(1, 1), (3, 4), (5, 6), (-2, 1), (1, 4)]
print(sorted(data, key=lambda x: (x[0] ** 2 + x[1] **  2) ** 0.5))


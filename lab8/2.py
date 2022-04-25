import numpy as np

def make_field(size):
    field = np.zeros((size, size), dtype=np.uint8)
    field[size % 2::2, ::2] = 1
    field[(size + 1) % 2::2, 1::2] = 1
    return field

print(make_field(size=8))
    
def mirror(arr):
    mirrored_part = arr.copy()
    mirrored_part.reverse()
    arr += mirrored_part
    
    
arr = [1, 2, 3, 4]
mirror(arr)
print(*arr)

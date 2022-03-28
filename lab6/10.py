def same_by(ch, obj):
    res = list(filter(ch, obj))
    if len(res) == len(obj):
        return True
    else:
        return False
    
val = [11, 121, 22, 33]
print('data:', val, '\nCharacteristic: Divisible by 11')    
print('result:', end='')
if same_by(lambda x: x % 11 == 0, val):
    print('same')
else:
    print('different')
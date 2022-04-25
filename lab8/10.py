with open('./data/input.bmp', 'rb') as bin_in:
    data = bytes(bin_in.read())
    
neg = []

for i, value in enumerate(data):
    if i < 54:
        neg.append(value)
    else:
        neg.append(255 - value)
    
with open('./data/output.bmp', 'wb') as out:
    out.write(bytes(neg))
    
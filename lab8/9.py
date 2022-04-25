with open('./data/input.txt', 'r', encoding='utf8') as inp:
    data = [int(i) for i in inp.read().split(' ')]
    
pos = []
neg = []
null = []

for _ in data:
    if _ > 0:
        pos.append(_)
    elif _ < 0:
        neg.append(_)
    else:
        null.append(_)

with open('./data/output.txt', 'w') as out:
    print(len(data), file=out)
    print('1', len(pos), '-1', len(neg), '0', len(null), file=out)
    

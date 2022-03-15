line = input().split()
count = dict()
for word in line:
    if word not in count:
        count.update({word:1})
    else:
        count.update({word: count[word] + 1})
print(count)
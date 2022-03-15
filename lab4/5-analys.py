count = dict()
for i in range(int(input())):
    line = input().split(" ")
    for word in line:
        if word not in count:
            count.update({word:1})
        else:
            count.update({word: count[word] + 1})
        
srt_count = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
print(srt_count)


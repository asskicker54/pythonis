import random

file = open('./data/lines.txt', encoding='utf8')
data = file.read()
text = data.split('\n')
lenght = len(text)

if lenght:
    line = random.randrange(lenght)
    print(text[line])
    
file.close()
    

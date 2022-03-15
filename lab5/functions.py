from email import message

from numpy import true_divide


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**0.5


def num_to_words(n):
    d = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
        10: 'десять',
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать',
        20: 'двадцать',
        30: 'тридцать',
        40: 'сорок',
        50: 'пятьдесят',
        60: 'шестьдесят',
        70: 'семьдесят',
        80: 'восемьдесят',
        90: 'девяносто',
    }
    
    if n < 20:
        print(d[n])

    one  = n % 10
    tens = n // 10
    
    print(d[tens * 10] + " " + d[one])

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0: 
        print(res)
    else:
        print(1/res)

def palindrome(s):
    s = list(s.lower().replace(" ", ""))
    if s == s[::-1]:
        return "palindrom"
    else:
        return "not palindrome"

mes = ""
def print_without_duplucates(m):
    global mes
    if m == mes:
        pass
    else:
        mes = m
        print(m)

friends = dict()

def add_friends(name, list_of_friends):
    if name not in friends:
        friends.update({name: list_of_friends})
    else:
        friends.update({name: friends[name] + list_of_friends})

#add_friends("Al", ["m", "n"])
#print(friends)
#add_friends("Al", ["F"])
#print(friends)
def are_friends(name1, name2):
    if name1 in friends and name2 in friends:
        if name1 in friends[name2] or name2 in friends[name1]:
            return True
        else:
            return False
    elif name1 in friends:
        if name2 in friends[name1]:
            return True
        else:
            return False
    elif name2 in friends:
        if name1 in friends[name2]:
            return True
        else:
            return False


#print(are_friends("Al", 'm'))
#print(are_friends('m', 'Al'))
#print(are_friends("Al", "r"))

def print_friends(name):
    for i in friends[name]:
        print(i, end=" ")
    print("\n")

#print_friends("Al")

def mirror(arr):
    mirrored_part = arr.copy()
    mirrored_part.reverse()
    arr += mirrored_part
    
    
#arr = [1, 2, 3, 4]
#mirror(arr)
#print(*arr)

#a = [77, "abc"]

def from_string_to_list(string, container):
    container += string.split(" ")

#from_string_to_list("", a)
#print(*a)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(m):
    res = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[i][j], res[j][i] = res[j][i], res[i][j]
    return res
    

    
m = transpose(matrix)
print(matrix)
for line in m:
    print(*line)

        

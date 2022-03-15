friends = dict()

def add_friends(name, list_of_friends):
    if name not in friends:
        friends.update({name: list_of_friends})
    else:
        friends.update({name: friends[name] + list_of_friends})

add_friends("Al", ["m", "n"])
print(friends)
add_friends("Al", ["F"])
print(friends)
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


print(are_friends("Al", 'm'))
print(are_friends('m', 'Al'))
print(are_friends("Al", "r"))

def print_friends(name):
    for i in friends[name]:
        print(i, end=" ")
    print("\n")

print_friends("Al")
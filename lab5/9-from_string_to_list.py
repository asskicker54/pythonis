a = [77, "abc"]

def from_string_to_list(string, container):
    container += string.split(" ")

from_string_to_list("", a)
print(*a)
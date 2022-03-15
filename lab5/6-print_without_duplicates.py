mes = ""
def print_without_duplucates(m):
    global mes
    if m == mes:
        pass
    else:
        mes = m
        print(m)

print_without_duplucates("1")
print_without_duplucates("1")
print_without_duplucates("2")
print_without_duplucates("3")
print_without_duplucates("2")

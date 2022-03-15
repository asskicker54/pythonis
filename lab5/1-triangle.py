def triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print("Yes")
    else:
        print("No")

i = input
triangle(i(), i(), i())
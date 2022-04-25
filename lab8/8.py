def reverse():
    with open('./data/input.dat', 'rb') as inp:
        q = inp.read()
    with open('./data/output.dat', 'wb') as out:
        out.write(q[::-1])
        
reverse()
    
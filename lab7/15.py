class Digits:
    def __init__(self, arr):
        self.arr = [int(x) for x in arr.split()]
 
    def make_negative(self):
        for i in range(len(self.arr)):
            self.arr[i] = -abs(self.arr[i])
 
    def square(self):
        for i in range(len(self.arr)):
            self.arr[i] = (self.arr[i]) ** 2
 
    def strange_command(self):
        for i in range(len(self.arr)):
            if self.arr[i] % 5 == 0:
                self.arr[i] += 1
 

           
dig = Digits(input("Digits: "))

for i in range(int(input("N: "))):
    operation = input("Operation: ")
    
    if operation == 'make_negative':
        dig.make_negative()
    elif operation == 'square':
        dig.square()
    else:
        dig.strange_command()

for i in dig.arr:
    print(i, end=' ')
print('\n')
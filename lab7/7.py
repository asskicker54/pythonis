class Polynomial():
    
    def __init__(self, coefficents):
        self.c = coefficents
        
    def __call__(self, x):
        result = self.c[0]
        
        for i in range(len(self.c)):
            result += (x ** i) * self.c[i]
            
        return result
        
    def __add__(self, other):
        temp = []
        result = Polynomial(temp)
        if len(self.c) < len(other.c):
            n = len(self.c)
        else:
            n = len(other.c)
            
        for i in range(n):
            temp.append(self.c[i] + other.c[i])
            
        if len(self.c) > n:
            temp += self.c[n::]
        else:
            temp += other.c[n::]
            
        result.c = temp
        
        return result
    
poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))

poly3 = poly1 + poly2
print(poly3(-2))
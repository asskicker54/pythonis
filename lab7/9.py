class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetr(self):
        return self.a + self.b + self.c
    
    
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)
        
et = EquilateralTriangle(10)
print(et.perimetr())
    
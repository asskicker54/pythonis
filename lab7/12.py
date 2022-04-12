class A():
    def __str__(self):
        return 'A.__str__method'
    
    def hello(self):
        print("Hello")
        
class B():
    def __str__(self):
        return 'B.__str__method'
    
    def good_evening(self):
        return "Good evening"
    

class C(A, B):
    pass

class D(B, A):
    pass

c = C()
d = D()

c.hello()
d.hello()
d.good_evening()
c.good_evening()

print(c)
print(d)
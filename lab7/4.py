class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.x == other.x and self.y == other.y:
            return False
        else:
            return True
        

p1 = Point(1, 1)
p2 = Point(1, 2)

if p1 == p2:
    print("True")
else:
    print("False")
        
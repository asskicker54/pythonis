class Queue():
    def __init__(self, *args):
            self.elements = []
            for i in args:
                self.elements.append(i)
            
    def append(self, *args):
        for i in args:
            self.elements.append(i)
            
    def copy(self):
        cop = Queue()
        for i in self.elements:
            cop.elements.append(i)
        return cop
            
    
    def pop(self):
        if len(self.elements) != 0:
            el = self.elements[0]
            self.elements.pop(0)
            return el
        else:
            return None
    
    def extend(self, queue):
        for i in queue.elements:
            self.elements.append(i)
            
    def next(self):
        temp = self.copy()
        temp.pop()
        return temp
    
    def __str__(self):
        if self.elements:
            self.elements = list(map(str, self.elements))
            el = ' -> '.join(self.elements)
            return f'[{el}]'
        else:
            return '[]'
        
    def __rshift__(self, n):
        if len(self.elements) > n:
            new = Queue()
            new.elements += self.elements[n:]
            return new
        return Queue()
 
    def __add__(self, other):
        temp = self.copy()
        temp.elements += other.elements
        return temp
 
    def __iadd__(self, other):
        self.elements += other.elements
        return self
 
    def __eq__(self, other):
        if self.elements == other.elements:
            return True
        return False
    
    def __next__(queue):
        cpy = queue.copy()
        cpy.elements = cpy.elements[1:]
        return cpy

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)

q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))  
q3 = q2.next()

print(q1, q2, q3, sep=', ')  
print(q1 + q3)  
q3.extend(Queue(1, 2))
print(q3) 

q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)  
q5 = next(q4)
print(q4)  
print(q5)

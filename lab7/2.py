class Balance():
    
    __left = 0
    __right = 0
    
    def add_left(self, left):
        self.__left += left
        
    def add_right(self, right):
        self.__right += right
        
    def result(self):
        if self.__left > self.__right:
            return "L"
        elif self.__left < self.__right:
            return "R"
        else:
            return "="
        
        
b = Balance()

b.add_left(9)
b.add_right(10)
print(b.result())
b.add_left(2)
print(b.result())
b.add_right(1)
print(b.result())

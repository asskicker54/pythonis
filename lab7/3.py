class Selector():
    
    #__val = []
    
    def __init__(self, values):
        self.__val = values
        
    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.__val))
    
    def get_odds(self):
        return [x for x in self.__val if x not in self.get_evens()]
    

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sel = Selector(values)
print(sel.get_evens())
print(sel.get_odds())
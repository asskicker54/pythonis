class ReversedList():
    __array = []
    def __init__(self, array):
        self.__array = array[::-1]
        
    def __len__(self):
        return len(self.__array)
    
    def __getitem__(self, index):
        return self.__array[index]
    


rev = ReversedList([1, 2, 3, 4, 5])

for i in range(len(rev)):
    print(rev[i])
        
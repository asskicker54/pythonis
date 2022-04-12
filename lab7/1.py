class BigBell():

    __ring_type = True
    
    def sound(self):
        if self.__ring_type:
            print("ding")
            self.__ring_type = False
        else:
            print("dong")
            self.__ring_type = True
            
bell = BigBell()

bell.sound()
bell.sound()
bell.sound()
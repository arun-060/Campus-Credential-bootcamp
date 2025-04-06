import time

class Tower:
    def __init__(self):
        print("welcome to tower of hanoi game")
        print()
        print("given problem A= [3,2,1]  B = [] C = []")
        print()
        print("Expected output A = []    B = [] C = []")
        self.A = []
        self.B = []
        self.C = []
        
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("items in tower A\n")
        
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass one comeplete===============================\n")   
             
    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass two comeplete===============================\n")     
           
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass Three complete==============================\n")  
        
    def pass4(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass four complete==============================\n")  
    
    def pass5(self):
        self.temp=self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass five complete==============================\n")
    
    def pass6(self):
        self.temp=self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass five complete==============================\n")
        
    def pass7(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A  , "      ", "B=",self.B,"        ","c=",self.C)
        print("pass five complete==============================\n")
    
if __name__ == "__main__":
    tower = Tower()
    tower.tower(3)
    tower.tower(2)
    tower.tower(1)
    tower.pass1()
    tower.pass2()
    tower.pass3()
    tower.pass4()
    tower.pass5()
    tower.pass6()
    tower.pass7()

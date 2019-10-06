#Exercise 6

class Boeing747(Aircraft):
    def __init__(self,x1=None,y1=None,x2=None,y2=None):
        if not x1:
            self.x1=random.randint(1,100)
        if not y1:
            self.y1=random.randint(1,100)
        if not x2:
            self.x2=random.randint(1,100)
        if not y2:
            self.y2=random.randint(1,100)
        print("A new object is created")
        print("Initial X coordinate is:",self.x1)
        print("Initial Y coordinate is:",self.y1)
        print('Boeing747 is going places')
        print("Final X Coordinate is:", self.x2)
        print("Final Y Coordinate is:", self.y2)
        
        m=(self.y2-self.y1)/(self.x2-self.x1)
        #print(m)
        b=self.y1-(m*self.x1)
        #print(b)
        
        print("Starting from: ",(self.x1,self.x2))
        print("Headed to: ", (self.x2,self.y2))
        for j in range (self.x1,self.x2):
            y=(m*j)+b
            print(j,y)
    
        return print("you have arrived")    
    def priacc(self):
        Aircraft.__init__(self)
        print ("The accelerations is:", self.a)
        

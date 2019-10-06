#Exercise 5
import random
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
        
l=int(input("Enter the number of instances you want to create: "))        
Boe=[]
for k in range(l):
    print("New aircraft object has been initialized:",k)
    k=Boeing747()

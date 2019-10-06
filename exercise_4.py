#Exercise 4

class Aircraft:
    def __init__(self,x=0,y=0):
        self.move(x,y)
        self.a = 1
        print("A new object is created")
    
    def move(self,x,y):
        self.x=x
        self.y=y     
         
    def moveup(self):
        print("move up...")
        self.x+=self.a
        return self.x, self.y
    def movedown(self):    
        print("move down...")
        self.x-=self.a
        return self.x, self.y
    def moveright(self):
        print("move right...")
        self.y+=self.a
        return self.x, self.y
    def moveleft(self):
        print("move left...")        
        self.y-=self.a
        return self.x, self.y
    
c=Aircraft(5,2)
print("The Initial X,Y and acceleration Coordinates are: ", c.__dict__)

c=Aircraft()
print("The Initial X,Y and acceleration Coordinates are: ", c.__dict__)

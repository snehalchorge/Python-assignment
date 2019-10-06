#Exercise 2

class Aircraft:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 1
        print ('X Coordinate is 0')
        print ('Y Coordinate is 0')
    
    def moveup(self):
        print("move up...")
        self.x+=self.a
        #return self.x, self.y
    def movedown(self):  
        print("move down...")
        self.x-=self.a
        #return self.x, self.y
    def moveright(self):
        print("move right...")        
        self.y+=self.a
        #return self.x, self.y
    def moveleft(self):  
        print("move left...")
        self.y-=self.a
        #return (self.x, self.y)
    def position(self):
        print("Final X coordinate is: ", self.x)
        print("Final Y coordinate is : ", self.y)
    
c=Aircraft()
c.moveup()
c.moveup()
c.moveup()
c.moveright()
c.moveright()
c.movedown()
c.moveleft()
c.moveright()
c.movedown()
c.moveleft()
c.moveup()
c.moveright()
c.moveright()
c.position()

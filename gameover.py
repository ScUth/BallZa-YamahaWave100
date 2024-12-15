import math

class gover:
    def __init__(self, ttl):
        self.ttl = ttl
        self.size = 100
    
    def g(self, size):
        self.ttl.penup()
        self.ttl.seth(90)
        self.ttl.forward(size/2)
        self.ttl.seth(180)
        self.ttl.forward(size/2)
        self.ttl.pendown()
        self.ttl.seth(0)
        self.ttl.forward(size/2)
        self.ttl.seth(270)
        self.ttl.forward(size/2)
        self.ttl.seth(180)
        self.ttl.forward(size)
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.forward(size)
        self.ttl.seth(270)
        self.ttl.penup()
        self.ttl.forward(size)
        self.ttl.seth(0)
        
    def a(self, size):
        self.ttl.pendown()
        self.ttl.seth(math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2))
        self.ttl.right(2 * math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2) / 1.5)
        self.ttl.seth(180)
        self.ttl.forward(size / 1.5)
        self.ttl.backward(size / 1.5)
        self.ttl.right(180 + math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2) - math.sqrt(size**2+(size/2)**2) / 1.5)
        self.ttl.seth(0)
        self.ttl.penup()
        
    def m(self, size):
        self.ttl.pendown()
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.right(90 + math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2))
        self.ttl.left(2 * math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2))
        self.ttl.seth(270)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.penup()
        
    def e(self, size):
        self.ttl.pendown()
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.forward(size)
        self.ttl.backward(size)
        self.ttl.seth(270)
        self.ttl.forward(size / 2)
        self.ttl.seth(0)
        self.ttl.forward(size)
        self.ttl.backward(size)
        self.ttl.seth(270)
        self.ttl.forward(size / 2)
        self.ttl.seth(0)
        self.ttl.forward(size)
        self.ttl.penup()
        
    def o(self, size):
        self.ttl.pendown()
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.forward(size)
        self.ttl.seth(270)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.backward(size)
        self.ttl.forward(size)
        self.ttl.penup()
        
    def v(self, size):
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.pendown()
        self.ttl.right(90 + math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2))
        self.ttl.left(2 * math.degrees(math.atan(size / (size/2))))
        self.ttl.forward(math.sqrt(size**2+(size/2)**2))
        self.ttl.penup()
        self.ttl.seth(270)
        self.ttl.forward(size)
        self.ttl.seth(0)
        
    def r(self, size):
        self.ttl.pendown()
        self.ttl.seth(90)
        self.ttl.forward(size)
        self.ttl.seth(0)
        self.ttl.forward(size * 3/4)
        self.ttl.backward(size * 3/4)
        self.ttl.seth(90)
        self.ttl.backward(size / 2)
        self.ttl.seth(0)
        self.ttl.forward(size *3/4)
        self.ttl.circle(size / 4, 180, 90)
        self.ttl.forward(size * 3/4)
        self.ttl.seth(270)
        self.ttl.forward(size / 2)
        self.ttl.left(math.degrees(math.atan(size / (size / 2))))
        self.ttl.forward(math.sqrt((size)**2+(size/2)**2))
        self.ttl.seth(0)
        self.ttl.penup()
        
    #def WIN
        
    def create(self):
        self.ttl.speed(0)
        self.ttl.penup()
        self.ttl.goto(-350, 0)
        self.g(100)
        self.ttl.forward(10)
        self.a(100)
        self.ttl.forward(10)
        self.m(100)
        self.ttl.forward(10)
        self.e(100)
        self.ttl.forward(40)
        self.o(100)
        self.ttl.forward(10)
        self.v(100)
        self.ttl.forward(10)
        self.e(100)
        self.ttl.forward(10)
        self.r(100)
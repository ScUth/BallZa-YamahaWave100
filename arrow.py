import turtle

class Arrow:
    def __init__(self, arrow):
        self.arrow = arrow
    
    def fire(self, ang, speed):
        self.arrow.clear()
        self.arrow.speed(0)
        self.arrow.pendown()
        self.arrow.seth(ang)
        self.arrow.forward(speed)
        
    
    #def set_loma(self, x, y):
    #    self.arrow.pendown()
    #    self.arrow.goto(x, y)
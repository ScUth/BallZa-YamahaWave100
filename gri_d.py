import turtle

class draw_grid:
    def __init__(self, turtle_name):
        self.turtle_name = turtle_name
        self.box_size = 1000
        
    def box(self):
        self.turtle_name.seth(0)
        for i in range(4):
            self.turtle_name.forward(self.box_size)
            self.turtle_name.left(90)

    def draw(self):
        self.turtle_name.speed(0)
        self.turtle_name.penup()
        self.turtle_name.goto(0, -self.box_size/2)
        self.turtle_name.pendown()
        self.turtle_name.seth(0)
        self.turtle_name.backward(self.box_size/2)
        self.box()
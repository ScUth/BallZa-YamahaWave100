import turtle

class hat_move:
    def __init__(self, tuhat, py_size, py_stroke):
        self.tuhat = tuhat
        self.py_size = py_size
        self.py_stroke = py_stroke
    
    def draw(self):
        self.tuhat.penup()
        self.tuhat.forward(3 * self.py_size)
        self.tuhat.pendown()
        
    def set_loma(self, x, y, ang):
        self.tuhat.speed(0)
        self.tuhat.clear()  # Clear previous drawing
        self.tuhat.penup()
        self.tuhat.goto(x, y)  # Move the turtle to the new position
        self.tuhat.pendown()
        
        # Redraw the hat
        self.tuhat.seth(ang)
        self.tuhat.pendown()
        self.tuhat.width(self.py_stroke)
        self.tuhat.seth(ang + 120)
        self.tuhat.forward(self.py_size)
        self.tuhat.backward(self.py_size)
        self.tuhat.seth(ang + 240)
        self.tuhat.forward(self.py_size)
        self.tuhat.backward(self.py_size)
        self.tuhat.seth(ang)
        self.tuhat.penup()
        
    def clear(self):
        self.tuhat.clear()
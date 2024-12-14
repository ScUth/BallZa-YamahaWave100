import turtle

class Arrow:
    def __init__(self, arrow):
        self.arrow = arrow
        self.state = "ready"
    
    def fire(self):
        if self.state == "ready":
            self.state = "active"
    
    def set_loma(self, x, y):
        self.arrow.pendown()
        self.arrow.goto(x, y)
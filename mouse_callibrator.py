import turtle
import math
import pynput

class callibrate:
    def __init__(self):
        self.xx = 0
        self.yy = 0
        self.xc = 0
        self.yc = 0
        self.turtle_move = turtle.Turtle()
        self.turtle_click = turtle.Turtle()
        self.turtle_z = turtle.Turtle()
        self.xz, self.yz = self.turtle_z.pos()
        self.xm, self.ym = self.turtle_move.pos()
        self.cx, self.cy = self.turtle_click.pos()
    
    def on_move(self, x, y):
        self.xx, self.yy = x, y
        
    def on_click(self, x, y, botton, pressed):
        if pressed:
            self.xc, self.yc = x, y
    def distance_btw_p(self, x1, y1, x2, y2):
        dist = math.sqrt((abs(x1-x2))+(abs(y1-y2)))
        return dist
    
    def distance_btw_p_2(self, x1, y1, x2, y2):
        disx = x2 - x1
        disy = y2 - y1
        return disx, disy
            
    def check(self):
        self.xm, self.ym = self.turtle_move.pos()
        self.cx, self.cy = self.turtle_click.pos()
        self.turtle_z.seth(90)
        dx, dy = self.distance_btw_p_2(self.xz, self.yz, self.cx, self.cy)
        print(dx, dy)
        
    def loop(self):
        listener = pynput.mouse.Listener(on_move= self.on_move, on_click= self.on_click)
        listener.start()
        while True:
            self.turtle_move.goto(self.xx, -self.yy)
            self.turtle_click.goto(self.xc, self.yc)
            self.check()
    def run(self):
        self.loop()
        
run = callibrate()
run.run()
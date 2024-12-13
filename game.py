import player
import gri_d
import hat
import math
import turtle
import pynput # for mouse listener

#canvas
class Run:
    def __init__(self):
        turtle.screensize(500, 500)
        self.playerb = "D:\Cmand\Py\Final-proj\playerb.gif"
        self.screen = turtle.Screen()
        self.screen.addshape(self.playerb)
        self.main_player = turtle.Turtle(self.playerb)
        # grid
        self.tugrid = turtle.Turtle()
        self.mphat = turtle.Turtle()
        self.detect_mouse = turtle.Turtle()
        self.player_size = 30
        self.player_stroke = 3
        self.player_control = player.Player(self.main_player, strk= self.player_stroke, size = self.player_size)
        self.tugrid_control = gri_d.draw_grid(self.tugrid)
        self.hat_control = hat.hat_move(self.mphat, py_size = self.player_size, py_stroke= self.player_stroke)
        self.xx = 0
        self.yy = 0
        
    def on_move(self, x, y):
        self.xx, self.yy = x, y
        
    def angle_btw_p(self, x1, y1, x2, y2):
        ang = math.atan2(y2- y1, x2 - x1)
        if ang < 0:
            ang += math.pi * 2
        return ang
    
    def distance_btw_p(self, x1, y1, x2, y2):
        dist = math.sqrt((abs(x1-x2))+(abs(y1-y2)))
        return dist
    
    def __redraw(self):
        turtle.clear()
        self.hat_control.clear()
        turtle.update()
    
    def move(self):
        # detect mouse
        listener = pynput.mouse.Listener(on_move= self.on_move)
        listener.start()
        # turtle part
        while True:
            self.detect_mouse.penup()
            self.detect_mouse.goto(self.xx - 965, -self.yy + 575)
            #self.detect_mouse.write(str(self.xx - 965)+","+str(-self.yy + 575))
            x_pos, y_pos = self.main_player.pos()
            dist = self.distance_btw_p(x_pos , y_pos , self.xx - 965 , -self.yy + 575)
            #print(x_pos, y_pos)
            #angle and movement
            angle = self.angle_btw_p(x_pos , y_pos , self.xx - 965 , -self.yy + 575)
            #self.detect_mouse.write(str(angle))
            #self.main_player.write(str(x_pos)+","+str(y_pos)) 
            self.hat_control.set_loma(x_pos + ((2*self.player_size) * math.cos(angle)), y_pos + ((2*self.player_size) * math.sin(angle)), (angle*180/math.pi))
            self.player_control.set_location(self.xx - 965, -self.yy + 575, dist, (angle*180/math.pi))
    
    def run(self):
        #self.player_control.draw()
        self.tugrid_control.draw()
        self.hat_control.draw()
        self.move()
        self.__redraw()
        turtle.mainloop()
    
run1 = Run()
run1.run()
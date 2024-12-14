import player
import gri_d
import hat
import arrow
import math
import turtle
import pynput # for mouse listener

#canvas
class Run:
    def __init__(self):
        turtle.screensize(500, 500)
        self.playerb = "D:\Cmand\Py\Final-proj\playerb.gif"
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.screen.title("BallZa-YamahaWave100")
        #self.screen.tracer(0)
        self.screen.addshape(self.playerb)
        self.main_player = turtle.Turtle(self.playerb)
        # turtle
        self.tugrid = turtle.Turtle()
        self.mphat = turtle.Turtle()
        self.detect_mouse = turtle.Turtle()
        self.arrow = turtle.Turtle()
        # adjust
        self.player_size = 25
        self.player_stroke = 2
        self.boarder_size = 2000
        self.bd_hw = self.boarder_size / 2
        # set
        self.player_control = player.Player(self.main_player, strk= self.player_stroke, size = self.player_size)
        self.tugrid_control = gri_d.draw_grid(self.tugrid, self.boarder_size)
        self.hat_control = hat.hat_move(self.mphat, py_size = self.player_size, py_stroke= self.player_stroke)
        self.arrow_control = arrow.Arrow(self.arrow)
        self.xx = 0
        self.yy = 0
        self.xc = 0
        self.yc = 0
        
    def on_move(self, x, y):
        self.xx, self.yy = x, y
        
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.xc, self.yc = x, y
        
    def boarder_check(self):
        x, y = self.tugrid.pos()
        x += 17
        #print(x, y)
        if x <= -self.boarder_size:
            self.camera(0, self.disty/6)
            self.tugrid_control.set_loma(x+20, y)
        if x >= 0:
            self.camera(0, self.disty/6)
            self.tugrid_control.set_loma(x-20, y)
        if y <= -self.boarder_size:
            self.camera(self.distx/6, 0)
            self.tugrid_control.set_loma(x, y+20)
        if y >= 0:
            self.camera(self.distx/6, 0)
            self.tugrid_control.set_loma(x, y-20)
        if 0 > x > -self.boarder_size and 0 > y > -self.boarder_size:
            self.camera(self.distx/6, self.disty/6)
        pass
        
    def angle_btw_p(self, x1, y1, x2, y2):
        ang = math.atan2(y2- y1, x2 - x1)
        if ang < 0:
            ang += math.pi * 2
        return ang
    
    def distance_btw_p(self, x1, y1, x2, y2):
        dist = math.sqrt((abs(x1-x2))+(abs(y1-y2)))
        return dist
    
    def distance_btw_p_2(self, x1, y1, x2, y2):
        disx = x2 - x1
        disy = y2 - y1
        return disx, disy
    
    def arrow_adj(self):
        self.arrow.penup()
        self.arrow.goto(self.xc - 965, -self.yc + 575)
    
    def camera(self, x, y):
        # grid
        x_grid, y_grid = self.tugrid.pos()
        self.tugrid_control.set_loma(x_grid - x, y_grid - y)
        pass
    
    def __redraw(self):
        turtle.clear()
        self.hat_control.clear()
        turtle.update()
    
    def move(self):
        # detect mouse
        listener = pynput.mouse.Listener(on_move= self.on_move, on_click= self.on_click)
        listener.start()        
        #liscliker.start()
        # turtle part
        while True:
            self.detect_mouse.penup()
            self.detect_mouse.goto(self.xx - 965, -self.yy + 575)
            x_pos, y_pos = self.main_player.pos()
            dist = self.distance_btw_p(x_pos , y_pos , self.xx - 965 , -self.yy + 575)
            self.distx, self.disty = self.distance_btw_p_2(x_pos, y_pos, self.xx - 965 , -self.yy + 575)
            angle = self.angle_btw_p(x_pos , y_pos , self.xx - 965 , -self.yy + 575)
            self.hat_control.set_loma(x_pos + ((2*self.player_size) * math.cos(angle)), y_pos + ((2*self.player_size) * math.sin(angle)), (angle*180/math.pi))
            self.player_control.set_location(self.xx - 965, -self.yy + 575, dist, (angle*180/math.pi))
            self.boarder_check()
            self.arrow_adj()
    
    def run(self):
        #self.player_control.draw()
        self.tugrid_control.draw()
        self.hat_control.draw()
        self.move()
        self.__redraw()
        turtle.mainloop()
        turtle.done()
    
run1 = Run()
run1.run()
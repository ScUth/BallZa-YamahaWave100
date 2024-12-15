# FOR TEST ONLY

import player
import gri_d
import hat
import arrow
import senemy
import math
import turtle
import pynput # for mouse listener
import random

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
        self.arrow_shooter = turtle.Turtle()
        self.enm1 = turtle.Turtle()
        self.enm2 = turtle.Turtle()
        self.enm3 = turtle.Turtle()
        self.enm4 = turtle.Turtle()
        self.enm5 = turtle.Turtle()
        #self.test = turtle.Turtle() #for test only
        # adjust
        self.player_size = 25
        self.player_stroke = 2
        self.boarder_size = 2000
        self.bd_hw = self.boarder_size / 2
        #self.test.color("red")
        #self.test.penup()
        # set
        self.player_control = player.Player(self.main_player, strk= self.player_stroke, size = self.player_size)
        self.tugrid_control = gri_d.draw_grid(self.tugrid, self.boarder_size)
        self.hat_control = hat.hat_move(self.mphat, py_size = self.player_size, py_stroke= self.player_stroke)
        self.arrow_control = arrow.Arrow(self.arrow_shooter)
        self.xx = 0 # cursor location
        self.yy = 0 # cursor location
        self.xc = 0 # clicker location
        self.yc = 0 # clicker location
        self.sxlp = 0 # Player simulation location
        self.sylp = 0 # Player simulation location
        self.x_pos, self.y_pos = self.main_player.pos()
        self.es1x, self.es1y = self.enm1.pos()
        self.es2x, self.es2y = self.enm2.pos()
        self.es3x, self.es3y = self.enm3.pos()
        self.es4x, self.es4y = self.enm4.pos()
        self.es5x, self.es5y = self.enm5.pos()
        self.fire = False
        self.arrow_speed = 100
        self.shooter_on_board = False
        #enemy default setting
        
    def set_daf_ene(self):
        print("set enermy")
        self.es1 = senemy.enemy_setting(self.enm1, self.bd_hw)
        self.es2 = senemy.enemy_setting(self.enm2, self.bd_hw)
        self.es3 = senemy.enemy_setting(self.enm3, self.bd_hw)
        self.es4 = senemy.enemy_setting(self.enm4, self.bd_hw)
        self.es5 = senemy.enemy_setting(self.enm5, self.bd_hw)
        self.es1x, self.es1y = self.es1.basic_set()
        self.es2x, self.es2y = self.es2.basic_set()
        self.es3x, self.es3y = self.es3.basic_set()
        self.es4x, self.es4y = self.es4.basic_set()
        self.es5x, self.es5y = self.es5.basic_set()
        pass
    
    def enemy_adj(self, x, y):
        # Adjust position
        self.es1x, self.es1y = self.enm1.pos()
        self.es2x, self.es2y = self.enm2.pos()
        self.es3x, self.es3y = self.enm3.pos()
        self.es4x, self.es4y = self.enm4.pos()
        self.es5x, self.es5y = self.enm5.pos()
        x_grid, y_grid = self.tugrid.pos()
        for enemy, xi, yi in [
            (self.enm1, self.es1x, self.es1y),
            (self.enm2, self.es2x, self.es2y),
            (self.enm3, self.es3x, self.es3y),
            (self.enm4, self.es4x, self.es4y),
            (self.enm5, self.es5x, self.es5y),
        ]:
            
            enemy.goto(xi - x, yi - y)
    
    def on_move(self, x, y):
        self.xx, self.yy = x, y
        
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.fire = True
            self.xc, self.yc = x, y
            if self.shooter_on_board is True:
                #self.shooter_on_board = False
                #self.arrow_shooter.goto(self.x_pos, self.y_pos)
                self.shooter_on_board = False
        
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
    
    def arrow_adj(self, x, y):
        self.arrow.penup()
        self.arrow_shooter.penup()
        xcc, ycc = self.arrow.pos()
        xs, ys = self.arrow_shooter.pos()
        #print(xs, ys)
        x_pos, y_pos = self.main_player.pos()
        x_grid, y_grid = self.tugrid.pos()
        angle = self.angle_btw_p(x_pos, y_pos, self.xc - 965, -self.yc + 575)
        #print(xcc, ycc)
        if self.fire is True and self.shooter_on_board is False:
            self.arrow_shooter.goto(x_pos, y_pos)
            self.arrow.goto(self.xc - 965, -self.yc + 575)
            #print(angle * 180 / math.pi)
            self.shooter_on_board = True
            self.fire = False
        elif self.fire is False and self.shooter_on_board is True:
            self.arrow.goto(xcc - x, ycc - y)
            self.arrow_shooter.goto(xs - x, ys - y)
            self.arrow_control.fire(angle * 180 / math.pi, self.arrow_speed)
            #if 45 < angle < 225:
            #    # base on boarder position. x is the same but y + self.boarder_size
            #    if xs >= x_grid and ys <= y_grid + self.boarder_size:
            #        self.arrow_shooter.clear()
            #        self.shooter_on_board = False
            #if 225 < angle < 405:
            #    if xs <= x_grid + self.boarder_size and ys >= y_grid:
            #        self.arrow_shooter.clear()
            #        self.shooter_on_board = False
        elif self.fire is False and self.shooter_on_board is False:
            self.arrow_shooter.goto(x_pos, y_pos)
            self.arrow.goto(xcc - x, ycc - y)
    
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
            x_grid, y_grid = self.tugrid.pos()
            # distance between cursor and player
            dist = self.distance_btw_p(self.x_pos , self.y_pos , self.xx - 965 , -self.yy + 575)
            # x and y distance between cursor and player
            self.distx, self.disty = self.distance_btw_p_2(self.x_pos, self.y_pos, self.xx - 965 , -self.yy + 575)
            # angle between player and cursor
            angle = self.angle_btw_p(self.x_pos , self.y_pos , self.xx - 965 , -self.yy + 575)
            # simulation location of player (Exactly location)
            self.sxlp = -(x_grid + (self.boarder_size / 2))
            self.sylp = -(y_grid + (self.boarder_size / 2))
            #print(sxlp, sylp)
            self.enemy_adj(self.distx/6, self.disty/6)
            self.hat_control.set_loma(self.x_pos + ((2*self.player_size) * math.cos(angle)), self.y_pos + ((2*self.player_size) * math.sin(angle)), (angle*180/math.pi))
            self.player_control.set_location(self.xx - 965, -self.yy + 575, dist, (angle*180/math.pi))
            self.boarder_check()
            self.arrow_adj(self.distx/6, self.disty/6)
            #print(x_grid, y_grid, self.distx/6, self.disty/6)
            #self.test.goto((self.xc - 965), (- self.yc + 575))
            #a, b = self.arrow_shooter.pos()
            #self.arrow_shooter.clear()
            #print(self.shooter_on_board)
            
    
    def run(self):
        #self.player_control.draw()
        self.tugrid_control.draw()
        self.hat_control.draw()
        print("call set emermy")
        self.set_daf_ene()
        self.move()
        self.__redraw()
        turtle.mainloop()
        turtle.done()
    
run1 = Run()
run1.run()
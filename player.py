import turtle
import math

#player
class Player:
    def __init__(self, main_player, strk:int, size):
        self.mainplayer = main_player
        self.size = size # not use
        self.pensize = strk
    
    def draw(self):
        pass
        
    def Move(self, dist, ang):
        # speed is directly proportional to distance btw mouse and player
        pass
    
    def set_location(self, x, y, dist, ang):
        self.mainplayer.speed(0)
        self.mainplayer.clear()
        self.mainplayer.penup()
        #self.mainplayer.goto(x, y)
        self.mainplayer.seth(ang)
        self.mainplayer.forward(dist)
        #
        self.mainplayer.pendown()
        
        # redraw
            #self.mainplayer.speed(0)
            #self.mainplayer.penup()
            #self.mainplayer.seth(ang)
            #self.mainplayer.pendown()
            #self.mainplayer.width(self.pensize)
            #self.mainplayer.circle(self.size)
            #self.mainplayer.penup()
            #self.mainplayer.seth(ang)
            #self.mainplayer.forward(self.size)
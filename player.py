import turtle
import math

#player
class Player:
    def __init__(self, main_player, strk:int, size):
        self.mainplayer = main_player
        self.size = size # not use
        self.pensize = strk

    def clear(self):
        self.mainplayer.clear()
    
    def set_location(self, x, y, dist, ang):
        self.mainplayer.speed(0)
        self.mainplayer.clear()
        self.mainplayer.penup()
        self.mainplayer.pendown()
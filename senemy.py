import turtle
import random

class enemy_setting:
    def __init__(self, enemy, size):
        self.enemy = enemy
        self.bdsize = size
    
    def basic_set(self):
        self.enemy.shape('circle')
        self.enemy.shapesize(3)
        self.enemy.color("orange")
        self.enemy.penup()
        # Set random position
        self.enemy.goto(random.randint(-self.bdsize, self.bdsize),
                        random.randint(-self.bdsize, self.bdsize))
        x, y = self.enemy.pos()
        #print(x,y)
        return x, y
        
    def set_loma(self, x, y):
        self.enemy.goto(x, y)
from random import random

class City(object):
    def __init__(self, x=0, y=0, create_random=False):
        self.x = x
        self.y = y
        
        if create_random:
            self.x = int(round(random() * 200))
            self.y =  int(round(random() * 200))
    
    def distance_to(self, city):
        import math
        
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
        
        return distance
    
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
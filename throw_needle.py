import random
import math
from math import pi
class needle():
    fromY = 20
    length = 5
    angle = 2
    endY = 0
    def __init__(self):
        self.fromY = random.randint(0,100)
        self.angle = random.uniform(0.0,2.0)*pi
        self.endY = self.fromY+self.length*math.cos(self.angle)

def isIntersect(needle):
    a=needle.fromY
    b=needle.endY
    o=(a+b)/2
    #if o==a and o==b and o%10 !=0:
    #    return False
    if o%10<=abs(needle.length*math.sin(needle.angle)):
        return True
    #elif (10-o%10)<=abs(needle.length*math.sin(needle.angle)):
    #    return True
    else:
        return False
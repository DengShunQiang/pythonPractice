import random
import math
class needle():
	"""’Î"""
	fromY = 0
	length = 5
	angle = 0
	endY = 0
	def _init_(self):
		self.fromY = random.randomint(0,101)
		self.angle = random.randomint(0,3)*math.pi/180
		self.endY = self.fromY+self.length*math.sin(self.angle)

def isIntersect(needle):
        a = needle.fromY
        b = needle.endY
        if a<10&&b>10:
                return false
        elif a<20&&b>20:
                return false
        elif a<30&&b>30:
                return false
        elif a<40&&b>40:
                return false
        elif a<50&&b>50:
                return false
        elif a<60&&b>60:
                return false
        elif a<70&&b>70:
                return false
        elif a<80&&b>80:
                return false
        elif a<90&&b>90:
                return false
        elif a<100&&b>100:
                return false
        else return true
        
        

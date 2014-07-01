import sys 
sys.path.append("E:\pythonFile\practiceFiles\throw_needle.py")
import math
import throw_needle

c=0
n=100000
for i in range(0,100001):
	needle_test = throw_needle.needle()
	if  throw_needle.isIntersect(needle_test) is True:
		c=c+1
s=float(n)/float(c)
print "non-paralle times:"+str(c)+"\n"
print "n/c="+str(s)

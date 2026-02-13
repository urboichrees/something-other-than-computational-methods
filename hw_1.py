import sys
import math

h=float(sys.argv[1])
a=9.81
t=math.sqrt(h*2/a)
print("the time it takes for the ball to hit the ground at height h in meters is",t,"seconds")
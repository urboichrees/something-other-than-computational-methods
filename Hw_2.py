import sys
import math

x=float(sys.argv[1])
v=float(sys.argv[2])

LF=1/math.sqrt(1-v**2)
ET=x/v
ST=ET/LF

print("Earth Travel Time:",ET,"years")
print("Ship Travel Time:",ST,"years")
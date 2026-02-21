import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("x", type=float, help="Distance to planet in Lightyears")
parser.add_argument("v", type=float, help="Speed as a fraction of the speed of light (c)"))

args = parser.parse_args()

x = args.x
v = args.v

LF=1/math.sqrt(1-v**2)
ET=x/v
ST=ET/LF

print("Earth Travel Time:",ET,"years")
print("Ship Travel Time:",ST,"years")
import numpy as np
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser(description = "Projectile With Air Resistance")

parser.add_argument("--v0", type=float, default=100, help="initial velocity")
parser.add_argument("--angle", type=float, default=30, help="angle in degrees")
parser.add_argument("--h", type=float, default=0.01, help="time step")
parser.add_argument("--tmax", type=float, default=20, help="max simulation time")

args = parser.parse_args()


# constants
g = 9.81
m = 1.0
R = 0.08
rho = 1.22
C = 0.47

#air resistance 
k = np.pi * R**2 * rho * C / (2 * m)

#initial Conditions 
v0 = args.v0
angle = np.radians(args.angle)
x0 = 0
y0 = 0
vx0 = v0 * np.cos(angle)
vy0 = v0 * np.sin(angle)

r = np.array([x0, y0, vx0, vy0])

# time setup
h = args.h
tmax = args.tmax
N = int(tmax / h)

#data storage
xs = []
ys = []

#positional function basically same setup as before
def f(r, t):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]

    v = np.sqrt(vx**2 + vy**2)

    dxdt = vx
    dydt = vy
    dvxdt = -k * vx * v
    dvydt = -g - k * vy * v

    return np.array([dxdt, dydt, dvxdt, dvydt])

for i in range(N):
    t = i * h
    xs.append(r[0])
    ys.append(r[1])

#just condition of hitting ground
    if r[1] < 0:
        break

#runge kutta same as pendulum 
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5*k1, t + 0.5*h)
    k3 = h * f(r + 0.5*k2, t + 0.5*h)
    k4 = h * f(r + k3, t + h)

    r += (k1 + 2*k2 + 2*k3 + k4)/6

plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Projectile with Air Resistance")
plt.show()
import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

parser = argparse.ArgumentParser(description="Electric potential and electric field from two charges")
parser.add_argument("--spacing", type=float, default=0.01, help="Grid spacing in meters")
parser.add_argument("--step", type=float, default=1e-5, help="Step size for numerical derivative")
args = parser.parse_args()

x = np.arange(-0.5, 0.5, args.spacing)
y = np.arange(-0.5, 0.5, args.spacing)
X, Y = np.meshgrid(x, y)

k = 1 / (4 * np.pi * constants.epsilon_0)

q1 = 1.0
q2 = -1.0

r1 = (-0.05, 0.0)
r2 = (0.05, 0.0)

distancepos = np.sqrt((X - r1[0])**2 + (Y - r1[1])**2)
distanceneg = np.sqrt((X - r2[0])**2 + (Y - r2[1])**2)

distancepos[distancepos == 0] = 1e-12
distanceneg[distanceneg == 0] = 1e-12

Epotpos = (q1 / distancepos) * k
Epotneg = (q2 / distanceneg) * k
phi = Epotpos + Epotneg

plt.figure()
plt.contourf(X, Y, phi, levels=50)
plt.colorbar(label="Electric Potential (V)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Electric Potential of Two Charges")

def potential(x, y):
    distancepos = np.sqrt((x - r1[0])**2 + (y - r1[1])**2)
    distanceneg = np.sqrt((x - r2[0])**2 + (y - r2[1])**2)

    distancepos = np.where(distancepos == 0, 1e-12, distancepos)
    distanceneg = np.where(distanceneg == 0, 1e-12, distanceneg)

    Epotpos = (q1 / distancepos) * k
    Epotneg = (q2 / distanceneg) * k

    return Epotpos + Epotneg

h = args.step
dfdx = (potential(X + h/2, Y) - potential(X - h/2, Y)) / h
dfdy = (potential(X, Y + h/2) - potential(X, Y - h/2)) / h

plt.figure()
plt.quiver(X, Y, -dfdx, -dfdy)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Electric Field of Two Charges")
plt.axis("equal")
plt.show()
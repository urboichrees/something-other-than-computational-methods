import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import argparse

# argparse setup
parser = argparse.ArgumentParser(description="Brownian motion simulation")

parser.add_argument("--steps", type=int, default=1000000,
                    help="Number of steps")
parser.add_argument("--size", type=int, default=101,
                    help="Lattice size")
parser.add_argument("--output", type=str, default="brownian.gif",
                    help="Output GIF filename")

args = parser.parse_args()

L = args.size
N = args.steps

Path = []

# start at center
x = L // 2
y = L // 2

Path.append((x, y))

rng = np.random.default_rng(seed=None)

# simulation
for step in range(N):
    moved = False

    while not moved:
        direction = rng.integers(0, 4)

        new_x = x
        new_y = y

        if direction == 0:
            new_y += 1
        elif direction == 1:
            new_y -= 1
        elif direction == 2:
            new_x += 1
        else:
            new_x -= 1

        if 0 <= new_x < L and 0 <= new_y < L:
            x = new_x
            y = new_y
            moved = True

    Path.append((x, y))

# separate coordinates
x_vals = [p[0] for p in Path]
y_vals = [p[1] for p in Path]

# plot setup
fig, ax = plt.subplots()
ax.set_xlim(0, L - 1)
ax.set_ylim(0, L - 1)
ax.set_title("Brownian Motion")
ax.set_xlabel("x")
ax.set_ylabel("y")

line, = ax.plot([], [])

def update(frame):
    line.set_xdata(x_vals[:frame])
    line.set_ydata(y_vals[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x_vals), interval=50)

writergif = PillowWriter(fps=30)
ani.save(args.output, writer=writergif)
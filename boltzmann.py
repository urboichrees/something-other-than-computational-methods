import numpy as np
import argparse
from scipy import constants

def f(x):
    if x == 0:
        return 0
    return x**3 / (np.exp(x) - 1)

parser = argparse.ArgumentParser(
    description="Computes the blackbody integral with Simpson's rule and use it to estimate the Stefan-Boltzmann constant."
)

parser.add_argument(
    "--L",
    type=float,
    required=True,
    help="Upper limit used to approximate infinity since simpson need a finite inteval #truncate."
)

parser.add_argument(
    "--N",
    type=int,
    required=True,
    help="Number of intervals for Simpson's rule (must be even)."
)

args = parser.parse_args()

L = args.L
N = args.N
a = 0
b = L

if N % 2 != 0:
    raise ValueError("N must be even for Simpson's rule.")

h = (b - a) / N
s = f(a) + f(b)

for i in range(1, N):
    x = a + i * h
    if i % 2 == 1:
        s += 4 * f(x)
    else:
        s += 2 * f(x)

integral = (h / 3) * s

sigma = (constants.k**4 / (4 * np.pi**2 * constants.c**2 * constants.hbar**3)) * integral

print("Integral =", integral)
print("Stefan-Boltzmann constant =", sigma)
import numpy as np
import matplotlib.pyplot as plt
import argparse


# Argument Parser
parser = argparse.ArgumentParser(description="Finite Square Well Energy Levels")

parser.add_argument("--V", type=float, default=20, help="Potential height in eV")
parser.add_argument("--w", type=float, default=1e-9, help="Width of well in meters")

args = parser.parse_args()

# Constants (from args)
eV = 1.602e-19
V = args.V
V_J = V * eV

m = 9.11e-31
hbar = 1.055e-34
w = args.w


# Functions
def f_even(E):
    E_J = E * eV
    return np.tan(np.sqrt((w**2 * m * E_J) / (2 * hbar**2))) - np.sqrt((V_J - E_J) / E_J)

def f_odd(E):
    E_J = E * eV
    return np.tan(np.sqrt((w**2 * m * E_J) / (2 * hbar**2))) + np.sqrt(E_J / (V_J - E_J))


# Bisection
def bisection(f, a, b, tol=1e-3):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("No root in this interval")
        return None

    while abs(b - a) > tol:
        c = (a + b) / 2
        fc = f(c)

        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc

    return (a + b) / 2


# Plot
E = np.linspace(0.001, V - 0.001, 1000)
E_J = E * eV

y1 = np.tan(np.sqrt((w**2 * m * E_J) / (2 * hbar**2)))
y2 = np.sqrt((V_J - E_J) / E_J)
y3 = -np.sqrt(E_J / (V_J - E_J))

plt.plot(E, y1, label="tan(...)")
plt.plot(E, y2, label="sqrt((V-E)/E)")
plt.plot(E, y3, label="-sqrt(E/(V-E))")

plt.ylim(-10, 10)
plt.xlabel("Energy (eV)")
plt.ylabel("Function value")
plt.legend()
plt.grid()
plt.title("Finite Square Well")

plt.show()

# Energy Levels
E1 = bisection(f_odd, 1.2, 1.3)
E2 = bisection(f_even, 2.5, 2.9)
E3 = bisection(f_odd, 4.7, 5.2)
E4 = bisection(f_even, 7.5, 7.9)
E5 = bisection(f_odd, 11.0, 11.3)
E6 = bisection(f_even, 14.9, 15.1)
E7 = bisection(f_odd, 19.0, 19.2)

print("\nEnergy Levels (eV):")
print(f"E1 (odd)  = {E1:.3f}")
print(f"E2 (even) = {E2:.3f}")
print(f"E3 (odd)  = {E3:.3f}")
print(f"E4 (even) = {E4:.3f}")
print(f"E5 (odd)  = {E5:.3f}")
print(f"E6 (even) = {E6:.3f}")
print(f"E7 (odd)  = {E7:.3f}")
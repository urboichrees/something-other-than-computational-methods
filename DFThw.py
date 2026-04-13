import numpy as np
import matplotlib.pyplot as plt
from cmath import exp, pi
import argparse

# this is the dft code from the lecture. but here we create a function that uses the signal y as an input.
def dft(y):
    # this shows us how many data points we have in our signal y and sets its to N
    N = len(y)

    # this creates an array filled with zeros and then fills it with an integer division model that drops the decimal and adds 1.
    # we're using 501 coefficients because the second half of the coefficients mirror the first half. so 0 to 500 = 501 real values
    # also the whole complex part is needed because our coef have both real and imaginary parts so we're just stating that.
    c = np.zeros(N//2 + 1, dtype=complex)

    # going through all the values in the frequency k for the range: N//2 + 1 testing them
    for k in range(N//2 + 1):
        # this goes through every single data point, also combining both loops just cycles for each frequency k we scan the ENTIRE signal
        for n in range(N):
            # y[n] is our signal at point n in which we multiply by the big exp which is a wave with frequency k.
            # we use += to add onto our current value. so in its entirety we compare the signal of the wave at this point
            # and then accumulate them to see how well they match across the whole signal and add them to our sum
            c[k] += y[n] * exp(-2j * pi * k * n / N)

    # returns the fourier coefficients
    return c

# this is just the argparse memes
parser = argparse.ArgumentParser(
    description="Compute DFT of different signals"
)

parser.add_argument(
    "signal",
    choices=["square", "saw", "mod"],
    help="Choose signal: square, saw, or mod"
)

args = parser.parse_args()

# sets up the 1000 evenly spaced points
N = 1000

# allows me to sample each of the 1k points in an array
n = np.arange(N)

# choose which signal to use
if args.signal == "square":
    # sets an array with values of one with 1k
    y = np.ones(N)
    # this cuts the N in half and starts at index 500, replaces everything from then onward as -1. important for a square wave.
    y[N//2:] = -1
    signal_title = "Square Wave"

elif args.signal == "saw":
    # sawtooth wave input value from the assignment
    y = n
    signal_title = "Sawtooth Wave"

elif args.signal == "mod":
    # modulated sine wave part
    y = np.sin(np.pi * n / N) * np.sin(20 * np.pi * n / N)
    signal_title = "Modulated Sine Wave"

# takes the signal y and feeds it into the dft function and then stores it as this new variable c
c = dft(y)

# we need the amplitudes to be the real size of the coefficient, since it may be a complex number we can use the abs function to store it real
amp = np.abs(c)

# this shows the first graph before transforming it
plt.figure()
plt.plot(n, y)
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title(signal_title)
plt.show()

# this plots the fourier transforms
plt.figure()
plt.plot(amp)
plt.xlabel("k")
plt.ylabel("|c[k]|")
plt.title("Fourier amplitudes of the " + signal_title)
plt.show()
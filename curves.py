import argparse
import numpy as np
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description="Plot special curves.")
    parser.add_argument("--points", type=int, default=5000)
    return parser.parse_args()

def main():
    args = parse_args()

    #our subplots which was a pain to learn
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # deltoid
    theta1 = np.linspace(0, 2*np.pi, args.points, endpoint=False)
    x1 = 2*np.cos(theta1) + np.cos(2*theta1)
    y1 = 2*np.sin(theta1) - np.sin(2*theta1)

    axs[0].plot(x1, y1)
    axs[0].set_title("Deltoid")
    axs[0].axis("equal")

    #spiral
    theta2 = np.linspace(0, 10*np.pi, args.points)
    r2 = theta2**2
    x2 = r2 * np.cos(theta2)
    y2 = r2 * np.sin(theta2)

    axs[1].plot(x2, y2)
    axs[1].set_title("Spiral")
    axs[1].axis("equal")

    #fey
    theta3 = np.linspace(0, 24*np.pi, args.points)
    r3 = np.exp(np.cos(theta3)) - 2*np.cos(4*theta3) + (np.sin(theta3/12))**5
    x3 = r3 * np.cos(theta3)
    y3 = r3 * np.sin(theta3)

    axs[2].plot(x3, y3)
    axs[2].set_title("Fey")
    axs[2].axis("equal")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
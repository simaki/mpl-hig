import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
import mpl_hig


def brown(*shape):
    a = np.random.randn(*shape)
    a[0] = 0
    return a.cumsum(0)


if __name__ == "__main__":
    mpl_hig.set("whitegrid")

    np.random.seed(42)

    a = brown(1000, 9)

    plt.figure(figsize=(10, 4))
    for i in range(9):
        plt.plot(a[:, i], label=f"line {i + 1}")

    plt.legend()
    plt.title("Brownian Motions")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.savefig("line.png")

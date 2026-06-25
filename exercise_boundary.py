"""
exercise_boundary.py

Plots the early exercise boundary for an American put option
using the Cox-Ross-Rubinstein (CRR) binomial tree.

"""

import os
import math
import matplotlib.pyplot as plt


def compute_exercise_boundary(
    S0=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.25,
    steps=200,
):
    """
    Build a CRR tree and identify the nodes where
    immediate exercise is optimal.
    """

    dt = T / steps

    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u

    p = (math.exp(r * dt) - d) / (u - d)
    discount = math.exp(-r * dt)

    # -----------------------
    # Stock Price Tree
    # -----------------------

    stock_tree = []

    for i in range(steps + 1):

        level = []

        for j in range(i + 1):

            price = S0 * (u ** j) * (d ** (i - j))

            level.append(price)

        stock_tree.append(level)

    # -----------------------
    # Terminal Payoff
    # -----------------------

    option_tree = [[] for _ in range(steps + 1)]

    option_tree[-1] = [
        max(K - s, 0)
        for s in stock_tree[-1]
    ]

    boundary_time = []
    boundary_price = []

    # -----------------------
    # Backward Induction
    # -----------------------

    for i in range(steps - 1, -1, -1):

        current = []

        exercise_prices = []

        for j in range(i + 1):

            continuation = discount * (
                p * option_tree[i + 1][j + 1]
                + (1 - p) * option_tree[i + 1][j]
            )

            exercise = max(
                K - stock_tree[i][j],
                0,
            )

            value = max(
                continuation,
                exercise,
            )

            current.append(value)

            if exercise > continuation + 1e-12:
                exercise_prices.append(
                    stock_tree[i][j]
                )

        option_tree[i] = current

        if exercise_prices:

            boundary_time.append(i * dt)

            boundary_price.append(
                max(exercise_prices)
            )

    return boundary_time, boundary_price


def plot_boundary():

    print("=" * 60)
    print("Generating Exercise Boundary")
    print("=" * 60)

    t, s = compute_exercise_boundary()

    os.makedirs(
        "figures",
        exist_ok=True,
    )

    plt.figure(
        figsize=(9, 6)
    )

    plt.plot(
        t,
        s,
        linewidth=2.5,
        marker="o",
        markersize=4,
    )

    plt.grid(True)

    plt.xlabel(
        "Time (Years)"
    )

    plt.ylabel(
        "Stock Price"
    )

    plt.title(
        "Early Exercise Boundary for an American Put"
    )

    plt.tight_layout()

    filename = (
        "figures/exercise_boundary.png"
    )

    plt.savefig(
        filename,
        dpi=300,
    )

    print()

    print(
        "Exercise boundary saved as:"
    )

    print(filename)

    plt.show()


if __name__ == "__main__":

    plot_boundary()
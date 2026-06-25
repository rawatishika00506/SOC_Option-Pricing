"""
price_surface.py

Generates a 3D price surface for an American put option using the
Cox-Ross-Rubinstein (CRR) binomial tree model.

The figure illustrates how the option price changes with
1. Initial stock price (S0)
2. Time to maturity (T)

"""

import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from crr_option_pricing import crr_put_price


def generate_surface():
    """
    Generate and save the American put price surface.
    """

    K = 100
    r = 0.05
    sigma = 0.25
    steps = 200

    stock_prices = np.linspace(60, 140, 25)
    maturities = np.linspace(0.05, 2.0, 20)

    S_grid, T_grid = np.meshgrid(stock_prices, maturities)

    option_prices = np.zeros_like(S_grid)

    print("=" * 70)
    print("Generating American Put Price Surface")
    print("=" * 70)

    for i in range(len(maturities)):
        for j in range(len(stock_prices)):

            option_prices[i, j] = crr_put_price(
                S0=stock_prices[j],
                K=K,
                T=maturities[i],
                r=r,
                sigma=sigma,
                steps=steps,
                american=True,
            )

    figures_dir = "figures"

    os.makedirs(figures_dir, exist_ok=True)

    fig = plt.figure(figsize=(10, 7))

    ax = fig.add_subplot(111, projection="3d")

    surface = ax.plot_surface(
        S_grid,
        T_grid,
        option_prices,
        cmap="viridis",
        edgecolor="none",
        alpha=0.9,
    )

    ax.set_xlabel("Initial Stock Price (S₀)")
    ax.set_ylabel("Time to Maturity (Years)")
    ax.set_zlabel("American Put Price")

    ax.set_title("American Put Price Surface (CRR Model)")

    fig.colorbar(
        surface,
        shrink=0.6,
        aspect=12,
        label="Option Price",
    )

    output_file = os.path.join(
        figures_dir,
        "price_surface.png",
    )

    plt.tight_layout()
    plt.savefig(output_file, dpi=300)

    print("\nSurface saved successfully.")
    print(f"Location: {output_file}")

    plt.show()


if __name__ == "__main__":
    generate_surface()
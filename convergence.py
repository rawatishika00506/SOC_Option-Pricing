
"""
convergence.py

Runs a convergence study for the CRR binomial model.
Generates a CSV table and a convergence plot for European and American puts.
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt

from crr_option_pricing import crr_put_price


OUTPUT_DIR = Path("tables")
FIGURE_DIR = Path("figures")
OUTPUT_DIR.mkdir(exist_ok=True)
FIGURE_DIR.mkdir(exist_ok=True)


def run_convergence():
    S0 = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.25

    step_sizes = [25, 50, 100, 200, 500, 1000]

    rows = []

    european_prices = []
    american_prices = []
    premiums = []

    print("=" * 70)
    print("CRR CONVERGENCE STUDY")
    print("=" * 70)

    for steps in step_sizes:

        european = crr_put_price(
            S0, K, T, r, sigma,
            steps,
            american=False,
        )

        american = crr_put_price(
            S0, K, T, r, sigma,
            steps,
            american=True,
        )

        premium = american - european

        european_prices.append(european)
        american_prices.append(american)
        premiums.append(premium)

        rows.append([
            steps,
            round(european, 6),
            round(american, 6),
            round(premium, 6),
        ])

        print(
            f"Steps = {steps:<5}"
            f" European = {european:.6f}"
            f" American = {american:.6f}"
            f" Premium = {premium:.6f}"
        )

    csv_file = OUTPUT_DIR / "convergence_table.csv"

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "Steps",
                "European Put",
                "American Put",
                "Early Exercise Premium",
            ]
        )
        writer.writerows(rows)

    plt.figure(figsize=(8, 5))
    plt.plot(step_sizes, european_prices, marker="o", label="European Put")
    plt.plot(step_sizes, american_prices, marker="s", label="American Put")
    plt.xlabel("Number of Binomial Steps")
    plt.ylabel("Option Price")
    plt.title("CRR Convergence")
    plt.grid(True)
    plt.legend()

    figure_file = FIGURE_DIR / "convergence.png"
    plt.tight_layout()
    plt.savefig(figure_file, dpi=300)

    print("\nConvergence table saved to:", csv_file)
    print("Figure saved to:", figure_file)

    print("\nInterpretation")
    print(
        "As the number of time steps increases, both prices stabilise. "
        "The American put consistently remains above the European put, "
        "and the gap converges to the early exercise premium."
    )


if __name__ == "__main__":
    run_convergence()

"""
tests.py

Finance-based sanity tests for the CRR option pricing model.

These tests are not formal unit tests. They are practical validation
checks that confirm the implementation behaves consistently with
financial theory.

"""

from crr_option_pricing import crr_put_price


def print_result(test_name, passed):
    """Print a formatted test result."""
    status = "PASS" if passed else "FAIL"
    print(f"{test_name:.<55} {status}")


def test_american_ge_european():
    """American put should never be worth less than a European put."""

    euro = crr_put_price(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.25,
        steps=500,
        american=False,
    )

    amer = crr_put_price(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.25,
        steps=500,
        american=True,
    )

    passed = amer >= euro

    print(f"European Put : {euro:.6f}")
    print(f"American Put : {amer:.6f}")
    print_result(
        "American put price >= European put price",
        passed,
    )

    return passed


def test_intrinsic_value():
    """
    American option should never be worth less than
    its intrinsic value.
    """

    stock_price = 90

    intrinsic = max(100 - stock_price, 0)

    amer = crr_put_price(
        S0=stock_price,
        K=100,
        T=1,
        r=0.05,
        sigma=0.25,
        steps=500,
        american=True,
    )

    passed = amer >= intrinsic

    print(f"Intrinsic Value : {intrinsic:.6f}")
    print(f"American Put    : {amer:.6f}")

    print_result(
        "American put >= intrinsic value",
        passed,
    )

    return passed


def test_put_decreases_as_stock_rises():
    """
    Put values should decrease as
    the underlying stock price increases.
    """

    prices = [80, 90, 100, 110, 120]

    values = []

    for s in prices:

        value = crr_put_price(
            S0=s,
            K=100,
            T=1,
            r=0.05,
            sigma=0.25,
            steps=500,
            american=True,
        )

        values.append(value)

    passed = all(
        values[i] >= values[i + 1]
        for i in range(len(values) - 1)
    )

    print("\nStock Price -> Put Value")

    for s, v in zip(prices, values):
        print(f"{s:>3} -> {v:.6f}")

    print_result(
        "Put value decreases as stock price increases",
        passed,
    )

    return passed


def test_put_increases_with_volatility():
    """
    Put values should increase
    when volatility increases.
    """

    vols = [0.10, 0.20, 0.30, 0.40]

    values = []

    for sigma in vols:

        value = crr_put_price(
            S0=100,
            K=100,
            T=1,
            r=0.05,
            sigma=sigma,
            steps=500,
            american=True,
        )

        values.append(value)

    passed = all(
        values[i] <= values[i + 1]
        for i in range(len(values) - 1)
    )

    print("\nVolatility -> Put Value")

    for vol, value in zip(vols, values):
        print(f"{vol:.2f} -> {value:.6f}")

    print_result(
        "Put value increases with volatility",
        passed,
    )

    return passed


def test_convergence():
    """
    Option prices should stabilise
    as the number of time steps increases.
    """

    steps = [100, 200, 500, 1000]

    prices = []

    for n in steps:

        value = crr_put_price(
            S0=100,
            K=100,
            T=1,
            r=0.05,
            sigma=0.25,
            steps=n,
            american=True,
        )

        prices.append(value)

    difference = abs(prices[-1] - prices[-2])

    passed = difference < 0.02

    print("\nSteps -> American Put")

    for n, value in zip(steps, prices):
        print(f"{n:>4} -> {value:.6f}")

    print_result(
        "Price converges as steps increase",
        passed,
    )

    return passed


def run_all_tests():
    """Run all sanity tests."""

    print("=" * 70)
    print("CRR OPTION PRICING SANITY TESTS")
    print("=" * 70)

    results = [
        test_american_ge_european(),
        test_intrinsic_value(),
        test_put_decreases_as_stock_rises(),
        test_put_increases_with_volatility(),
        test_convergence(),
    ]

    print("\n" + "=" * 70)

    passed = sum(results)

    print(f"Passed {passed} out of {len(results)} tests.")

    if passed == len(results):
        print("All sanity checks passed.")
    else:
        print("One or more tests failed. Review the implementation.")

    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
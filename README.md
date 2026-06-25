# Cox-Ross-Rubinstein (CRR) Option Pricing Model

## Project Overview

This project implements the **Cox-Ross-Rubinstein (CRR) Binomial Tree Model** for pricing both **European** and **American put options**. The implementation is written entirely in Python and demonstrates the fundamental concepts of option pricing, early exercise, convergence analysis, and model validation.

The project was completed as part of a quantitative finance assignment and is designed to be modular, reproducible, and easy to extend.

---

## Objectives

* Implement the CRR binomial tree from scratch.
* Price both European and American put options.
* Compute the early exercise premium.
* Verify theoretical option pricing properties using finance-based sanity tests.
* Study convergence of option prices as the number of tree steps increases.
* Visualize the American put price surface.
* Identify and plot the optimal early exercise boundary.

---

## Repository Structure

```text
SOC_Option-Pricing
│
├── Week4_CRR_Option_Pricing.ipynb
├── crr_option_pricing.py
├── convergence.py
├── tests.py
├── price_surface.py
├── exercise_boundary.py
│
├── figures/
│   ├── convergence.png
│   ├── price_surface.png
│   └── exercise_boundary.png
│
├── tables/
│   └── convergence_table.csv
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Methodology

The project uses the Cox-Ross-Rubinstein (CRR) binomial tree model to approximate option values under risk-neutral valuation.

For every time step:

* The stock price moves either upward or downward.
* Risk-neutral probabilities are used to discount expected future payoffs.
* American options additionally compare continuation value with immediate exercise value at every node.

The implementation supports both European and American put options using the same pricing framework.

---

## Parameters Used

| Parameter           |      Value |
| ------------------- | ---------: |
| Initial Stock Price |        100 |
| Strike Price        |        100 |
| Time to Maturity    |     1 Year |
| Risk-Free Rate      |         5% |
| Volatility          |        25% |
| Steps               | Up to 1000 |

---

## Features

* CRR Binomial Tree implementation
* European Put Pricing
* American Put Pricing
* Early Exercise Premium Calculation
* Convergence Analysis
* Finance-Based Validation Tests
* Three-Dimensional Price Surface
* Early Exercise Boundary Visualization
* Jupyter Notebook Demonstration

---

## Finance-Based Validation

The implementation verifies several theoretical properties of option pricing:

* American put value is greater than or equal to the European put value.
* American put value is never below its intrinsic value.
* Put option value decreases as the stock price increases.
* Put option value increases with higher volatility.
* Option prices converge as the number of binomial steps increases.

---

## Sample Output

For the benchmark parameters:

* European Put Price: **7.4540**
* American Put Price: **7.9724**
* Early Exercise Premium: **0.5184**

These results are consistent with option pricing theory.

---

## Visualizations

The repository includes:

* Convergence of European and American option prices
* American Put Price Surface
* Early Exercise Boundary

These plots help illustrate both numerical convergence and the financial intuition behind early exercise.

---

## Technologies Used

* Python 3
* NumPy
* Pandas
* Matplotlib
* Jupyter Notebook

---

## Future Improvements

Potential extensions include:

* Black–Scholes Model comparison
* Option Greeks
* Implied Volatility estimation
* Monte Carlo Simulation
* Barrier and Exotic Options
* Interactive dashboards using Plotly or Streamlit

---

## References

* John C. Cox, Stephen A. Ross and Mark Rubinstein (1979), *Option Pricing: A Simplified Approach*
* Hull, John C. *Options, Futures and Other Derivatives*
* Zerodha Varsity – Options Theory
* National Stock Exchange (NSE) Learning Resources

---

## Author

**Ishika Rawat**

BS Economics, IIT Bombay

Project completed as part of a quantitative finance option pricing assignment.


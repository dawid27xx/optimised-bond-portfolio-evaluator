import numpy as np
import matplotlib.pyplot as plt

def plot_yield_curve(yield_curve, title=None):
    tenors = np.array(yield_curve.tenors)
    spot_rates = np.array(yield_curve.spotRates)

    grid = np.linspace(min(tenors), max(tenors), 300)
    interpolated_rates = [yield_curve.getSpotRate(t) for t in grid]

    plt.figure(figsize=(8, 5))
    plt.plot(grid, np.array(interpolated_rates) * 100, label="Interpolated curve", linewidth=2)
    plt.scatter(tenors, spot_rates * 100, color="red", zorder=3, label="Market points")

    plt.xlabel("Maturity (years)")
    plt.ylabel("Spot rate (%)")
    plt.title(title or f"Yield Curve ({yield_curve.currency})")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

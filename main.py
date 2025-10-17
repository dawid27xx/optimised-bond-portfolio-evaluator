from datetime import date
from models.yieldCurve import YieldCurve
from models.bond import Bond
from utils.plotCurve import plot_yield_curve

def main():
    yc = YieldCurve(
        curveDate=date(2025, 10, 17),
        tenors=[0.5, 1, 2, 5, 10, 20, 30],
        spotRates=[0.043, 0.044, 0.045, 0.047, 0.048, 0.049, 0.050],
        compounding="semiannual",
        currency="USD",
        dayCount="ACT/ACT"
    )

    print("Interpolated Spot Rate at 7.5 years:")
    print(round(yc.getSpotRate(7.5) * 100, 3), "%")

    print("\nDiscount Factor at 7.5 years:")
    print(round(yc.getDiscountFactor(7.5), 6))

    bond = Bond(
        face=1000,
        couponRate=0.05,
        maturityDate=date(2030, 10, 1),
        issueDate=date(2020, 1, 1),
        frequency=2,
        dayCount="ACT/ACT"
    )

    paymentDates, payments = bond.generateCashflows()
    print("\nSample bond cashflows:")
    for d, p in zip(paymentDates[:5], payments[:5]):
        print(d, p)

    print("\nPlotting yield curve...")
    plot_yield_curve(yc, title="US Treasury Yield Curve")

if __name__ == "__main__":
    main()

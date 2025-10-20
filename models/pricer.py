from datetime import date

class Pricer:
    def __init__(self, yieldCurve, valuationDate):
        self.yieldCurve = yieldCurve
        self.valuationDate = valuationDate

    def priceBond(self, bond):
        paymentDates, payments = bond.generateCashflows()
        pv = 0.0
        received = 0.0

        for d, cf in zip(paymentDates, payments):
            if d <= self.valuationDate:
                received += cf
                continue

            t = (d - self.valuationDate).days / 365.0
            df = self.yieldCurve.getDiscountFactor(t)
            pv += cf * df

        total = pv + received
        return pv, received, total


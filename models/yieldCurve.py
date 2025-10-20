from datetime import date
import math
from utils.plotCurve import plotYieldCurve
import numpy as np


class YieldCurve:
    def __init__(self, curveDate, tenors, spotRates, compounding, currency, dayCount):
        self.curveDate = curveDate
        self.tenors = tenors
        self.spotRates = spotRates
        self.compounding = compounding
        self.currency = currency
        self.dayCount = dayCount


    def getSpotRate(self, t):
        if t <= self.tenors[0]:
            return self.spotRates[0]
        if t >= self.tenors[-1]:
            return self.spotRates[-1]
        

        if t in self.tenors:
            idx = np.where(self.tenors == t)[0][0]
            return self.spotRates[idx]


        # interporlation
        # to change as not fully accurate
        for i in range(len(self.tenors) - 1):
            t1, t2 = self.tenors[i], self.tenors[i + 1]
            if t1 <= t <= t2:
                r1, r2 = self.spotRates[i], self.spotRates[i + 1]
                break

        if self.compounding == "annual":
            DF1 = (1 + r1) ** (-t1)
            DF2 = (1 + r2) ** (-t2)
        elif self.compounding == "semiannual":
            DF1 = (1 + r1 / 2) ** (-2 * t1)
            DF2 = (1 + r2 / 2) ** (-2 * t2)
        else:
            raise ValueError("Unsupported compounding type")

        lnDF1, lnDF2 = math.log(DF1), math.log(DF2)
        lnDFt = lnDF1 + (lnDF2 - lnDF1) * (t - t1) / (t2 - t1)
        DFt = math.exp(lnDFt)

        if self.compounding == "annual":
            rt = DFt ** (-1 / t) - 1
        elif self.compounding == "semiannual":
            rt = 2 * (DFt ** (-1 / (2 * t)) - 1)

        return rt


    def getDiscountFactor(self, t):
        r = self.getSpotRate(t)

        if self.compounding == "annual":
            DF = (1 + r) ** (-t)
        elif self.compounding == "semiannual":
            DF = (1 + r / 2) ** (-2 * t)
        else:
            raise ValueError("Unsupported compounding type")

        return DF


    def getForwardRate(self, t1, t2):
        pass

    def plotCurve(self):
        plotYieldCurve(self, title="US Treasury Yield Curve")


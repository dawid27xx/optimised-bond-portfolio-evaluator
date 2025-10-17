from datetime import date
from dateutil.relativedelta import relativedelta


class Bond:
    def __init__(self, face, couponRate, maturityDate, issueDate, frequency, dayCount):
        self.face = face
        self.couponRate = couponRate
        self.maturityDate = maturityDate
        self.issueDate = issueDate
        self.frequency = frequency
        self.dayCount = dayCount

    def generateCashflows(self):
        monthsPerPeriod = 12 // self.frequency
        couponAmount = self.face * self.couponRate / self.frequency

        paymentDates = []
        payments = []

        currentDate = self.issueDate
        while True:
            nextDate = currentDate + relativedelta(months=+monthsPerPeriod)
            if nextDate >= self.maturityDate:
                break
            paymentDates.append(nextDate)
            payments.append(couponAmount)
            currentDate = nextDate
            
        # to change to consider ACT/ACT or ACT/365

        daysFull = (currentDate + relativedelta(months=+monthsPerPeriod) - currentDate).days
        daysStub = (self.maturityDate - currentDate).days
        stubFraction = daysStub / daysFull if daysFull > 0 else 1.0

        finalCoupon = couponAmount * stubFraction
        finalPayment = finalCoupon + self.face

        paymentDates.append(self.maturityDate)
        payments.append(finalPayment)

        return paymentDates, payments


class USTreasuryBond(Bond):
    def __init__(self, face, couponRate, maturityDate, issueDate):
        super().__init__(
            face=face,
            couponRate=couponRate,
            maturityDate=maturityDate,
            issueDate=issueDate,
            frequency=2,          
            dayCount="ACT/ACT"    
        )
        self.currency = "USD"
        self.issuer = "US_TREASURY"


class UKGiltBond(Bond):
    def __init__(self, face, couponRate, maturityDate, issueDate):
        super().__init__(
            face=face,
            couponRate=couponRate,
            maturityDate=maturityDate,
            issueDate=issueDate,
            frequency=2,           
            dayCount="ACT/365"     
        )
        self.currency = "GBP"
        self.issuer = "UK_GOVERNMENT"

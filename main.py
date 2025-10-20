from datetime import date
from models.yieldCurve import YieldCurve
from models.bond import Bond
from models.pricer import Pricer
from utils.loadData import loadData
from utils.generateBonds import loadBonds


def main():
    
    UKGiltTenors, UKGiltSRs = loadData("data/boeYield.csv")
    USTreasuryTenors, USTreasurySRs = loadData("data/treasuryYield.csv")

    UKGiltYC = YieldCurve(date(2025, 10, 16), UKGiltTenors, UKGiltSRs, compounding="annual", currency="GBP", dayCount="ACT/365")
    USTreasuryYC = YieldCurve(date(2025, 10, 16), USTreasuryTenors, USTreasurySRs, compounding="semiannual", currency="USD", dayCount="ACT/ACT")

    UKPricer = Pricer(UKGiltYC, date.today())
    USPricer = Pricer(USTreasuryYC, date.today())
    
    bonds = loadBonds("data/bonds.csv")

    print("\n📊 PORTFOLIO VALUATION RESULTS")
    print("-" * 80)

    UK_total, US_total = 0, 0

    for issuer, bond in bonds:
        if issuer == "UK":
            pv, received, total = UKPricer.priceBond(bond)
            UK_total += pv
            print(f"🇬🇧 UK | Maturity: {bond.maturityDate} | Face: £{bond.face:>7,.0f} | Coupon: {bond.couponRate*100:>4.2f}% | PV: £{pv:>8.2f} | Received: £{received:>8.2f}")
        elif issuer == "US":
            pv, received, total = USPricer.priceBond(bond)
            US_total += pv
            print(f"🇺🇸 US | Maturity: {bond.maturityDate} | Face: ${bond.face:>7,.0f} | Coupon: {bond.couponRate*100:>4.2f}% | PV: ${pv:>8.2f} | Received: ${received:>8.2f}")
        else:
            print(f"⚠️ Unknown issuer: {issuer}")

    print("\n💼 PORTFOLIO SUMMARY")
    print("-" * 80)
    print(f"Total UK Gilts Value: £{UK_total:,.2f}")
    print(f"Total US Treasuries Value: ${US_total:,.2f}")
    print(f"Combined Portfolio Value: £{UK_total:,.2f} + ${US_total:,.2f}")

    

if __name__ == "__main__":
    main()

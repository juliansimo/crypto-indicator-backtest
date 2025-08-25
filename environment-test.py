import vectorbt as vbt

price = vbt.YFData.download('BTC-USD').get('Close')

pf = vbt.Portfolio.from_holding(price, init_cash=100)

print(f"BTC/USD total profit since 2014 = {pf.total_profit():,.2f}")
print(pf.stats())
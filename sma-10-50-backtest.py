import vectorbt as vbt

assets = ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD"]
assets = ["ADA-USD", "LINK-USD", "SUI-USD", "BNB-USD"]
assets = ["DOGE-USD", "TRX-USD", "AVAX-USD", "HYPE-USD", "LTC-USD"]

for asset in assets:
    price = vbt.YFData.download(asset).get('Close')
    fast_ma = vbt.MA.run(price, 10)
    slow_ma = vbt.MA.run(price, 50)
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100)
    pf.total_profit()
    print("========================== Strategy analysis =========================")
    print(f"Criptoasset = {asset}")
    print(pf.stats())
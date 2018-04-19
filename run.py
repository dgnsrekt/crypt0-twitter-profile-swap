import schedule
import time

from coinmarketcap import Market
from states import ProfileStateSwap


def getBTC_PercentChange():
    market = Market()
    bitcoin = market.ticker(currency='bitcoin')[0]
    pct = float(bitcoin['percent_change_1h'])
    print('Checking BTC 1 Hour PCHG:{}'.format(pct))
    return pct


bitcoin_pct = getBTC_PercentChange()
device = ProfileStateSwap(bitcoin_pct)


def job():
    bitcoin_pct = getBTC_PercentChange()
    device.on_event(bitcoin_pct)


schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

#!python3.6

import click
import schedule
import time

from coinmarketcap import Market
from states import ProfileStateSwap


def getBTC_PercentChange():
    market = Market()
    bitcoin = market.ticker(currency='bitcoin')[0]
    percent_change = float(bitcoin['percent_change_1h'])
    print('Checking BTC 1 Hour PCHG:{}'.format(percent_change))
    return percent_change


@click.group()
def main():
    'Sync your twitter profile picture and banner with BTC 1H percent change.'


@main.command()
def run():
    '''Run program'''
    bitcoin_pct = getBTC_PercentChange()
    device = ProfileStateSwap(bitcoin_pct)

    def job():
        bitcoin_pct = getBTC_PercentChange()
        device.on_event(bitcoin_pct)

    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


@main.command()
def test():
    '''Tests profile/banner.'''
    from time import sleep
    from profile import TwitterProfile

    profile = TwitterProfile()
    profile.setBearishProfileStatus()

    print('Check your twitter profile page for bearish profile/banner.')
    print('Profile will change to bullish in 30 seconds.')
    sleep(30)

    profile.setBullishProfileStatus()
    print('Check your twitter profile page for bullish profile/banner.')
    print('Test Complete.')


if __name__ == '__main__':
    main()

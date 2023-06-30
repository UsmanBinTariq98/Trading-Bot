# This trading bot is a combination of EMA, ADX and Super Trend Strategies

import pandas as pd
import numpy as np
import MetaTrader5 as mt
from datetime import datetime as dt
import talib as ta
import PySide6 as ps

def market_order(symbol, volume, order_type, ema20, ema50):
    ticks = mt.symbol_info_tick(symbol)
    order_dict = {'buy': 0, 'sell': 1}
    price_dict = {'buy': ticks.ask, 'sell': ticks.bid}
    sl = {'buy': ema50, 'sell': ema20}
    tp = {'buy': ticks.bid + 0.00003, 'sell': ticks.ask - 0.00003}
    request = {
        'action': mt.TRADE_ACTION_DEAL,
        'symbol': symbol,
        'volume': volume,
        'type': order_dict[order_type],
        'price': price_dict[order_type],
        'deviation': 20,
        'magic': 100,
        'sl': sl[order_type],
        'tp': tp[order_type],
        'comment': "Python market order",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC
    }
    order = mt.order_send(request)
    print(order)

if __name__ == '__main__':
    print('EURUSD')
    symbol = 'EURUSD'
    volume = 1.0
    timeframe = mt.TIMEFRAME_M1
    smaPeriod = 60
    mt.initialize()
    while True:
        bars = mt.copy_rates_from_pos(symbol, timeframe, 1, smaPeriod)
        df = pd.DataFrame(bars)
        df['ema20'] = ta.EMA(df['close'], timeperiod=20)
        df['ema50'] = ta.EMA(df['close'], timeperiod=50)
        df['ADX'] = ta.ADX(df['high'], df['low'], df['close'], timeperiod=18)
        df['superTrend'] = ta.SAREXT(df['high'], df['low'])
        ema20 = df['ema20'].iloc[-1]
        ema50 = df['ema50'].iloc[-1]
        adx = df['ADX'].iloc[-1]
        superTrend = df['superTrend'].iloc[-1]
        if mt.positions_total() <=1:
            if ema20 > ema50:
                if adx > 18:
                    if superTrend > 0:
                        market_order(symbol, volume, 'buy', ema20, ema50)
            elif ema20 < ema50:
                if adx > 18:
                    if superTrend < 0:
                        market_order(symbol, volume, 'sell', ema20, ema50)
            else:
                print('No trade')
import talib
from binance_api import *
from chart import *
from utils import stochrsi, supertrend # smoothed stochastic rsi

if __name__ == '__main__':
    candles_df = get_candles('BTCUSDT', interval='4h')

    # plot candle sticks
    # T O C H L order is important
    candles = candles_df[['T', 'O', 'C', 'H', 'L']]
    fplt.candlestick_ochl(candles, ax=ax)

    close = candles_df['C'].to_numpy()
    high = candles_df['H'].to_numpy()
    low = candles_df['L'].to_numpy()

    ema = talib.EMA(close, timeperiod=200)
    fplt.plot(ema, width=2)

    slowk, slowd = stochrsi(close, smoothK=3, smoothD=3, length=14)
    fplt.plot(slowk, ax=ax2, width=2)
    fplt.plot(slowd, ax=ax2, width=2, color='#fd6900')
    fplt.add_band(20, 80, ax=ax2, color='#311a51')

    up1, dn1, trend1 = supertrend(high, low, close, length=10, atr_factor=1)
    fplt.plot(up1, width=2, color='#4caf50')
    fplt.plot(dn1, width=2, color='#fd5352')

    up2, dn2, trend2 = supertrend(high, low, close, length=11, atr_factor=2)
    fplt.plot(up2, width=2, color='#4caf50')
    fplt.plot(dn2, width=2, color='#fd5352')

    up3, dn3, trend3 = supertrend(high, low, close, length=12, atr_factor=3)
    fplt.plot(up3, width=2, color='#4caf50')
    fplt.plot(dn3, width=2, color='#fd5352')

    # restore view (X-position and zoom)
    fplt.autoviewrestore()
    fplt.show()

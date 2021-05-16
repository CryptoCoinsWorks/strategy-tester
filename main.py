import talib
from binance_api import *
from chart import *
from utils import stochrsi # smoothed stochastic rsi

if __name__ == '__main__':
    candles_df = get_candles('ETHUSDT', interval='1h')

    # plot candle sticks
    # T O C H L order is important
    candles = candles_df[['T', 'O', 'C', 'H', 'L']]
    fplt.candlestick_ochl(candles, ax=ax)

    close = candles_df['C'].to_numpy()

    ema = talib.EMA(close, timeperiod=200)
    fplt.plot(ema)

    slowk, slowd = stochrsi(close, smoothK=3, smoothD=3, length=14)
    fplt.plot(slowk, ax=ax2)
    fplt.plot(slowd, ax=ax2)

    # restore view (X-position and zoom)
    fplt.autoviewrestore()
    fplt.show()

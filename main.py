from binance_api import *
import finplot as fplt

if __name__ == '__main__':
    # dark mode
    fplt.foreground = '#b2b5be'
    fplt.background = '#151924'
    fplt.candle_bull_body_color = fplt.candle_bull_color
    fplt.odd_plot_background = '#151924'
    fplt.cross_hair_color = fplt.foreground

    candles_df = get_candles('ETHUSDT', interval='1h')

    # create two axes
    ax, ax2 = fplt.create_plot('ETHUSDT', rows=2)
    ax.set_visible(crosshair=True, xaxis=True,
                   yaxis=True, xgrid=True, ygrid=True)
    ax2.set_visible(crosshair=True, xaxis=True,
                    yaxis=True, xgrid=True, ygrid=True)

    # plot candle sticks
    # O C H L order is important
    candles = candles_df[['T', 'O', 'C', 'H', 'L']]
    fplt.candlestick_ochl(candles, ax=ax)

    # restore view (X-position and zoom)
    fplt.autoviewrestore()

    fplt.show()

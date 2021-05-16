import finplot as fplt

# dark mode
fplt.foreground = '#b2b5be'
fplt.background = '#151924'
fplt.candle_bull_body_color = fplt.candle_bull_color
fplt.odd_plot_background = fplt.background
fplt.cross_hair_color = fplt.foreground
    
# create two axes
ax, ax2 = fplt.create_plot('Strategy', rows=2)
ax.set_visible(crosshair=True, xaxis=True,
                yaxis=True, xgrid=True, ygrid=True)
ax2.set_visible(crosshair=True, xaxis=True,
                yaxis=True, xgrid=True, ygrid=True)
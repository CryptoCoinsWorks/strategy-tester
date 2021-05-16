import numpy as np
import talib

def lowest(source, length):
  if len(source) < length:
    raise Exception(f"Length parameter is {length} but the maximum data length is {len(source)}")
    
  lowest = source[-1]
  for i in range(len(source) - 1, len(source) - length - 1, -1):
    if source[i] < lowest:
      lowest = source[i]
  
  return lowest

def highest(source, length):
  if len(source) < length:
    raise Exception(f"Length parameter is {length} but the maximum data length is {len(source)}")

  highest = source[-1]
  for i in range(len(source) - 1, len(source) - length - 1, -1):
    if source[i] > highest:
      highest = source[i]
  
  return highest

def stochrsi(close, smoothK, smoothD, length):
  fastk, _ = talib.STOCHRSI(close, fastk_period=length, fastd_period=length, timeperiod=length)
  slowk = talib.SMA(fastk, timeperiod=smoothK)
  slowd = talib.SMA(slowk, timeperiod=smoothD)
  return slowk, slowd


def nz(x, y):
  if not np.isnan(x):
    return x
  return y

# Periods = input(title="ATR Period 1", type=input.integer, defval=10)
# src = input(hl2, title="Source 1")
# Multiplier = input(title="ATR Multiplier 1", type=input.float, step=0.1, defval=1.0)
def supertrend(high, low, close, length, atr_factor=1):
  # // calculations
  hl2 = (high + low) / 2
  
  atr = talib.ATR(high, low, close, timeperiod=length) * atr_factor
  up = hl2 - atr
  dn = hl2 + atr
  trend = np.ones(len(close))

  for i in range(length-1, len(close)):
    try:
      _up = up[i]
      _up1 = nz(up[i-1], up[i])
      up[i] = max(_up, _up1) if close[i-1] > _up1 else _up

      _dn = dn[i]
      _dn1 = nz(dn[i-1], dn[i])
      dn[i] = min(_dn, _dn1) if close[i-1] < _dn1 else _dn

      _trend = nz(trend[i-1], trend[i])
      trend[i] = 1 if _trend == -1 and close[i] > _dn1 else (-1 if _trend == 1 and close[i] < _up1 else _trend)
    except:
      pass    
  
  up_plt = up
  dn_plt = dn
  for i in range(len(up)):
    up_plt[i] = up_plt[i] if trend[i] == 1 else np.nan
    dn_plt[i] = dn_plt[i] if trend[i] == -1 else np.nan
  # up := close[1] > up1 ? max(up,up1) : up
  # dn=src+(Multiplier*atr)
  # dn1 = nz(dn[1], dn)
  # dn := close[1] < dn1 ? min(dn, dn1) : dn
  # trend = 1
  # trend := nz(trend[1], trend)
  # trend := trend == -1 and close > dn1 ? 1 : trend == 1 and close < up1 ? -1 : trend
  return up_plt, dn_plt, trend

# TESTS
if __name__ == "__main__":
  arr = np.random.randint(10, size=10)
  print(arr)

  # print(lowest(arr, 4))
  # print(lowest(arr, -1))
  # print(lowest(arr, 0))
  # print(lowest(arr, 10))
  # print(lowest(arr, 11)) # exception

  # print(highest(arr, 4))
  # print(highest(arr, -1))
  # print(highest(arr, 0))
  # print(highest(arr, 10))
  # print(highest(arr, 11)) # exception

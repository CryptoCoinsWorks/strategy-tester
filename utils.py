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

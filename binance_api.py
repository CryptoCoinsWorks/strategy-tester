from credentials import api_key, api_secret
from binance.client import Client
import pandas as pd
import numpy as np

client = Client(api_key, api_secret)

def get_candles(symbol, interval):
    data = client.get_klines(symbol=symbol, interval=interval)
    array = np.array(data)

    df = pd.DataFrame(array[:, 0:5], columns={
                      'T': 'time', 'O': 'open', 'H': 'high', 'L': 'low', 'C': 'close'}).astype(float)

    return df

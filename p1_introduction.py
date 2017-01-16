#! python3
#p1_introduction.py - Introduces the Pandas module

import pandas as pd
import pandas_datareader.data as wb
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

def adj_close(ticker):
    """
    Prints the head (top five) of the pricing data found on
    Yahoo Finance API and plots the Adj Close in Matplotlib.
    """
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2015, 1, 1)

    df = wb.DataReader(ticker.upper(), "yahoo", start, end)
    
    print(df.head())
    df['Adj Close'].plot()
    plt.show()

def main():
    adj_close('GOOG')

if __name__ == '__main__':
    main()

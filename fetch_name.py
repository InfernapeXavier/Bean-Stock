import pandas as pd

def fetch(symbol):
    df = pd.read_csv('secwiki_tickers.csv')
    name = df[df['Ticker']==symbol]['Name'].item()
    return (name)

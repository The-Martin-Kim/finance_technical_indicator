import yfinance as yf
import os

start = "1999-01-04"
end = "2024-01-02"

ticker = "^IXIC"

df = yf.download(ticker, start=start, end=end)

df.to_csv("NASDAQ.csv")

os.system("python preprocess_downloaded_data.py")

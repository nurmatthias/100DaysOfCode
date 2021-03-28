import requests
import datetime as dt
import pandas
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "XXXXXXXXXXXXXXXXXX",
}

response = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
response.raise_for_status()

df = pandas.DataFrame().from_dict(response.json()["Time Series (Daily)"], orient="index", columns=["4. close"])
df.sort_index(ascending=True, inplace=True)
df = df.tail(2)

df.rename(columns={"4. close": "close"}, inplace=True)
df.close = [float(value) for value in df.close]

df['date'] = df.index
df["diff_pct"] = df.close.pct_change()


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "from": df.date.max(),
    "apiKey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

response = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
response.raise_for_status()

news = [f"Headline: {data['title']}.\nBrief: {data['description']}" for data in response.json()["articles"][:3]]

print(f"{COMPANY_NAME}: {'🔺' if df.diff_pct.max() > 0 else '🔻'} {round(df.diff_pct.max()*100, 1)}%")
for entry in news:
    print(entry)
    print("")

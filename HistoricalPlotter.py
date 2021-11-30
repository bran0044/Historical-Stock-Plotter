import requests
import plotly.graph_objects as go
from config import authkey

date = []
open = []
high = []
low = []
close = []
volume = []

auth = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/ZM?apikey={}'.format(authkey))
fmp = auth.json()

for x in range(len(fmp)):
    date.append(fmp[x]['date'])
    open.append(fmp[x]['open'])
    high.append(fmp[x]['high'])
    low.append(fmp[x]['low'])
    close.append(fmp[x]['close'])
    volume.append(fmp[x]['volume'])
print(volume)
fig = go.Figure(data=[go.Candlestick(x=date,
                open=open,
                high=high,
                low=low,
                close=close)])

fig.update_xaxes(
    rangeslider_visible=True,
    rangebreaks=[
        # NOTE: Below values are bound (not single values), ie. hide x to y
        dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
        dict(bounds=[16, 9.5], pattern="hour"),  # hide hours outside of 9.30am-4pm
        # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
    ])
fig.show()

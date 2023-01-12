R!/usr/bin/env python


import pandas as pd
import pandas_datareader.data as web

all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})

volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

returns = price.pct_change() 			#Calcula mudanás percentuais nos preços
print(returns.tail())
print(returns['MSFT'].cov(returns['IBM']))	#Calcula a covariancia entre os dois valores diferentes

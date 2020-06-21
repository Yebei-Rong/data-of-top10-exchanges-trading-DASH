import os
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# get order book history
def get_historical_order_book(api_key, url, exchange, pair, time):
	""" return the dictionary of historical order book

		api_key: the string of free api key
		url: request url
		exchange: target exchange, string
		pair: target pair, string
		time: target datetime, string
	"""

	# set api key
	key = os.environ.get('COINAPI_KEY', api_key)
	headers = {
    'X-CoinAPI-Key': api_key
	}

	# request url
	request_url = url + exchange + "_SPOT_" + "pair/history?time_start=" + time + "T00:00:00"

	# get data
	response = requests.get(request_url, hearders = headers)

	return response.json()

# get spread data
def get_spread(order_book):
	""" return the historical order book data, with the depth added

		order_dict: a list of the historical order book data
	"""
	spread = []

	for i in range(len(order_book)):
		min_ask = order_book[i]['asks'][0]['price']
		max_bid = order_book[i]['bids'][0]['price']

		depth = min_ask - max_bid

		spread.append(depth)

		order_book[i]['depth'] = depth


	return order_book, spread

# # plot the spread pattern
# def plot_spread_pattern(spread, exchange, pair, time_period):
# 	""" plot the spread pattern of the specific exchange pair during the time_period
# 	"""



if __name__ == '__main__':
	benchmark = ['COINBASE', 'BINANCE', 'KRAKEN', 'POLONIEX']
	exchange = ['BITFINEX','BITTREX','GATEIO','COINFIELD','VINDAX','HITBTC']
	time_period = ['2020-03-30', '2020-03-31', '2020-04-01', '2020-04-02', '2020-04-03']

	my_key = "EE69C22E-BF60-4DCD-88A5-EF686A8E8EBF"
	url = """https://rest.coinapi.io/v1/orderbooks/"""
	time_period = ['2020-03-30', '2020-03-31', '2020-04-01', '2020-04-02', '2020-04-03']

	#COINBASE
	order_book = []
	exchange = "COINBASE"
	pair = "DASH_USD"
	for i in time_period:
		time = i

		order_book = order_book + get_historical_order_book(my_key, url, exchange, pair, time)

	_, spread = get_spread(order_book)

	plt.plot(spread)




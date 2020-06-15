
# data-of-top10-exchanges-trading-DASH
Use exchange API to get trading data of DASH

# Is cryptocurrency price manipulated?

## Ranking top 10 exchanges trading DASH
# Qianruo Mu
First Step: 
Crypto Exchange Ranking by Cyber Security Score(CSS) 
the recent report can be referred by https://cer.live

Cyber Security Score (CSS) is one of the main metrics provided by Crypto Exchange Ranks (CER) to calculate the complex rating of crypto exchanges. 
(reason: cybersecurity is the most fundamental thing that must be addressed to the full extent by any exchange before commencing its operations: exchanges must take responsibility for users’ money and personal data. )
To know whether the exchanges are sustainable and safe for using from three aspects: 
1)	Server Security 
SSL/TLS certificate, WAF&CDN, SPF, DNSSEC, Open Ports, Hidden dirs and dirs access, Secure Headers, Secure cookies, Existence in Spam DB. 
2)	User Security (Captcha, 2FA, Strict Password Requirements) 
3)	Ongoing Crowdsource Security Assessment (OCSA). 

Second Step:
CoinGecko (https://blog.coingecko.com/trust-score-explained/)
traditional markets: exchanges with high volume equate to high liquidity. crypto markets: exchanges with high volume does not necessarily equate to high liquidity. (because many of the unregulated exchanges engage in wash trading and other manipulative behaviors to inflate their trading volume.)
####1)Normalized Trading Volume by Traffic (SimilarWeb) 
 difficult to fake their web traffic statistics which are aggregated by 3rd party services such as SimilarWeb
based on the Bitwise 10 Real Volume Exchanges (Binance, Bitfinex, Kraken, Bitstamp, Coinbase, Bitflyer, Gemini, itBit, Bittrex, Poloniex) 
use them as benchmark may cause some problems

The normalization of exchange volumes involves several steps, which we will walk you through below:
1	We aggregate monthly web traffic statistics from SimilarWeb for all crypto exchanges that we track on CoinGecko. We then divide it by 30 to get average daily traffic.
2	Together with the daily reported trading volume information that we track, we are able to derive the Average Daily User Trading Volume (ADUTV) for each exchange.
ADUTV(EXCHANGE x) = DAILY VOLUME(EXCHANGE x)/DAILY VISITORS(EXCHANGE X)
3 Then, based on the Bitwise 10 Real Volume Exchanges (Binance, Bitfinex, Kraken, Bitstamp, Coinbase, Bitflyer, Gemini, itBit, Bittrex, Poloniex), we calculate the median for the 10 exchanges ADUTV and we call this the Benchmark Daily User Volume. 
Benchmark = median(ADUTV-binance, ADUTV - Bitfinex...)
We then derive a Normalized Exchange Total Trading Volume based on this Benchmark. Exchanges with lower ADUTV when compared to the Benchmark will not have their Reported Trading Volume normalized. However, for exchanges reporting ADUTV higher than Benchmark, we will discard their ADUTV and multiply their SimilarWeb daily traffic estimate and multiply it against the Benchmark.

2) Order Book Analysis (Bid/Ask Spread & ±2% Depth Cost)
two new order book based metrics 
i.	Bid/Ask Spread 
Bid/Ask Spread = (Lowest Ask – Highest Bid) / Lowest Ask x 100
The Bid/Ask Spread is the amount by which the ask price (lowest price a seller is willing to sell) exceeds the bid price (highest price a buyer is willing to buy) for an asset in any particular market. This spread is represented in a percentage format and is a good measure of liquidity. A lower bid/ask spread will mean that a particular market is more liquid while a higher bid/ask spread will mean that it is more illiquid. 
ii.	± 2% Depth Cost
when combined with trading volume data provides a better overview of the real liquidity of any given trading pair on an exchange. 
(Capital in USD required to move the order book by 2% up or down from last traded price.)
1)first take the last done price for any particular market and then calculate the 2% upper and lower bound. Assuming BTC/USDT for a particular exchange was last traded at $6,000, the 2% upper bound is thus $6,120 and the 2% lower bound is thus $5,880.
2) sum up the amount of BTC sitting in the order book between $6,000 and $6,120 and then multiply it by the order price. This is the amount of capital required to move the order book up by 2% and we call it +2% Depth.
3) sum up the amount of BTC sitting in the order book between $5,880 and $6,000 and then also multiply it by the order price. This is the amount of capital required to move the order book down by 2% and we call it -2% Depth.
A thick order book will indicate that there is more liquidity for any trader to come in and buy or sell a particular crypto asset without much slippage while a thin order book will indicate that there is no liquidity for any trader to trade meaningfully.



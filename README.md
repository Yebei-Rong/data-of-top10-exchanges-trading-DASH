## 1. Ranking top 5 exchanges trading DASH based on transparency

Based on the measures given by Nomics https://blog.nomics.com/essays/transparency-ratings/ and academic papers, we summarized their rating method, advantages and disadvantages, and would like to establish our own reliable and explicit ranking rules for cryptocurrency exchanges.

## Ranking top 10 exchanges trading DASH

### Nomics' Exchanges Transparency Ratings

#### Historical Trade-Level Data
According to the examination of 10 trusted exchanges revealed by Bitwise, Nomics found eight of the 10 exchanges provide historical trade level data which is considered *the most granular and audible* form of data available. In contrast, for the exchanges called bad actors by Bitwise, every single one of them provides limited trading history and virtually no granularity around trading activity.

Nomics assign 7 types of transparency scores (A+,A,A-,B,C,D,F) to exchanges. The middle one is score B which represents a good exchange. For one to have rating B, it must provide, at the very least, this much candle history:
* 1-Day Candles: 7 candles with last candle occurring within a rolling 48 hours
* 1-Hour Candles: 24 candles with last candle occurring within a rolling 2 hours
* 1-Minute Candles: 60 candles with last candle occurring within a rolling 10 minutes

One advantage of Nomics ratings is that these are not subjective. They check their database and exchange APIs to determine the qualitiy of data. Meanwhile, Nomics says they have never charged for exchange listings. Nomics dose not charge for exchage listing, only creating deep data integration

However, I think it is possible that the data obtained by exchange APIs is fake although exchanges release all historical data because some exchanges may follow the trend of very big exchanges such as Binance to simulate fake data. 

### Bitwise

#### What do suspicious exchanges look like?

* Trade printing between bid and ask: 
It takes CoinBene as example. The trade activity on its official website shows a perfectly alternating pattern of green and red trades. Furthermore, trades on CoinBene come in pairs, and each pair has one buy(green) and one offsetting sell(red) at the same time, and the size of these trades are always roughly equal in size, allowing them to nearly offset one-another over time.


### Our Criteria

In addition to the transparency score from Nomics, our ratings will analyze the trade data further and consider aspects besides data itself to draw our final conlusions.

* Alexa rank (more details at https://blog.alexa.com/marketing-research/alexa-rank/)

Alexa rank is a measure of website popularity, and it ranks millions of websites in order of popularity. This is a good feature to detect exchanges that do fake volumes in order to be listed first in websites like coinmarketcap. For example, if we rank active market pairs for DASH, the first one is DASH/TRX, traded in Cat.Ex with a volume(24h) $103,717,243. However, its official website only ranks 72,293 in the global Internet traffic over past 90 days. In this sense, volume is a very misleading factor and Alexa rank can be used to detect if exchanges post fake voumes effectively.

* Bid-ask spread

In the Bitwise report to SEC, it gave the CoinBene example as suspicous exchanges. CoinBene's average and peak spreads are unreasonable high, upwards of $100. This is only plausible in a thin market, which contradicts CoinBene's claim of high volume. Thus, we consider the spread/price into our model.

* Abnormal volume

Multiple hours (and days) with zero volume, or monotonic trading volume which is not sensitive to price movements.

* Crypto Exchange Ranking by Cyber Security Score(CSS) https://cer.live

Cyber Security Score (CSS) is one of the main metrics provided by Crypto Exchange Ranks (CER) to calculate the complex rating of crypto exchanges. 
(reason: cybersecurity is the most fundamental thing that must be addressed to the full extent by any exchange before commencing its operations: exchanges must take responsibility for users’ money and personal data. )
To know whether the exchanges are sustainable and safe for using from three aspects: 

1)	Server Security

SSL/TLS certificate, WAF&CDN, SPF, DNSSEC, Open Ports, Hidden dirs and dirs access, Secure Headers, Secure cookies, Existence in Spam DB. 

2)	User Security(Captcha, 2FA, Strict Password Requirements) 

3)	Ongoing Crowdsource Security Assessment (OCSA). 

The above factors are qualitative analysis which are not precise enough to determine if the exchange has fake data. We will follow the criterion in the following to do quantitative analysis.

* criterion 1: 

an exchange is considered to fail this criterion if more than 10% of its trades by volume did not appear on its order book prior or if we could identify its prints as time-delayed relays from other exchanges.
    (result: In general, we found that if an exchange failed this test, it would fail almost all the
others as well,which means that they don't make their data avaliable)

* criterion 2: 

for each trade with price p and size x, checked the most recently-reported orderbook whether a) contained bids with totalling size>=x and averege price >=p, or offers with totalling size >=x and average price <=p. if neither the two conditions is met, it failed
    (result: Note that the distribution is bimodal, with most exchanges either having close to 0 or close to all of their trades crossing the best bid or offer)

* criterion 3: having set of reputable exchanges established(strict regulation):Coinbase, Poloniex, Bittrex, Gemini, Kraken, Bitstamp, and itBit(**we need to choose our own index for dash market**). creating a time series by summing their volume up per unit of time, and calculate the correlation of other exchanges' volume by time.
    if correlation>=0.5, it passes the criterion.
    ![alt text](https://github.com/jiachun10/data-of-top10-exchanges-trading-DASH/blob/master/Screen%20Shot%202020-06-13%20at%208.19.47%20PM%20copy.png)

* criterion 4: if *order book ratio*>=0.005 pass the criterion
1) for c1/c2 pairs, getting order book threshold σt at time t is the sum of the hourly
standard deviations (in terms of USD) of c1 and c2.
2) define the *order book depth* to be the total of all the orders
on the order book with price within σt of the best bid and offer
3) order book ratio=order book depth/exchange's reported average daily volume for c1/c2
        
* criterion 5: saying that having real c1/c2 market: if order book ratio>=10^(-6), if an exchange  has <= 5% fake market, then this exchange pass the criterion


====
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

          

# poloniex-lending-bot
Hi,

This is a python 3 poloniex lending bot based on the Poloniex API wrapper of s4w3d0ff.

To make run the bot:

First, edit lending-bot.py and configure this part:

### CONFIGURATION ###
currency = 'BTC'    # currency that you want lend, for exemple BTC or ETH
min_rate = 0.25     # min_rate lend in % for exemple 0.25%
duration = 2        # in day
autoRenew = 0       # if you want auto renew it auto at the same rate, better keep it to 0
APIKey = 'your api key'
Secret = 'your secret'
### END CONFIGURATION ###

Then start it with:
python3 lending-bot.py

Actually the bot place order on the lending market at the best rate for you.
It's mean that your lending rate will be >= min_rate.

This bot split your lending balance in lending volume of 0.001 coins.
It's mean than your lending balance will be split in multiple orders of 0.001 coins on the lending market.

If you prefere lend all you balance in one time just uncomment the line 109 and comment the line 110:
order_id = createLoanOffer(currency, lending_balance, duration, autoRenew, my_offer_rate)
# order_id = createLoanOffer(currency, 0.001, duration, autoRenew, my_offer_rate) 


If you find this tool usefull you can Tip me.
BTC: 1Jrj8oXEoZYNbMpdENYX968kGu8Y4fm1an
ETH: 0xf00ca8ef66d8fbf5ad8628d01eab76af8b464a14
SJCX: 1Ftpk8nonRnaBpsLmE76PRH4dK3ra79PEG

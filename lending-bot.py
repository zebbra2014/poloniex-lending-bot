#!/usr/bin/env python3

import poloniex
from time import sleep

### CONFIGURATION ###
currency = 'BTC'    # currency that you want lend, for exemple BTC or ETH
min_rate = 0.25     # min_rate lend in % for exemple 0.25%
duration = 2        # in day
autoRenew = 0       # if you want auto renew it auto at the same rate, better keep it to 0
APIKey = 'your api key'
Secret = 'your secret'
### END CONFIGURATION ###

limit = 0
min_rate = min_rate / 100.

polo = poloniex.Poloniex(APIKey, Secret)

def api_sleep():
    global limit
    limit += 1
    if limit == 8:
        limit = 0
        sleep(1)

def returnLoanOrders(currency):
    global polo
    while True:
        try:
            api_sleep()
            loan_orders = polo.api('returnLoanOrders',{'currency':currency})
            # demand_rate = float(loan_orders['demands'][0]['rate'])
            offer_rate = float(loan_orders['offers'][0]['rate'])
            # print("offer_rate = ", offer_rate)
            # return offer_rate, demand_rate
            return offer_rate
        except Exception as exc:
            # print("Exception in returnLoanOrders(currency):", exc)
            sleep(1)

def returnLendingBalanceAvailable(currency):
    global polo
    while True:
        try:
            api_sleep()
            return_Available_Account_Balances = polo.api('returnAvailableAccountBalances')
            # print(return_Available_Account_Balances)
            lending_balance = float(return_Available_Account_Balances['lending'][currency])
            # print("lending_balance = ", lending_balance)
            return lending_balance
        except Exception as exc:
            # print("Exception in returnLendingBalanceAvailable:", exc)
            sleep(1)

def createLoanOffer(currency, amount, duration, autoRenew, lendingRate):
    global polo
    while True:
        try:
            api_sleep()
            create_Loan_Offer = polo.api('createLoanOffer', {'currency':currency, 'amount':amount, 'duration':duration, 'autoRenew':autoRenew, 'lendingRate':lendingRate})
            # print(create_Loan_Offer)
            if int(create_Loan_Offer['success']) == 1:
                order_id = int(create_Loan_Offer['orderId'])
                print(str(create_Loan_Offer['message']))
                return order_id
            else:
                return -1
        except Exception as exc:
            # print("Exception in createLoanOffer(currency, amount, duration, autoRenew, lendingRate):", exc)
            sleep(1)

def cancelLoanOffer(order_id):
    global polo
    try:
        api_sleep()
        cancel_Loan_Offer = polo.api('cancelLoanOffer', {'orderNumber':order_id})
    except Exception as exc:
        # print("Exception in cancelLoanOffer(order_id):", exc)
        sleep(1)   
            

# offer_rate, demand_rate = returnLoanOrders(currency)
# returnLengingBalanceAvailable(currency)

def main():
    global currency
    global min_rate
    global duration
    global autoRenew

    print("Welcome on the lending bot ^^")
    print("You need at least 0.001 coins to lend to someone (poloniex requirement)")
    print("Your min_rate is set to: ", min_rate * 100, "%")
    print("It s mean than you will not lend to less than", min_rate * 100, " % but it's possible that sometime you lend more than the min_rate")
    print("If you find this tool usefull you can Tip me.")
    print("BTC: 1Jrj8oXEoZYNbMpdENYX968kGu8Y4fm1an")
    print("ETH: 0xf00ca8ef66d8fbf5ad8628d01eab76af8b464a14")
    print("SJCX: 1Ftpk8nonRnaBpsLmE76PRH4dK3ra79PEG")
    

    while True:
        try:
            offer_rate = returnLoanOrders(currency)
            if offer_rate > min_rate:
                my_offer_rate = offer_rate - 0.00000001
                lending_balance = returnLendingBalanceAvailable(currency)
                if lending_balance >= 0.001:
                    # order_id = createLoanOffer(currency, lending_balance, duration, autoRenew, my_offer_rate)
                    order_id = createLoanOffer(currency, 0.001, duration, autoRenew, my_offer_rate)
                    if order_id == -1:
                        pass
                    else:
                        while True:
                            try:
                                offer_rate = returnLoanOrders(currency)
                                if offer_rate < my_offer_rate:
                                    cancelLoanOffer(order_id)
                                    break
                            except Exception as exc:
                                print(exc)
                                sleep(1)
        except Exception as exc:
            # print(exc)
            sleep(1)

main()

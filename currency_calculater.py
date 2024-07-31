bills = [1000,2000,5000,10000]
Coins = [1,5,10,50,100,500]
last_currency_check = 0
returned_currency = {}


def get_change_due(payment_due,cash_inserted):
    return cash_inserted - payment_due

def calculate_currency():
    amount = get_change_due(1061,5516)
    while (amount!=0 ):
        if (amount > 500):
            for bill in bills:        
                if amount <= bill:
                    amount = amount - last_currency_check
                    add_currency(last_currency_check)
                    break            
                elif amount >= bill:            
                    last_currency_check = bill
        else:
            last_currency_check = min(Coins)
            for coin in Coins:
                if amount < coin:
                    amount = amount - last_currency_check
                    add_currency(last_currency_check)
                    break            
                elif amount >= coin:            
                    last_currency_check = coin
            



def add_currency(currency):
    if currency in returned_currency:
        returned_currency[currency] +=1 # 1000 : 4
    else:
        returned_currency[currency] =1 # 1000 : 1
        
    
calculate_currency()


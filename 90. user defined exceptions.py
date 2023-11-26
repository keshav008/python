class balance_exception(Exception):
    pass
def checkbalance():
    money=int(input("enter total amount:"))
    withdraw=int(input("enter amount want to withdraw:"))
    try:
        balance=money-withdraw
        if(balance<=2000):
            raise balance_exception('insufficient balance')
        print("ramaining balance",balance)
    except balance_exception as be:
        print(be)
checkbalance()

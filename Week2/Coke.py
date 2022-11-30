def coke(amount_due):
    while True:
        print("Amount due: " + str(amount_due))
        coin = int(input("insert the coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -=coin
        else:
            print('',end='')
        if amount_due <= 0:
            print("Change owed: " + str(-amount_due))
            return
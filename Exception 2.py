class AccountBalanceException(Exception):
    pass

def withdraw(amount):
    try:
        withdraw(amount)
        if amount > 10000:
            return amount - 5000
        else:
            raise AccountBalanceException('Account should have minimum 5000 Rs')
    except Exception as e:
        return str(e)




try:
    amount = int(input('Enter the amount '))
    c= withdraw(amount)
    print(c)
except ValueError:
    print('Enter integer only')

no=input('Enter 16 digit card number ')
no=no.replace(' ','')        #a string method
if len(no)==16:
    four=no[-4:]
    digit='X'*4 + ' '
    receipt = digit *3 + four
    print(receipt)
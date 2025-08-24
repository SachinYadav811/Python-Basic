no=int(input('Enter the number '))
n=no
x=0
while n>0:
    d=n%10
    n=n//10
    x=(10*x)+d

if (x==no):
    print('No is palindrome')
else:
    print('No is not palindrome')
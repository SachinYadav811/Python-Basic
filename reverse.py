n=int(input('Enter the number '))
x=0
while n>0:
    d=n%10
    n=n//10
    x=(10*x)+d
print(x)

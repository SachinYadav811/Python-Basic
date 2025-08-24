n=int(input('Enter the number '))
i=0
d=0
while n>0:
     d=n%10
     n=n//10
     i=i+d
print(i)


n=int(input('Enter the number '))
i=0
a=0
b=1
for i in range (n+1):
    c=a+b
    print(a)
    a=b
    b=c
    i=i+1


n=int(input('Enter the count '))
i=0
y=1000
while i<n:
    x=int(input('Enter the numbers '))
    if x<y:
        y=x
    else:
        x=1
    i=i+1
print('Min number is',y)
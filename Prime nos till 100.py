
for j in range(2,101):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count=count+1
    if count==2:
        print('No is prime: ',j)


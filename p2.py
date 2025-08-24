digit = int(input('Enter a positive number: '))
count = 0
if digit ==0 :
   print('Count is 1')
else:
   while digit >0:
        count = count + 1
        digit = digit//10
print('Digits are :', count)



#there is issue with this compiler ,this program is working online but not here
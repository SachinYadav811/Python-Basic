def gap(number):
    space=len(bin(number)[2:])
    for i in range (1,number +1):
        print(i,bin(i)[2:],hex(i)[2:],oct(i)[2:])


if  __name__ == '__main__' :
    n=int(input())
    gap(n)


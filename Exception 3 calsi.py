class Calculation(Exception):
    pass

def evaluate(num1,num2,oper):
    try:
        #evaluate(num1,num2,oper)
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        elif oper == '/':
            if num2==0:
                raise Exception("0 can't be the second number for division")
            return num1 / num2
        else:
            raise Exception('Type the correct operator(+,-,*,/)')
    except Exception as e:
        return str(e)


try:
    num1 = int(input('Enter first no '))
    num2 = int(input('Enter second no '))
    oper = str(input('Enter the operator sign to be used '))
    result = evaluate(num1,num2,oper)
    print(result)
except ValueError:
    print("Type the integer's only")
except :
    print('Wrong format entered')

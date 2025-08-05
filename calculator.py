number1 = float(input("enter the 1st number plaese: "))
number2 = float(input("enter the 2nd number please: "))
op = input("enter the operator")


def calci(number1,number2,op):
    if op == '+':
        return number1+number2
    elif op == '*':
        return number1*number2
    elif op == '-':
        return number1-number2
   
    elif op == '/':
        if number2 == 0:
            return " Error: Division by zero"
    
    else:
        return "invalid operator"
    
    
result = calci(number1,number2,op)
print("result:",result)   
   

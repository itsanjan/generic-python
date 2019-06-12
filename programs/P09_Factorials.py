# This program calculates Factorial of a input number


def getFactorial(number):
    fact = 1
    while(number>0):
        fact = fact * number
        number = number - 1
    return fact

def getFactorial_recursively(number):
    if number == 1:
        return 1
    else:
        return number * getFactorial_recursively(number - 1)

if __name__ == '__main__' :
    input_number = int(input('Enter the number : '))
    print(getFactorial_recursively(input_number))

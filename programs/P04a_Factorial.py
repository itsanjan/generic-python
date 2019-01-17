# A factorial of any integer n!=n*(n-1)*(n-2)*....*2*1

def  factorial(number):
    if number < 0 :
        print ( " factorial is invalid for negative numbers")

    if number == 0 or number == 1 :
        return 1
    
    else :
        return number*factorial(number-1)

if __name__ == '__main__':
    inputValue = int(input("Enter the N value : "))
    print(str(factorial(inputValue)))
# For a positive number n, n!=n*(n-1)*(n-2)*...*2*1

def get_factorial(number):
    if number < 0 :
        print ("Factorial is undefined")

    if number == 0 :
        print ("Factorial is 1")

    if number > 0 :
        factorial_value = 1
        #for n in range (0,number) :
        n=0
        while (n<number):
            factorial_value = factorial_value * (n+1)
            n+=1
        print ("Factorial of number \'"+str(number)+"\' is "+str(factorial_value))

if __name__ == "__main__":
    user_number = int(input("Please enter the number"))
    get_factorial(user_number)

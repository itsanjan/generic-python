# This program checks whether the entered number is prime or not


def checkPrime(number):
    isPrime = False
    i = 0
    if (number == 1 or number == 2):
        print("Number is a prime")

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print("Number is not a prime")
            isPrime = False
            break
        else:
            isPrime = True
    if(isPrime):
        print("Number is a prime")


if __name__ == '__main__':
    input_number = int(input('Enter the number '))
    checkPrime(input_number)
 
# This program calculates the fibonacci series till the nth term


def fibonacci_sequence(number):
    i1 = 0
    i2 = 1
    for number in range(1, number):
        #print(number)
        fib = i2 + i1
        i1 = i2
        i2 = fib
        print (fib)
        
    
    
if __name__ == '__main__':
    input_number = int(input("Enter the number of sequence digits required "))
    fibonacci_sequence(input_number)
# #Program to convert decimal to its equivalent binary
#
# def decimalToBinary(n):
#    '''Function to print binary number for the input decimal using recursion'''
#    if n > 1:
#        decimalToBinary(n//2)
#    print(n % 2,end = '')
#
# if __name__ == '__main__':
#     userInput = int(input('Enter the decimal number to find its binary equivalent: '))
#     decimalToBinary(userInput)


# P12_DecimalToBinary.py

def DecToBin(decimal):
    binary = ['Windows', 'macOS', 'Linux']
    # while (decimal):
    #     Q = decimal // 2
    #     binary.append(decimal % 2)
    #     decimal = Q
    #     print(binary)
    print(binary.reverse())


if __name__ == '__main__':
    user_input = int(input('Enter a number : '))
    DecToBin(user_input)

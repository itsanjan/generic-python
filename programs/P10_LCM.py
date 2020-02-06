# The program calculates LCM of 2 numbers
# LCM (a,b) = a.b / gcd(a,b) | input : 12 15 - Out : 60

def LCM(num1, num2):
    '''This function calculates LCM of 2 numbers takes a input by user'''
    maximum = max(num1, num2)
    i = maximum
    while True:
        if ( i % num1 == 0 and i % num2 == 0):
            lcm = i
            break
        i+= maximum

    return lcm

if __name__ == '__main__':
    usr_ip_1 = int(input('Enter first number'))
    usr_ip_2 = int(input('Enter second number'))

    print('LCM of {} and {} is {}'.format( usr_ip_1, usr_ip_2, LCM(usr_ip_1, usr_ip_2)))
# The program calculates decimal of a binary value
# 0101 = 0x2^3 + 1*2^2 + 1*2^1 + 0*2^0

def bin_to_dec(bin_num):
    '''This function calculates decimal form of a binary value using rudimentary method'''
    dec_num, index = 0, 0
    while (bin_num):
        bin_num, rem = bin_num//10, bin_num%10
        dec_num = dec_num + rem*(2**(index))
        index +=1
    return dec_num

if __name__ == '__main__':
    usr_ip = int(input('Enter binary number'))
    print('Decimal form of binary {} is {}'.format( usr_ip, bin_to_dec(usr_ip)))
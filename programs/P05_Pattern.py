
def tree_pattern(level):
    '''This function prints the following pattern:
    <blank>
    *
    **
    ***
    ****
    '''
    # ALT1
    # symbol = '*'
    # print()
    # for n in range(1, level+1):
    #     print(symbol*n)
    # ALT 2
    # for n in range(1, level+1):
    #     print()
    #     for m in range(1, n+1):
    #         print('*', end='')
    for n in range(1, level+1):
        print()
        print('*'*(n), end='')
    print('\n')


def inverted_tree_pattern(level):
    '''This function prints the following pattern:
    <blank>
    ****
    ***
    **
    *
    '''
    # for n in range(level, 0, -1):
    #     print()
    #     for m in range(n, 0, -1):
    #         print('*', end='')
    for n in range(level, 0, -1):
        print()
        print('*'*n, end='')
    print('\n')


def right_aligned_inverted_tree_pattern(level):
    '''This function prints the following pattern:
    <blank>
    ****
     ***
      **
       *
    '''
    blank_count = 0
    for n in range(level, 0, -1):
        print()
        print(' '*blank_count + '*'*n, end='')
        blank_count += 1
    print('\n')


if __name__ == "__main__":
    input_level = int(input("Enter the pattern level : "))
    tree_pattern(input_level)
    inverted_tree_pattern(input_level)
    right_aligned_inverted_tree_pattern(input_level)

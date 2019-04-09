# WAP to count the frequency in the input string


def count_character(user_input):
    for char in set(user_input):
        print(char, user_input.count(char))


if __name__ == "__main__":
    input_string = str(input("Please type the input string"))
    # input_character = str(input("Please type the input character to count"))
    count_character(input_string)

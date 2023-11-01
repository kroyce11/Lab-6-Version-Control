
def encode(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = (int(digit) + 3) % 10
        encoded_password += str(shifted_digit)
    print('Your password has been encoded and stored! ')
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        shifted_digit = (int(digit) - 3) % 10
        decoded_password += str(shifted_digit)
    return decoded_password


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def main():
    x = 0
    while x == 0:
        print_menu()
        user_input = int(input('Please enter an option: '))
        if user_input == 3:
            x = 1
        elif user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
        elif user_input == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
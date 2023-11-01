x=0

def encode(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = (int(digit) + 3) % 10
        encoded_password += str(shifted_digit)
    print('Your password has been encoded and stored! ')
    return encoded_password

def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()





while x == 0:
    print_menu()
    user_input = int(input('Please enter an option: '))
    if user_input == 3:
        x = 1
    elif user_input == 1:
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
    elif user_input == 2:
        decode(encoded_password)
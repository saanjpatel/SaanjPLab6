# Saanj Patel
# function for menu options
def password_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
# function to encode password by shifting each digit by 3
def encode(password):
    # create an empty string for encoded password
    new_password = ''
    # create for loop to change to integer, add 3, change to string, and add to final string
    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        new_password += i
    return new_password
if __name__ == '__main__':
    # creating condition and while loop
    encoding_decoding = True
    while encoding_decoding == True:
        # print menu and ask for user input
        password_menu()
        input_menu = int(input('Please enter an option: '))
        # if user inputs 1, enter password, and encode
        if input_menu == 1:
            password = input('Please enter your password to encode: ')
            encode_password = encode(password)
            print('Your password has been encoded and stored!')
        # if user inputs 2, decode, and print encoded and decoded password
        elif input_menu == 2:
            decode_password = decode(encode_password)
            print(f'The encoded password is {encode_password}, and the original password is {decode_password}.')
        # if user inputs 3, make condition false and break
        elif input_menu == 3:
            encoding_decoding = False
            break



def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):
    encoded_password = ""
    for number in password:
        new_digit = str((int(number) + 3) % 10)
        encoded_password += new_digit
    return encoded_password


def main():
    print_menu()
    option = input(f"Please enter an option: ")
    if option == "1":
        password = (input(f"Please enter your password to encode: "))
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
    elif option == "2":
        pass
    elif option == "3":
        exit()


if __name__ == '__main__':
    main()

import random
import os

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$%&/#*="

class colors:
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        WARNING = '\033[93m'
        GREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC= '\033[0m'

# Choose an option
def optionMenu():
    g_password = generatePassword()
    choice = input(colors.GREEN + "Do you want to save the password? (Y/N) > " + colors.ENDC)
    if (choice == "Y" or choice == "y"):
        os.system("echo " + g_password + " >> passwords.txt")
        print()
        print(colors.CYAN + "Password saved succesfully." + colors.ENDC)
        print()
        main()
    elif (choice == "N" or choice == "n"):
        return optionMenu()
    else:
        print("Wrong input. Try again.")

# Generate new password
def generatePassword():
    password_len = int(input(colors.CYAN + "Enter password length: " + colors.ENDC))
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(chars)
        password = password + password_char
    print(colors.WARNING + "Password: " + colors.ENDC, password)
    return password

# Main menu
def main():
    try:
        print()
        print(colors.BLUE + "Hey. Please choose an option:" + colors.ENDC)
        print("1. Generate new password")
        print("2. Show my passwords")
        print()
        choice = input("Your choice > ")
    except Exception:
        pass

if __name__ == '__main__':
    main()

while "1":
    optionMenu()    

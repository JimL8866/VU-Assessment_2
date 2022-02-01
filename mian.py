# Looks great Jim.
# Fully test the program, including attempting to view the file when the program
# is run for the very first time. Delete 'User Information. txt' to test that.
# Also, suggest to remove spaces from 'User Information. txt', to maintain compatibility.
# Provide commenting for how the script section for encryption/decrytpion works
# This will help anyone that is maintaining your code, including yourself in say 12 months
# when you have forgotten how it works.
# If you have time consider how you may accomodate a user entering a password that has a
# > greater than sign in it. e.g   my>password
# > will be encrypted to a comma, which will create issues when using .split(",")
# your script is sufficient without fixing that, but its something for you to think about.
# Its also something that should have become apparent when you were testing your script.


import os
import sys
import csv

# 95 printable ASCII characters
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*+()_-=|\}]{[\"':;?/>.<, "

print("Hello, Welcome to DigiCore Password Manager APP!")

print("Please choose from the following menu options:")


def menu():
    """ ask user to make a choice by choosing 1,2,3. Will display error message if user choose other answers"""

    user_choice = input('Press "1" for Storing your information.\nPress "2" for Viewing your information.\nPress "3" '
                        'for Exit the program.\n')
    if user_choice == "1":
        record_info()
    elif user_choice == "2":
        view_info()
    elif user_choice == "3":
        sys.exit("Thanks for using DigiCore Password Manager APP! See you soon.")
    else:
        print("Don't put other numbers or characters.Please choose 1, 2 or 3 only!")


def record_info():
    """" ask user for information and store it in a CSV file"""

    username = input("What's your username?\n")
    password = input("What's your password?\n")
    resource = input("What's the resource you want to save?\n")
    print("Thank you. Your information will be saved securely.")

    """
     use ROT3 for encrypting user data:
     This is a list comprehension.
     Extract each character in username.
     Then use find method find the position in CHARSET. 
     Then Add position with 3 to see if can mod 95 for repeat.
     if not repeat, use indexing to get the character list
     Finally use empty string and join method to make a one string.
     """
    enc_username = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in username])
    enc_password = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in password])
    enc_resource = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in resource])

    # create a csv file to store user encrypted data in each line
    with open("userInformation.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([enc_username, enc_password, enc_resource])


def view_info():
    """"read csv file and display decrypted user information in a presentable way"""

    # check if userInformation.csv file exist and not empty
    if os.path.exists("userInformation.csv") and os.stat("userInformation.csv").st_size > 0:

        try:  # use try, except to catch error: empty lines at the beginning of the csv file
            print(f"{'USERNAME':<20}{'PASSWORD':<20}{'URL':<20}")  # create a heading
            with open("userInformation.csv", "r") as data:
                user_info = csv.reader(data)
                for info in user_info:  # each row is a list
                    dec_username = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in info[0]])
                    dec_password = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in info[1]])
                    dec_resource = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in info[2]])
                    print(f"{dec_username:<20}{dec_password:<20}{dec_resource:<20}")
        except IndexError:
            print("Please remove all empty lines at the beginning of userInformation.csv.")

    else:  # if file not exist will create userInformation.csv file and if file is empty will prompt user to add info
        print('There is nothing to view at the moment. Please store some information by pressing "1".')
        new_file = open("userInformation.csv", "w")
        new_file.close()


# run in a while loop until user want to quit by choosing option 3
while True:
    menu()

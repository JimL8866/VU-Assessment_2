#Looks great Jim.
#Fully test the program, including attempting to view the file when the program
#is run for the very first time. Delete 'User Information. txt' to test that.
#Also, suggest to remove spaces from 'User Information. txt', to maintain compatibility.
#Provide commenting for how the script section for encryption/decrytpion works
#This will help anyone that is maintaining your code, including yourself in say 12 months
#when you have forgotten how it works.
#If you have time consider how you may accomodate a user entering a password that has a
#> greater than sign in it. e.g   my>password
#> will be encrypted to a comma, which will create issues when using .split(",")
#your script is sufficient without fixing that, but its something for you to think about.
#Its also something that should have become apparent when you were testing your script.


#import os module 
import os
# global constant
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\\\"':;?/>.<, " 

# print APP welcome message
print("Hello, Welcome to DigiCore Password Manager APP!")
print("Please choose from the following menu options:")


def menu():
    """ ask user to make a choice by choosing 1,2,3. Will display error message if user choose other answers"""

    try:  # use try, except to catch errors
        user_choice = input(
            'Press "1" for Storing your "username", "password" and "URL".\nPress "2" for Viewing your "username", '
            '"password" and "URL".\nPress "3" for Exit the program.\n')
        if int(user_choice) == 1:
            record_info()  # call record_info function
        elif int(user_choice) == 2:
            view_info()  # call view_info function

        elif int(user_choice) == 3:
            print("Thanks for using DigiCore Password Manager APP! See you soon.")
            exit()  # exist program
        else:  # if user put in other numbers will print out error message
            print("Don't put other numbers.Please choose 1, 2 or 3 only!")
    except ValueError:  # if user put in characters or words will print out error message
        print("Don't put characters or words.Please choose 1, 2 or 3 only!")
    

def record_info():
    """" ask user for information and store it in a text file"""

    username = input("What's your username?\n")
    password = input("What's your password?\n")
    url = input("What is the url you want to save?\n")
    print("Thank you. Your information will be saved securely.")

    """
     use ROT3 for encrypting user data:
     This is a list comprehension.
     Extract each character in username.
     Then use find method find the position in CHARSET. 
     Then Add position with 3 to see if can mod 94 for repeat.
     if not repeat use indexing to get the character list
     Finally use empty string and join method to make a one string.
     """
    enc_username = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in username])
    enc_password = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in password])
    enc_url = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in url])

    # create a text file to store user encrypted data each line
    with open("userInformation.txt", "a") as file:
        file.write(f"{enc_username}\n{enc_password}\n{enc_url}\n")


def view_info():
    """"read text file and display un-encrypted user information in a presentable way"""
    if os.path.exists("userInformation.txt") and os.stat("userInformation.txt").st_size > 0: # check if userInformation.txt file exist and not empty
        with open("userInformation.txt") as info:
            contents = info.readlines()
            
            if len(contents) % 3 == 0: 
                print(f"{'USERNAME':<20}{'PASSWORD':<20}{'URL':<20}")  # create a heading

                # use while loop to extract data accoring to format sequence : username, passowrd, url 
                num=0
                while num < len(contents):
                    username_encrypted = contents[num].strip("\n")  # strip "\n" so will not remove space character if user input space character
                    password_encrypted = contents[num + 1].strip("\n")
                    url_encrypted = contents[num + 2].strip("\n")
                    num += 3

                    # unencrypted data similar with encryption 
                    unenc_username = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in username_encrypted])
                    unenc_password = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in password_encrypted])
                    unenc_url = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in url_encrypted])
                    print(f"{unenc_username:<20}{unenc_password:<20}{unenc_url:<20}")
            else:
                print("Please remove any empty lines in userInformation.txt if this is your first time starting the APP.\n"
                      "Or You deleted some data in that file. Try to use previous one.")

    else:  # if file not exist will create userInformation.txt file and if file is empty will prompt user to add info
        print('There is nothing to view at the moment. Please store some information by pressing "1".')
        new_file = open("userInformation.txt", "w")
        new_file.close()

# run in a while loop until user want to quit by choosing option 3
while True:
    menu()
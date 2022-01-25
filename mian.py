# global constant
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "

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
    url = input("What is your url\n")
    print("Thank you. Your information will be saved securely.")

    # use ROT3 for encrypting user data
    enc_username = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in username])
    enc_password = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in password])
    enc_url = "".join([CHARSET[(CHARSET.find(c) + 3) % 95] for c in url])

    # create a text file to store user encrypted data separated by comma
    with open("User Information. txt", "a") as file:
        file.write(f"{enc_username},{enc_password},{enc_url}\n")


def view_info():
    """"read text file and display un-encrypted user information in a presentable way"""

    with open("User Information. txt") as info:
        contents = info.readlines()
        print(contents)
        print(f"{'USERNAME':<20}{'PASSWORD':<20}{'URL':<20}")  # create a heading
        for user_content in contents:
            username_encrypted = user_content.split(",")[0]  # split string to a list and choose relevant index
            password_encrypted = user_content.split(",")[1]
            url_encrypted = user_content.split(",")[2].strip()  # dispose the last newline character
            unenc_username = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in username_encrypted])
            unenc_password = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in password_encrypted])
            unenc_url = "".join([CHARSET[(CHARSET.find(c) - 3) % 95] for c in url_encrypted])
            print(f"{unenc_username:<20}{unenc_password:<20}{unenc_url:<20}")


# run in a while loop until user want to quit by choosing option 3
while True:
    menu()
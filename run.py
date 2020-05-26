#!/usr/bin/env python3.6

import unittest
from user import User
from credentials import Credential
import random
import string

def register_user(f_name, l_name, u_name, password):
    """
    Function that creates a new Password Locker user.
    """
    new_user = User(f_name, l_name, u_name, password)
    new_user.save_user()


def login_user():
    """
    Function that logs user to Password Locker.
    """
    username = input("Enter your user name \n")
    password = input("Enter your password \n")

    if User.user_exists(username):
        for user in User.user_list:
            if username == user.username and password == user.password:
                return True
            else:
                print("Invalid user name or password! Please try again.")
                # login_user()
    else:
        print("User does not exist")
        anykey = input('Kindly press any key to continue...')
        return False


def create_credentials(account_name, username, password):
    """
        Method that create new credentials
    """
    save_credentials(Credential(account_name, username, password))


def save_credentials(cred):
    """
        Method that stores existing credentials
    """
    Credential.cred_list.append(cred)


def display_credentials():
    """
        Method that displays all credentials
    """
    return Credential.cred_list


def generate_password(username):
    '''
    Method that generates random password
    '''
    return Credential.generate_password(username)

    

def delete_credentials(cred):
    '''
    Method that deletes credentials

    '''
    return  Credential.cred_list.remove()



def main():
    """
    The main function that runs before the other functions
    """
    while True:
        print("\033c")
        selection = input(
            "Welcome to The Password Locker App Developed by Jerry Nabango. Type in the following: \n \n \"login\" - to login to your account \n \"register\" - to create a new Password Locker Account. \n  \"exit\" - to Exit the Password Locker Application \n \n").lower()
        print("." * 14)

        if selection == 'register':
            print("\033c")
            f_name = input("Enter your first name \n")
            l_name = input("Enter your last name \n")
            u_name = input("Enter your username \n")
            password = input("Enter new password password \n")
            register_user(f_name, l_name, u_name, password)
            print('\n')
            print("Your Account has been created successfully!! \n")
            anykey = input('Kindly press any key to continue...')
            continue

        elif selection == 'login':
            print("\033c")
            logged_in = login_user()

            while logged_in:
                print("\033c")
                print(f" Welcome once again. Type the following:\n new - to create new credentials,\n save - to store credentials,\n display - display all credentials,\n quit - to close this section")

                selected_word = input().lower()

                if selected_word == 'new':
                    print("\033c")
                    account_name = input('Enter  your account name \n')
                    u_name = input('Enter your user name \n')
                    choice = input(
                        'Would you like to autogenerate your password?(yes/no) \n').lower()
                    if choice == 'yes':
                        print("\n")
                        print("your random password is {password} ")
                        password = Credential.generate_password(u_name)
                        
                        
                    elif choice == "no":
                        password = input('Enter password \n')

                    create_credentials(account_name, u_name, password)

                elif selected_word == 'save':
                    print("\033c")
                    account_name = input('Enter your account name \n')
                    u_name = input('Enter your user name \n')
                    password = input('Enter your password \n')

                    create_credentials(account_name, u_name, password)
                    print("Successfully added!! \n")
                    anykey = input('Kindly press any key to continue...')

                elif selected_word == 'display':
                    print("\033c")
                    logged_in = login_user()

                    if logged_in and Credential.cred_list:
                        print("\033c")
                        print("Here is a list of all your accounts details")
                        print("\n")

                        for account in display_credentials():
                            print("-"*10)
                            print(f"Account: {account.account_name}")
                            print(f"Login: {account.username}")
                            print(f"Password: {account.password}")
                            print('\n')

                            '''
                            Choice to delete credentials.

                            '''
                            choice = input("Would you like to delete the credentials?(yes/no)\n")
                            if choice == "Yes":
                                delete_credentials(Credential(account_name, u_name, password))
                                print("Successfully deleted credentials")
                                print("\n")
                                anykey = input('Kindly press any key to continue...')
                                
                    else:
                        print('\n')
                        print("You do not have any saved details yet")
                        print('\n')

                    print('\n \n')
                    anykey = input('Kindly press any key to continue...')

                # elif selected_word == 'delete':
                #     print("\033c")
                #     Credential.cred_list.remove(account_name, u_name, password)

                elif selected_word == 'quit':
                    print('See you again!')
                    break
                else:
                    print("Invalid Input")

        else:
            print("Thank you for using Password Locker . See you again!!.")
            break


if __name__ == '__main__':
    main()
import re

# Encryption Psw
encrypt_key = input("Please enter your password: ")

def add_psw(username,psw):
    with open("psw.txt","a") as file:
        file.write(username + ":" + psw + "\n")
        return

def view_psw():
    with open("psw.txt","r") as file:
        for line in file:
            username,psw = line.split(":")
            print(f"Username: {username} \nPassword: {psw}")



while True:

    operation = int(input("Please enter your operation:  \n"
                          "1: View Password \n"
                          "2: Add New Password \n"
                          "3: Quit\n"))

    if operation == 1:
        view_psw()


    elif operation == 2:
        username = input("Enter Username: ")
        psw = input("Enter Password: ")

        add_psw(username,psw)

    elif operation == 3:
        print('Exiting Psw Manger')
        break

    else:
        print("Invalid Operation")

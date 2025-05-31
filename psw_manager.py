import re


def main():
    """
    Main function to run the password manager.

    This function prompts the user for a Master Password,
    Enters the infinite Loop if the password is of invalid len until valid.

    Prompts the user to enter their operation.

    """
    
    masterPassword = input("Please enter your password: ") # Encryption Key 
    
    while len(masterPassword) >15 or len(masterPassword) <6:
        print("Password must be between 15 and 6 characters")
        masterKey = input("Please enter your password: ")

        while True:

            operation = int(input("Please enter your operation:  \n"
                                  "1: View Password \n"
                                  "2: Add New Password \n"
                                  "3: Quit\n"))

            if operation == 1:
                view_psw(masterKey)


            elif operation == 2:
                username = input("Enter Username: ")
                psw = input("Enter Password: ")

                add_psw(username, psw,masterKey)

            elif operation == 3:
                print('Exiting Psw Manger')
                return

            else:
                print("Invalid Operation")


def xor_encrypt_decrypt(raw_psw, key):
    """
    Encrypts or decrypts a password using the XOR cipher.

    This function iterates through each character of the raw password, XORs it with a character from the key,
    and concatenates the resulting characters to form the encrypted/decrypted password.

    :param raw_psw: The password to be encrypted or decrypted (string).
    :param key: The encryption/decryption key (string).
    :return: The encrypted or decrypted password (string).

    """
    encrypted_chars=[]
    for i in range(len(raw_psw)):
        char = raw_psw[i]
        key_char = key[i % len(key)]
        encrypted_chars.append(chr(ord(char) ^ ord(key_char)))

    encrypted_psw = "".join(encrypted_chars)
    return encrypted_psw


"""
Functions to handle password operations:
    1. Add a new password.
    2. View existing passwords.
    3. Quit the application.
    
    Parameters:
    - acc_name: The account name for the password (string).
    - password: The password to be encrypted and stored (string).
    - masterKey: The encryption/decryption key (string).
"""
def add_psw(acc_name,password,masterKey):
    encrypted_password = xor_encrypt_decrypt(password,masterKey)

    with open("psw.txt","a") as file:
        file.write(acc_name + ":" + encrypted_password + "\n")
        return

def view_psw(masterKey):
    with open("psw.txt","r") as file:
        for line in file:

            userName,psw = line.split(":")
            psw= xor_encrypt_decrypt(psw,masterKey)
            print(f"Username: {userName} \nPassword: {psw}")




if __name__ == "__main__":
    main()
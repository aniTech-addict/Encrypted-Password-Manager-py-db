import re


def main():
    """
    Main function to run the password manager.

    This function prompts the user for a Master Password,
    Enters the infinite Loop if the password is of invalid len until valid.

    Calls operation_index function that prompts for user input and handles operation_indexs as per req

    """
    master_key = input("Please enter your password: ") # Encryption Key
    while not 6<= len(master_key) <=15:
        print("Password must be between 15 and 6 characters")
        master_key = input("Please enter your password: ")

    handle_operations(master_key)



def xor_encrypt_decrypt(raw_psw, master_key):
    """
    Encrypts or decrypts a password using the XOR cipher.

    This function iterates through each character of the raw password, XORs it with a character from the key,
    and concatenates the resulting characters to form the encrypted/decrypted password.

    :param raw_psw: The password to be encrypted or decrypted (string).
    :param master_key: The encryption/decryption key (string).
    :return: The encrypted or decrypted password (string).

    """
    encrypted_chars=[]
    for i in range(len(raw_psw)):
        char = raw_psw[i]
        key_char = master_key[i % len(master_key)]
        encrypted_chars.append(chr(ord(char) ^ ord(key_char)))

    encrypted_psw = "".join(encrypted_chars)
    return encrypted_psw


def handle_operations(master_key):
    while True:

        operation_index = int(input("Please enter your operation_index:  \n"
                                  "1: View Password \n"
                                  "2: Add New Password \n"
                                  "3: Search Password\n"
                                  "4: Quit"))



        if operation_index == 1:
            view_psw(master_key)


        elif operation_index == 2:
            username = input("Enter Username: ")
            raw_psw = input("Enter Password: ")

            add_password(username, raw_psw,master_key)

        elif operation_index == 3:
            search_psw(master_key)

        elif operation_index == 4:
            print('-----------------\nExiting Password Manger\n------------------')
            return

        else:
            print("Invalid operation_index")


"""
Functions to handle password operation_indexs:
    1. Add a new password.
    2. View existing passwords.
    3. Search for a password by account name.
    
    
    Parameters:
    - acc_name: The account name for the password (string).
    - password: The password to be encrypted and stored (string).
    - master_key: The encryption/decryption key (string).
"""
def add_password(acc_name,raw_password,master_key):
    encrypted_password = xor_encrypt_decrypt(raw_password,master_key)

    with open("psw.txt","a") as file:
        file.write(acc_name + ":" + encrypted_password + "\n")


def view_psw(master_key):
    with open("psw.txt","r") as file:
        for line in file:

            username,encrypted_password = line.split(":",1)

            decrypted_password= xor_encrypt_decrypt(encrypted_password.strip(), master_key)
            print(f"Username: {username} \nPassword: {decrypted_password}")

def search_psw(master_key):

    search_pattern = input("Enter the account name to search: ")
    found = False

    with open("psw.txt","r") as file:
        for line in file:
            username,encrypted_password = line.split(":",1)

            if re.search(search_pattern,username):
                decrypted_password = xor_encrypt_decrypt(encrypted_password.strip(),master_key)
                print(f"Username: {username} \nPassword: {decrypted_password}")

                found = True

        if not found:
            print("No matching account found.")





if __name__ == "__main__":
    main()
from manager import PasswordManager


def main():
    """
    Main entry point for the password manager application.
    Prompts the user to enter a master password, ensuring it is between 6 and 15 characters.
    Initializes the PasswordManager with the provided password and database file,
    then delegates further operations to the handle_operations function.
    Raises:
        None
    Returns:
        None
    """
    

    master_key = input("Please enter your password: ") # Encryption Key
    while not 6<= len(master_key) <=15:
        print("Password must be between 15 and 6 characters")
        master_key = input("Please enter your password: ")

    pm = PasswordManager("passwords.db", master_key)
    handle_operations(pm,master_key)


def handle_operations(pm,master_key):
    while True:

        operation_index = int(input("Please enter your operation_index:  \n"
                                  "1: View Password \n"
                                  "2: Add New Password \n"
                                  "3: Search Password\n"
                                  "4: Quit\n"
                                  "----->"))



        if operation_index == 1:
            pm.view_passwords()


        elif operation_index == 2:
            username = input("Enter Username: ")
            raw_psw = input("Enter Password: ")

            pm.add_password(username,raw_psw)

        elif operation_index == 3:
            username = input("Enter Usename to Search for: ")
            pm.search_password(username)

        elif operation_index == 4:
            print('-----------------\nExiting Password Manger\n------------------')
            return

        else:
            print("Invalid operation_index")


if __name__ == "__main__":
    main()
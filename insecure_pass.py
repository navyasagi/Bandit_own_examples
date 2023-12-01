def insecure_authentication(username, password):
    # Insecure storage of user credentials in plain text
    with open("user_credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

if __name__ == "__main__":
    # User input for username and password
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    # Insecure authentication function that stores credentials in plain text
    insecure_authentication(username_input, password_input)

def insecure_file_handling(filename):
    # User input is directly used to construct a file path
    file_path = f"/var/www/{filename}"

    # Attempt to read the contents of the file
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # User input from an untrusted source (e.g., user input) is directly used in a file path
    user_input = input("Enter filename: ")
    insecure_file_handling(user_input)

import random
import string

def generate_password(length):
    # Define the characters that will be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random choices from the characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Ask the user for the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Validate the length
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()

import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def include_letters():
    response = input("Include letters (y/n)? ").lower()
    return response == "y"

def include_symbols():
    response = input("Include symbols (y/n)? ").lower()
    return response == "y"

def generate_secure_password(length, use_letters, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.digits + string.punctuation

    if not characters:
        print("Error: You must include either letters or symbols.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = get_password_length()
    use_letters = include_letters()
    use_symbols = include_symbols()

    secure_password = generate_secure_password(password_length, use_letters, use_symbols)
    if secure_password:
        print("Secure Password:", secure_password)

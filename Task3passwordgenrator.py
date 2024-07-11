import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("No character types selected! Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue

            use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

            password = generate_password(length, use_upper, use_lower, use_digits, use_special)
            if password:
                print(f"Generated password: {password}")

            next_password = input("Do you want to generate another password? (yes/no): ")
            if next_password.lower() == "no":
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

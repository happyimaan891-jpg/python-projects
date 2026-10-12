# Password Generator in Python

import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    # Characters to choose from
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    digits = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special else ""

    # Combine all allowed characters
    all_characters = letters + digits + special_chars

    if not all_characters:
        return "Error: No character types selected!"

    # Ensure password contains at least one character from each selected set
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))

    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the characters to make the password unpredictable
    random.shuffle(password)

    return "".join(password)

def main():
    print("==========================================")
    print("       RANDOM PASSWORD GENERATOR          ")
    print("==========================================")

    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("Length too short! Setting default length to 6.")
            length = 6
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12

    include_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, include_digits, include_special)

    print("\n------------------------------------------")
    print(f"Generated Password: {password}")
    print("------------------------------------------")

if __name__ == "__main__":
    main()

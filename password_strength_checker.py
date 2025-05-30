import re

def check_password_strength(password):
    """
    Checks the strength of the given password based on:
    - Length (8 or more characters)
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of digits
    - Presence of special characters
    """
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count how many criteria are met
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    print("\nPassword Strength Assessment:")
    print(f"Length: {'OK' if not length_error else 'Too Short'}")
    print(f"Uppercase: {'OK' if not uppercase_error else 'Missing'}")
    print(f"Lowercase: {'OK' if not lowercase_error else 'Missing'}")
    print(f"Digits: {'OK' if not digit_error else 'Missing'}")
    print(f"Special Characters: {'OK' if not special_char_error else 'Missing'}")
    print(f"\nOverall Strength: {strength}")

def main():
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter a password to assess: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()

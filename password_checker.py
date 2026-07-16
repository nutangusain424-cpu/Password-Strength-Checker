import re

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check numbers
    if re.search(r"\d", password):
        score += 1

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Display missing requirements
    print("\nPassword Analysis")
    print("-" * 30)

    if len(password) < 8:
        print("❌ Password should be at least 8 characters long.")

    if not re.search(r"[A-Z]", password):
        print("❌ Add at least one uppercase letter.")

    if not re.search(r"\d", password):
        print("❌ Add at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("❌ Add at least one special character.")

    print("-" * 30)

    # Determine strength
    if score <= 1:
        strength = "Weak 🔴"
    elif score <= 3:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    print(f"Password Strength: {strength}")


def main():
    print("=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("Enter your password: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
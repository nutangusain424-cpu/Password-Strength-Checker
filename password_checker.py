def check_password_strength(password):
    score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    if len(password) >= 8:
        score += 1

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    print("\nPassword Analysis")
    print("----------------------------")

    print("Length >=8 :", "Yes" if len(password) >= 8 else "No")
    print("Uppercase  :", "Yes" if has_upper else "No")
    print("Lowercase  :", "Yes" if has_lower else "No")
    print("Digit      :", "Yes" if has_digit else "No")
    print("Special    :", "Yes" if has_special else "No")

    print("\nScore:", score, "/5")

    if score <= 2:
        print("Strength : Weak")
    elif score <= 4:
        print("Strength : Medium")
    else:
        print("Strength : Strong")


password = input("Enter your password: ")

check_password_strength(password)
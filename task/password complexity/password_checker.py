import re

def check_password_strength(password):
    # Criteria weights
    strength_score = 0
    
    # Check length
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        print("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should include at least one special character.")

    # Provide feedback based on strength
    if strength_score == 5:
        print("Strong password!")
    elif 3 <= strength_score < 5:
        print("Moderate password. Consider adding more complexity.")
    else:
        print("Weak password. Improve based on the suggestions above.")

# Run the tool
def main():
    print("Welcome to the FOTECH Password Complexity Checker")
    print("Enter your password to check its strength.")
    
    password = input("Password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()

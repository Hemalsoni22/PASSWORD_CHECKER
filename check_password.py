
import re

def strength_check(password):
    length = int(bool(len(password) >= 8))
    uppercase = int(bool(re.search(r'[A-Z]',password)))
    lowercase = int(bool(re.search(r'[a-z]',password)))
    digit = int(bool(re.search(r'[0-9]',password)))
    special_char = int(bool(re.search(r'[\W_]',password)))

    score = length + uppercase + lowercase + digit + special_char

    if score == 5:
        strength = "Very Strong"
    if score == 4:
        strength = "Strong"
    if score == 3:
        strength = "Medium"
    if score == 2:
        strength = "Weak"
    if score == 1:
        strength = "Very Weak"

    feedback = []

    if length < 1:
        feedback.append("at least 8 characters")
    if uppercase < 1:
        feedback.append("at least one Uppercase letter.")
    if lowercase < 1:
        feedback.append("at least one lowercase letter.")
    if digit < 1:
        feedback.append("at least one digit.")
    if special_char < 1:
        feedback.append("at least one special character.")

    return strength, feedback

while True:
    password = input("Enter your password: ")
    strength, feedback = strength_check(password)
    print(f"Password Strength: {strength}\n")

    if(strength != "Very Strong"):
        print("Your password should contain: ")
        for comment in feedback:
            print(f" {comment}")
        print("\n")

    else:
        break

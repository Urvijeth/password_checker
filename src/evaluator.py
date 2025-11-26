import re
from src.utils import load_common_passwords

def evaluate_password(password):
    score = 0
    passed = []
    failed = []
    suggestions = []

    # Load common passwords
    common = load_common_passwords()

    # 1. Check if password is common
    if password.lower() in common:
        return {
            "score": 5,
            "label": "Very Weak",
            "passed": [],
            "failed": ["Password is too common"],
            "suggestions": ["Avoid common passwords like '123456', 'password', 'admin'"]
        }

    # 2. Length score
    if len(password) >= 12:
        score += 30
        passed.append("Good length")
    elif len(password) >= 8:
        score += 20
        passed.append("Okay length")
    else:
        score += 5
        failed.append("Password is too short")
        suggestions.append("Use at least 8–12 characters")

    # 3. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 15
        passed.append("Uppercase letters")
    else:
        failed.append("Missing uppercase letters")
        suggestions.append("Add uppercase letters (A–Z)")

    # 4. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 15
        passed.append("Lowercase letters")
    else:
        failed.append("Missing lowercase letters")
        suggestions.append("Add lowercase letters (a–z)")

    # 5. Numbers
    if re.search(r"[0-9]", password):
        score += 15
        passed.append("Numbers")
    else:
        failed.append("Missing numbers")
        suggestions.append("Add numbers (0–9)")

    # 6. Special characters
    if re.search(r"[!@#$%^&*()_+=\-[\]{};:'\",.<>/?]", password):
        score += 15
        passed.append("Special characters")
    else:
        failed.append("Missing special characters")
        suggestions.append("Add special characters (#, @, !, %, etc.)")

    # 7. Simple pattern check
    if re.search(r"(.)\1\1\1", password):  # repeated characters
        score -= 10
        failed.append("Too many repeated characters")
        suggestions.append("Avoid repeating characters (aaaa, 1111)")
    
    # Normalize score
    if score < 0:
        score = 0
    if score > 100:
        score = 100

    # Label
    if score < 30:
        label = "Weak"
    elif score < 60:
        label = "Medium"
    elif score < 80:
        label = "Good"
    else:
        label = "Strong"

    return {
        "score": score,
        "label": label,
        "passed": passed,
        "failed": failed,
        "suggestions": suggestions
    }

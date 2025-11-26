import os

COMMON_PASSWORDS_PATH = "src/common_passwords.txt"

def load_common_passwords():
    """Load list of weak/common passwords from file."""
    if not os.path.exists(COMMON_PASSWORDS_PATH):
        return set()

    with open(COMMON_PASSWORDS_PATH, "r") as f:
        return set(line.strip().lower() for line in f.readlines())

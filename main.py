#!/usr/bin/env python3
import argparse
from src.evaluator import evaluate_password

def print_result(res):
    print(f"\nPassword score: {res['score']} / 100")
    print(f"Strength: {res['label']}\n")
    if res.get("passed"):
        print("Rules passed:", ", ".join(res["passed"]))
    if res.get("failed"):
        print("Rules failed:", ", ".join(res["failed"]))
    if res.get("suggestions"):
        print("\nSuggestions:")
        for s in res["suggestions"]:
            print(" -", s)
    print()

def main():
    parser = argparse.ArgumentParser(description="Simple Password Strength Checker")
    parser.add_argument("password", nargs="?", help="Password to check (if omitted, you'll be prompted)")
    args = parser.parse_args()

    if args.password:
        pwd = args.password
    else:
        try:
            pwd = input("Enter password to check: ")
        except (KeyboardInterrupt, EOFError):
            print("\nCancelled.")
            return

    result = evaluate_password(pwd)
    print_result(result)

if __name__ == "__main__":
    main()

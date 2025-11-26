import tkinter as tk
from tkinter import messagebox
from src.evaluator import evaluate_password

def check_password():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    
    result = evaluate_password(pwd)

    output = (
        f"Score: {result['score']} / 100\n"
        f"Strength: {result['label']}\n\n"
    )

    if result['failed']:
        output += "Suggestions:\n"
        for s in result["suggestions"]:
            output += f" - {s}\n"

    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, output)
    text_box.config(state="disabled")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=40)# to disable add show="*"
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password, width=20).pack(pady=10)

text_box = tk.Text(root, height=10, width=50, state="disabled")
text_box.pack(pady=10)

root.mainloop()

import pandas as pd
import string
import pickle


from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import tkinter as tk
from tkinter import messagebox


def text_process(review):
    
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

try:
    with open('/MINI PROJECT/APP/svc.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    raise Exception("Model file not found. Ensure 'svc.pkl' is in the correct path.")


def check_review():
    review_text = review_input.get("1.0", tk.END).strip()
    if not review_text:
        messagebox.showwarning("Input Error", "Please enter a review!")
        return
    
    
    prediction = model.predict([review_text])[0]
    result = "Fake" if prediction == 0 else "Genuine"
    result_label.config(text=f"The review is: {result}", fg="red" if result == "Fake" else "green")


root = tk.Tk()
root.title("Fake Review Detector")
root.geometry("500x600")
root.configure(bg="#f0f8ff")


header_label = tk.Label(root, text="Fake Review Detector", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333333")
header_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter the review below:", font=("Arial", 14), bg="#f0f8ff", fg="#555555")
instruction_label.pack(pady=5)

review_input = tk.Text(root, height=10, width=50, font=("Arial", 12))
review_input.pack(pady=10)

check_button = tk.Button(root, text="Check Review", font=("Arial", 14), bg="#4caf50", fg="white", command=check_review)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
result_label.pack(pady=20)


root.mainloop()

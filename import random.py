import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
        self.lower_bound = 1
        self.upper_bound = 100
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        
        self.label = tk.Label(root, text=f"Guess a number between {self.lower_bound} and {self.upper_bound}:", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=6)
        self.entry.bind("<Return>", self.check_guess)
        
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=5)
        
    def check_guess(self, event=None):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.lower_bound or guess > self.upper_bound:
                messagebox.showerror("Error", "Out of bounds! Try again.")
            elif guess < self.secret_number:
                messagebox.showinfo("Hint", "Too low! Try again.")
            elif guess > self.secret_number:
                messagebox.showinfo("Hint", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} in {self.attempts} attempts.")
                self.root.quit()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

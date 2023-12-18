import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Create and set up GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        tk.Label(self.root, text="Choose rock, paper, or scissors:").pack(pady=10)

        # Buttons for user choices
        tk.Button(self.root, text="Rock", command=lambda: self.play("rock")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Paper", command=lambda: self.play("paper")).pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors")).pack(side=tk.LEFT, padx=10)

        # Label to display user's and computer's choices
        self.choices_label = tk.Label(self.root, text="")
        self.choices_label.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        # Label to display the scores
        self.scores_label = tk.Label(self.root, text="Score: User - 0, Computer - 0")
        self.scores_label.pack(pady=10)

    def play(self, user_choice):
        # Dictionary to map choices to outcomes
        outcomes = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        # Computer randomly chooses rock, paper, or scissors
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display user's and computer's choices
        choices_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}"
        self.choices_label.config(text=choices_text)

        # Determine the winner
        if user_choice == computer_choice:
            result_text = "It's a tie!"
        elif outcomes[user_choice] == computer_choice:
            result_text = "You win!"
            self.user_score += 1
        else:
            result_text = "Computer wins!"
            self.computer_score += 1

        # Display the result
        self.result_label.config(text=result_text)

        # Update and display the scores
        scores_text = f"Score: User - {self.user_score}, Computer - {self.computer_score}"
        self.scores_label.config(text=scores_text)

        # Ask the user if they want to play again
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            # Reset choices and result labels
            self.choices_label.config(text="")
            self.result_label.config(text="")
        else:
            # Exit the game
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

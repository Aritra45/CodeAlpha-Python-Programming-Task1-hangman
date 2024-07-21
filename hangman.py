import random
import tkinter as tk
from tkinter import messagebox

def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "developer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def check_guess():
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if guess in guessed_letters:
        messagebox.showinfo("Hangman", "You already guessed that letter. Try again.")
        return
    
    guessed_letters.add(guess)
    
    if guess in word:
        messagebox.showinfo("Hangman", f"Congratulations! You've guessed the word: {word}")
        root.after(1000, reset_game)
    else:
        global incorrect_guesses
        incorrect_guesses += 1
        
        if incorrect_guesses >= max_incorrect_guesses:
            messagebox.showinfo("Hangman", f"You've run out of guesses. The word was: {word}")
            root.after(1000, reset_game)
        else:
            messagebox.showinfo("Hangman", f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
    
    current_display = display_word(word, guessed_letters)
    word_label.config(text=current_display)

def reset_game():
    global word, guessed_letters, incorrect_guesses
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0

    
    pre_suggested_letters = random.sample(word, 2)
    guessed_letters.update(pre_suggested_letters)
    
    word_label.config(text=display_word(word, guessed_letters))

def exit_game():
    root.destroy()

if __name__ == "__main__":
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("400x400")
    root.config(bg="#282c34")

    title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 24, "bold"), bg="#61dafb", fg="#282c34")
    title_label.pack(pady=20)

    word_label = tk.Label(root, text=display_word(word, guessed_letters), font=("Helvetica", 18), bg="#282c34", fg="#ffffff")
    word_label.pack(pady=20)

    guess_frame = tk.Frame(root, bg="#282c34")
    guess_frame.pack(pady=10)

    guess_entry = tk.Entry(guess_frame, font=("Helvetica", 18), width=10)
    guess_entry.grid(row=0, column=0, padx=10)

    guess_button = tk.Button(guess_frame, text="Guess", command=check_guess, font=("Helvetica", 18), bg="#61dafb", fg="#282c34", activebackground="#21a1f1", activeforeground="#ffffff")
    guess_button.grid(row=0, column=1, padx=10)

    button_frame = tk.Frame(root, bg="#282c34")
    button_frame.pack()

    reset_button = tk.Button(button_frame, text="Reset", command=reset_game, font=("Helvetica", 18), bg="#61dafb", fg="#282c34", activebackground="#21a1f1", activeforeground="#ffffff")
    reset_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_game, font=("Helvetica", 18), bg="#f44336", fg="#ffffff", activebackground="#d32f2f", activeforeground="#ffffff")
    exit_button.pack(side=tk.LEFT, padx=10)

    
    reset_game()

    root.mainloop()

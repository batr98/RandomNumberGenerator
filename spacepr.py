import tkinter as tk
import random
window=tk.Tk()
window.title("It project")
window.geometry("400*300")
secret=random.randint(1,100)
attempts_left=7

def guess():
    global attempts_left
    guess=entry.get()
    if not guess.isdigit():
        result.config(text="Please enter a valid number")
        return
    guess=int(guess)
    if guess==secret:
        result.config(text="Congratulations! You guessed it!")
        button.config(state="disabled")
    else:
        attempts_left -= 1
        if attempts_left == 0:
            result.config(text=f"Game over! The number was {secret}.")
            button.config(state="disabled")
        elif guess < secret:
            result.config(text=f"Guessed number is bigger. Attempts left: {attempts_left}")
        else:
            result.config(text=f"Guessed number is smaller. Attempts left: {attempts_left}")
entry=tk.Entry(window)
entry.pack()

result=tk.Label(window,text="")
result.pack(pady=10)

button=tk.Button(window,text="Click here",command=guess)
button.pack(pady=10)

window.mainloop()
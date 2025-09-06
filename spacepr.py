import tkinter as tk
import random
window=tk.Tk()
window.title("It project")
window.geometry("400*300")
secret=random.randint(1,100)
attempts_left=7

def guess():
    pass
entry=tk.Entry(window)
entry.pack()

result=tk.Label(window,text="")
result.pack(pady=10)

button=tk.Button(window,text="Click here",command=guess)
button.pack(pady=10)

window.mainloop()
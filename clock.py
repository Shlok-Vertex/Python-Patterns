import tkinter as tk
from tkinter import Label
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


root = tk.Tk()
root.title("Beautiful Clock made by Shlok...")
root.geometry("400x200")
root.configure(bg="#2c3e50")


clock_label = Label(
    root,
    text="",
    font=("Helvetica", 48, "bold"),
    fg="#ecf0f1",
    bg="#2c3e50",
    pady=20
)
clock_label.pack(expand=True)


title_label = Label(
    root,
    text="Digital Clock",
    font=("Helvetica", 20, "italic"),
    fg="#ecf0f1",
    bg="#2c3e50"
)
title_label.pack()


update_time()

root.mainloop()

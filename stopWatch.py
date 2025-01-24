import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Beautiful Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg="#1abc9c")

        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        self.label = tk.Label(
            root,
            text="00:00:00",
            font=("Helvetica", 48, "bold"),
            fg="#ffffff",
            bg="#1abc9c"
        )
        self.label.pack(pady=50)

        self.start_button = tk.Button(
            root,
            text="Start",
            font=("Helvetica", 14),
            bg="#27ae60",
            fg="#ffffff",
            width=10,
            command=self.start
        )
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(
            root,
            text="Pause",
            font=("Helvetica", 14),
            bg="#e67e22",
            fg="#ffffff",
            width=10,
            command=self.pause
        )
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(
            root,
            text="Reset",
            font=("Helvetica", 13),
            bg="#c0392b",
            fg="#ffffff",
            width=10,
            command=self.reset
        )
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.display_time()
            self.root.after(50, self.update)

    def display_time(self):
        mins, secs = divmod(self.elapsed_time, 60)
        hrs, mins = divmod(mins, 60)
        time_string = f"{int(hrs):02}:{int(mins):02}:{int(secs):02}"
        self.label.config(text=time_string)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update()

    def pause(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
import random

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Joke Generator")
        
        self.jokes = []
        
        self.label = tk.Label(root, text="Welcome to the Random Joke Generator!", wraplength=300, justify="center")
        self.label.pack(pady=20)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.load_button = tk.Button(self.button_frame, text="Load Jokes", command=self.load_jokes)
        self.load_button.pack(side="left", padx=10)
        
        self.joke_button = tk.Button(self.button_frame, text="Show Random Joke", command=self.show_random_joke)
        self.joke_button.pack(side="right", padx=10)
        
        self.joke_label = tk.Label(root, text="", wraplength=300, justify="center")
        self.joke_label.pack(pady=20)
        
    def load_jokes(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.jokes = file.readlines()
                messagebox.showinfo("Success", "Jokes loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load jokes: {e}")
    
    def show_random_joke(self):
        if self.jokes:
            joke = random.choice(self.jokes).strip()
            self.joke_label.config(text=joke)
        else:
            messagebox.showwarning("No Jokes", "Please load jokes first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()

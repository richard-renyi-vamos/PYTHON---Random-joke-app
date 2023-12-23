import tkinter as tk
import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms?\nBecause they make up everything!",
    "Parallel lines have so much in common.\nIt's a shame they'll never meet.",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field!"
    # Add more jokes to this list
]

# Function to show a random joke
def show_joke():
    random_joke = random.choice(jokes)
    joke_label.config(text=random_joke)

# Create the main window
root = tk.Tk()
root.title("Random Joke Generator")

# Label to display the joke
joke_label = tk.Label(root, text="", wraplength=300, font=("Arial", 12))
joke_label.pack(padx=20, pady=20)

# Button to show a new joke
show_joke_button = tk.Button(root, text="Show Joke", command=show_joke)
show_joke_button.pack(padx=10, pady=10)

# Run the application
root.mainloop()

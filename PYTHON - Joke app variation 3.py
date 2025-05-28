import random

def get_random_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😄",
        "Why don’t skeletons fight each other? They don’t have the guts! 💀😅",
        "Why did the bicycle fall over? Because it was two-tired! 🚲😂",
        "I'm reading a book on anti-gravity. It's impossible to put down! 📚🌌",
        "Did you hear about the claustrophobic astronaut? He just needed a little space. 🚀😆",
        "Parallel lines have so much in common… it’s a shame they’ll never meet. 📏😭",
        "Why can’t you hear a pterodactyl in the bathroom? Because the ‘P’ is silent! 🦖🚽",
        "I told my wife she was drawing her eyebrows too high. She looked surprised. 😳🎨",
        "Why don’t eggs tell jokes? They’d crack each other up! 🥚🤣",
        "I would tell you a construction joke, but I’m still working on it. 🏗️😜"
    ]
    return random.choice(jokes)

def main():
    print("🎉 Welcome to the Python Joke App! 😂\n")
    while True:
        input("Press Enter to hear a joke or type 'q' to quit: ")
        joke = get_random_joke()
        print("\n" + joke + "\n")
        if input("Wanna hear another one? (y/n): ").lower() != 'y':
            break
    print("Thanks for laughing with us! 🤗 See you next time!")

if __name__ == "__main__":
    main()

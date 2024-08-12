import random

# List of 100 random words
words = ["hangman", "python", "computer", "programming", "algorithm", "internet", "keyboard", "software", "developer", "application", 
         "database", "network", "variable", "function", "loop", "conditional", "statement", "integer", "string", "list", "tuple", 
         "dictionary", "module", "package", "object", "class", "inheritance", "polymorphism", "encapsulation", "abstraction", 
         "iteration", "recursion", "debugging", "testing", "optimization", "exception", "file", "input", "output", "interface", 
         "algorithm", "data", "structure", "binary", "tree", "graph", "sorting", "searching", "hashing", "queue", "stack", "linked", 
         "list", "array", "pointer", "memory", "allocation", "garbage", "collection", "compiler", "interpreter", "runtime", 
         "environment", "operating", "system", "kernel", "shell", "desktop", "application", "web", "server", "client", "browser", 
         "html", "css", "javascript", "framework", "library", "version", "control", "git", "repository", "branch", "merge", 
         "conflict", "repository", "remote", "clone", "pull", "push", "fork", "commit", "database", "SQL", "MySQL", "PostgreSQL", 
         "MongoDB", "SQLite"]

def choose_word(words):
    """Choose a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters and placeholders for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_guesses):
    """Display the hangman based on the number of incorrect guesses."""
    hangman_parts = [
        """
           _________
          |         |
          |
          |
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |         |
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |        /|
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |        /|\\
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |        /|\\
          |        /
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _________
          |         |
          |         O
          |        /|\\
          |        / \\
          |
          |
         _|_
        |   |______
        |__________|
        """
    ]
    return hangman_parts[incorrect_guesses]

def hangman():
    word = choose_word(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))
        else:
            print("Good guess!")

        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            break

    if incorrect_guesses == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()

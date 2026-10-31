
import random
import re
from collections import Counter

# --------------------------------
# NUMBER GUESSING GAME
# --------------------------------

def number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    score = 100

    print("Guess a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess == secret_number:
                score = max(10, 100 - (attempts - 1) * 15)

                print("\nCongratulations! You guessed correctly!")
                print("Number of attempts:", attempts)
                print("Your score:", score)
                break

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            print("Attempts remaining:", max_attempts - attempts)

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("\nGame Over!")
        print("The correct number was:", secret_number)
        print("Your score: 0")


# --------------------------------
# WORD COUNTER AND FREQUENCY ANALYSIS
# --------------------------------

def word_counter():
    print("\n===== WORD COUNTER =====")

    filename = input("Enter the text file name (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Count total words
        words = re.findall(r"\b[\w']+\b", text.lower())

        total_words = len(words)
        unique_words = len(set(words))

        # Calculate word frequency
        word_frequency = Counter(words)

        print("\n===== TEXT ANALYSIS RESULTS =====")
        print("Total words:", total_words)
        print("Unique words:", unique_words)

        print("\nWord Frequency:")

        for word, frequency in word_frequency.most_common():
            print(f"{word}: {frequency}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")


# --------------------------------
# MAIN MENU
# --------------------------------

def main():

    while True:
        print("\n================================")
        print(" NUMBER GUESSING & WORD COUNTER")
        print("================================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("\nThank you for using the program!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()

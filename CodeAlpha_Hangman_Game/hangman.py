
import random

def play_game():

    categories = {
        "Fruits": ["apple", "banana", "mango"],
        "Technology": ["python", "coding", "laptop"],
        "Animals": ["tiger", "rabbit", "monkey"]
    }

    print("\nChoose a Category:")
    print("1. Fruits")
    print("2. Technology")
    print("3. Animals")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        category = "Fruits"
    elif choice == "2":
        category = "Technology"
    elif choice == "3":
        category = "Animals"
    else:
        category = "Technology"

    word = random.choice(categories[category])

    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6
    score = 0

    while wrong_guesses < max_attempts:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print(f"❤️ Lives Left: {max_attempts - wrong_guesses}")
        print(f"⭐ Score: {score}")

        guess = input("🔤 Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter only one alphabet!")
            continue

        if guess in guessed_letters:
            print("🔄 Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
            score += 10
        else:
            print("❌ Wrong!")
            wrong_guesses += 1
            score -= 2

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 YOU WON!")
            print("🏆 Word:", word)
            print("⭐ Final Score:", score)
            return

    print("\n💀 GAME OVER!")
    print("📌 Word was:", word)


print("🎮 WELCOME TO HANGMAN GAME 🎮")

play_again = "yes"

while play_again == "yes":
    play_game()
    play_again = input("\n🔄 Play Again? (yes/no): ").lower()

print("👋 Thanks for playing!")
import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_guessing_game()
    else:
        print("Thank you for playing!")

# Start the game
play_guessing_game()

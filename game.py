# --- Number Guessing Game ---
# This is the template file for the collaborative Git tutorial.

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(secret_number, player_guess):
    if player_guess == secret_number:
        return "correct"
    elif player_guess > secret_number:
        return "high"
    else:
        return "low"

def play_game():
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        guess = get_player_guess()
        result = check_guess(secret_number, guess)

        if result == "correct":
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif result == "high":
            print("Too high! Try again.")
        elif result == "low":
            print("Too low! Try again.")

if __name__ == "__main__":
    play_game()

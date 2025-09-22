from src.GameIO import user_guess
from src.GameIO import target_number


def check_guess() -> str:
    """Check the user's guess against the target number.

    Returns:
        A message indicating whether the guess is too low, too high, or correct.
    """
    user_guess1 = user_guess()
    if user_guess1 < target_number:
        print("Your Number too Low!")
        return check_guess()
    elif user_guess1 > target_number:
        print("Your Number too High!")
        return check_guess()
    else:
        print(f"Congratulations! You've guessed the number {target_number}.")
        again = input("Do you want to play again? (yes/no): ")
        if again.lower() == "yes":
            return check_guess()
        else:
            print("Thank you for playing!")
            return "Game Over"


if __name__ == "__main__":
    check_guess()

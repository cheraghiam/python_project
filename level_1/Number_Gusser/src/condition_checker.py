from src.GameIO import user_guess
from src.GameIO import target_number


def check_guess():
    user_guess1 = user_guess()
    if user_guess1 < target_number:
        print("Your Number too Low!")
        return check_guess()
    elif user_guess1 > target_number:
        print("Your Number too High!")
        return check_guess()
    else:
        return f"Congratulations! You've guessed the number {target_number}."
    

if __name__ == "__main__":
    print(check_guess())

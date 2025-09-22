import random


target_number = random.randint(1, 100)


def user_guess():
    while True:
        input_user = input("Enter Your Guess Number: ")
        try:
            return int(input_user)
        except ValueError:
            print("Your Guess Should be Number")


if __name__ == "__main__":
    print(target_number())
    user_guess = user_guess()
    print(user_guess)

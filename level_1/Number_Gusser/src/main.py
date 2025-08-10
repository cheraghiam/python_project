import random


def main():

    target_number = random.randint(1, 100)

    score = 100

    while True:
        user_guess = input("Enter Your Number: ")
        if user_guess == 'q':
            print("Thanks for join the my game")
            break
        try:
            user_guess = int(user_guess)
            if  user_guess > 100 or user_guess < 1:
                print("Pleas Enter a Number between 1 to 100")
                continue
            else:
                if user_guess < target_number:
                    print("Your Number too Low")
                    score -= 10
                    continue
                elif user_guess > target_number:
                    print("Yourn Number too High")
                    score -= 10
                    continue
                else:
                    print(f"congratulations, your score: {score}")
                    user_countinu = input("Do you like play again:[y,n]: ").lower()
                    if user_countinu == 'y':
                        target_number = random.randint(1, 100)
                        score = 100
                        continue
                    else:
                        print("Good Bye...")
                        break
        except ValueError:
            print("Pleas Enter just Number")
            continue


if __name__ == '__main__':
    main()
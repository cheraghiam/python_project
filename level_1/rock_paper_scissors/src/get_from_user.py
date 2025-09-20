from src.constants import game_items


def get_user_choice():
    input_user = input("Enter your choice  ['rock', 'paper', 'scissors']: ")
    if input_user.lower() in set(game_items):
        return input_user
    else:
        get_user_choice()


if __name__ == "__main__":
    print(get_user_choice())
import random 

from src.constants import game_items
from src.constants import game_items


def get_item_from_computer() -> str :
    """Get a random item from the computer's choices.

    Returns:
       The computer's choice.
    """
    return random.choice(game_items)


def get_user_choice() -> str :
    """Get the user's choice.

    Returns:
        The user's choice.
    """
    input_user = input("Enter your choice  ['rock', 'paper', 'scissors']: ")
    if input_user.lower() in set(game_items):
        return input_user
    else:
        get_user_choice()


if __name__ == "__main__":
    print(get_user_choice())
    print(get_item_from_computer())

import random 

from src.main import game_items


def get_item_from_computer():
    return random.choice(game_items)


if __name__ == "__main__":
    print(get_item_from_computer())
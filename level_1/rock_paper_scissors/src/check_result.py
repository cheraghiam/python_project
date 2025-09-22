from src.constants import winner
from src.GameIO import get_item_from_computer
from src.GameIO import get_user_choice


user_choice = get_user_choice()
pc_choice = get_item_from_computer()


def check_result(user_choice: str, pc_choice: str) -> str:
        """check result for who winner

        Args:
            user_choice: user's choice
            pc_choice: computer's choice

        Returns:
            str: result message
        """
        for choice_win, choice_lost in winner:
                if user_choice == choice_win and pc_choice == choice_lost:
                        return f"You win! {user_choice} beats {pc_choice}"
        return f"You lose! {pc_choice} beats {user_choice}"


if __name__ == "__main__":
        print(check_result(user_choice=user_choice, pc_choice=pc_choice))

game_items = ['rock', 'paper', 'scissors']
winner = [
    ('rock', 'scissors'),
    ('scissors', 'paper'),
    ('paper', 'rock')
]


class RockPaperScissors:
    def check_result(self, item_computer, item_user):
        if item_computer == item_user:
            return "Its a Tie"

        for stage_win in winner:
            if stage_win[0] == item_user and stage_win[1] == item_computer:
                return "you win, Computer loses"
        return "Computer win, you loses"

    def play_game(self, user_choice):
        item_computer = self.get_item_from_computer()
        item_user = self.get_item_from_user(user_choice)
        print(f"item computer is {item_computer}, your choice {item_user}")
        print(self.check_result(item_computer, item_user))
        again_play = input("Do you want to play again? (yes/no): ")
        if again_play.lower() == "yes":
            user_choice = input(f"Enter your choice ({['rock', 'paper', 'scissors']}): ")
            self.play_game(user_choice=user_choice)
        else:
            print("Thank you for playing!")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_choice = input(f"Enter your choice ({['rock', 'paper', 'scissors']}): ")
    rps = RockPaperScissors(user_name)
    rps.play_game(user_choice=user_choice)

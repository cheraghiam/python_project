import random

user_name = input("Enter your name: ")

class rock_paper_scissors:
    
    def __init__(self, name):
        self.game_items = ['rock', 'paper', 'scissors']
        self.name = name
        print(f"hello {self.name}")
    
    def get_item_from_computer(self):
        return random.choice(self.game_items)

    def get_item_from_user(self):
        input_user = input(f"Enter your choice ({self.game_items}): ")
        if input_user.lower() in self.game_items:
            return input_user.lower()
        else:
            print(f"please Enter from {self.game_items}")
            return self.get_item_from_user()

    def check_result(self, item_computer, item_user):
        if item_computer == item_user:
            return "Its a Tie"
        winner = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        for stage_win in winner:
            if stage_win[0] == item_user and stage_win[1] == item_computer:
                return "you win, Computer loses"
        return "Computer win, you loses"

    def play_game(self):
        item_computer = self.get_item_from_computer()
        item_user = self.get_item_from_user()
        print(f"item computer is {item_computer}, your choice {item_user}")
        print(self.check_result(item_computer, item_user))
        again_play = input("Do you want to play again? (yes/no): ")
        if again_play.lower() == "yes":
            self.play_game()
        else:
            print("Thank you for playing!")


if __name__ == "__main__":
    rps = rock_paper_scissors(user_name)
    rps.play_game()
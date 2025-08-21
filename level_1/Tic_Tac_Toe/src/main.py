import random


class Tic_Tac_Toe:
    def __init__(self):
        self.board = [' ' for _ in range(10)]
        print(self.board[0], '\n')
        print(self.board[1], '|', self.board[2], '|', self.board[3])
        print(self.board[4], '|', self.board[5], '|', self.board[6])
        print(self.board[7], '|', self.board[8], '|', self.board[9])

    def select_user(self, num):
        if self.board[num] == ' ':
            self.board[num] = 'X'
            print(self.board[0], '\n')
            print(self.board[1], '|', self.board[2], '|', self.board[3])
            print(self.board[4], '|', self.board[5], '|', self.board[6])
            print(self.board[7], '|', self.board[8], '|', self.board[9])
            self.condition_won()
        

    def select_game(self):
        self.board[random.choice([ind for ind, value in enumerate(self.board) if value == ' ' and ind != 0])] = 'O'
        print(self.board[0], '\n')
        print(self.board[1], '|', self.board[2], '|', self.board[3])
        print(self.board[4], '|', self.board[5], '|', self.board[6])
        print(self.board[7], '|', self.board[8], '|', self.board[9])
        self.condition_won()

    def condition_won(self):
        won_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                    (1, 4, 7), (2, 5, 8), (3, 6, 9),
                    (1, 5, 9), (3, 5, 7)]
        
        for state1, state2, state3 in won_list:
            if self.board[state1] == 'X' and self.board[state2] == 'X' and self.board[state3] == 'X':
                print("Player X wins!")

            elif self.board[state1] == 'O' and self.board[state2] == 'O' and self.board[state3] == 'O':
                print("Player O wins!")



if __name__ == '__main__':
    Tic_Tac_Toe = Tic_Tac_Toe()
    while True:
        number_user = input("Enter your position (1-9): ")
        if number_user.isdigit():
            number_user = int(number_user)
            if 1<= number_user <=9:
                Tic_Tac_Toe.select_user(number_user)
                Tic_Tac_Toe.select_game()
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number.")

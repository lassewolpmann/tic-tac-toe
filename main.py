import os


def clear_screen():
    os_name = os.name
    if os_name == 'nt':
        os.system('cls')

    else:
        os.system('clear')


class TicTacToe:
    def __init__(self):
        self.board = []
        self.current_player = 'X'
        self.is_won = False
        self.winning_player = ''

    def create_board(self):
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append('-')

        print(self.board)

    def play_game(self):
        for i in range(9):
            clear_screen()
            self.print_board()
            if i % 2 == 0:
                print('Player X')
                self.current_player = 'X'

            else:
                print('Player O')
                self.current_player = 'O'

            self.place_mark()
            self.check_win()

            if self.is_won:
                clear_screen()
                print(f'Player {self.winning_player} won!')
                self.print_board()
                break

    def place_mark(self):
        while True:
            spot = input('Place mark (row:place): ')
            row = int(spot.split(':')[0]) - 1
            place = int(spot.split(':')[1]) - 1
            current_mark = self.board[row][place]
            if current_mark == '-':
                self.board[row][place] = self.current_player
                break

            else:
                print('Spot already taken, try again!')

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_win(self):
        def count_marks(mark_list):
            if mark_list.count('X') == 3:
                self.winning_player = 'X'
                self.is_won = True

            elif mark_list.count('O') == 3:
                self.winning_player = 'O'
                self.is_won = True

        # Check row for win
        for row in self.board:
            count_marks(row)

        # Check columns for win
        for column_count in range(3):
            column = []
            for row_count in range(3):
                column.append(self.board[row_count][column_count])

            count_marks(column)

        # Check diagonal for win
        top_left_bottom_right = []
        for spot in range(3):
            top_left_bottom_right.append(self.board[spot][spot])

        count_marks(top_left_bottom_right)

        top_right_bottom_left = []
        for row in range(3):
            for spot in range(2, -1, -1):
                top_right_bottom_left.append(self.board[row][spot])

        count_marks(top_right_bottom_left)


if __name__ == '__main__':
    game = TicTacToe()
    game.create_board()
    game.play_game()

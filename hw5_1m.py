import random

class Minesweeper:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[' ' for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.place_mines()
        self.calculate_adjacent_mines()

    def place_mines(self):
        while len(self.mines) < self.num_mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.mines.add((x, y))

        for (x, y) in self.mines:
            self.board[x][y] = 'M'

    def calculate_adjacent_mines(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 'M':
                    continue
                mine_count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size:
                            if self.board[nx][ny] == 'M':
                                mine_count += 1
                self.board[x][y] = str(mine_count)

    def print_board(self, show_mines=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            if show_mines:
                row = " ".join(self.board[i])
            else:
                row = " ".join(self.revealed[i])
            print(f"{i} {row}")

    def reveal(self, x, y):
        if self.revealed[x][y] != ' ':
            return
        self.revealed[x][y] = self.board[x][y]
        if self.board[x][y] == '0':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.reveal(nx, ny)

    def mark_mine(self, x, y):
        if self.revealed[x][y] == ' ':
            self.revealed[x][y] = 'F'
        elif self.revealed[x][y] == 'F':
            self.revealed[x][y] = ' '

    def check_win(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.revealed[x][y] == ' ' and self.board[x][y] != 'M':
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            action = input("Enter action (r for reveal, m for mark): ")
            x, y = map(int, input("Enter coordinates (row and column): ").split())
            if action == 'r':
                if (x, y) in self.mines:
                    print("You hit a mine! Game over.")
                    self.print_board(show_mines=True)
                    break
                self.reveal(x, y)
            elif action == 'm':
                self.mark_mine(x, y)
            if self.check_win():
                print("Congratulations! You've won.")
                self.print_board(show_mines=True)
                break

# Example of how to start a game
game = Minesweeper(size=5, num_mines=3)
game.play()

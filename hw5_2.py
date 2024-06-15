import random

# Constants
BOARD_LENGTH = 30
PENALTY_PROBABILITY = 0.3

# Function to create the board
def create_board():
    board = {}
    for i in range(1, BOARD_LENGTH + 1):
        if random.random() < PENALTY_PROBABILITY:
            board[i] = 'P'
        else:
            board[i] = '_'
    return board

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to print the board
def print_board(board, player_positions):
    board_representation = []
    for i in range(1, BOARD_LENGTH + 1):
        if i == player_positions['A'] and i == player_positions['B']:
            if board[i] == 'P':
                board_representation.append('x')
            else:
                board_representation.append('X')
        elif i == player_positions['A']:
            if board[i] == 'P':
                board_representation.append('a')
            else:
                board_representation.append('A')
        elif i == player_positions['B']:
            if board[i] == 'P':
                board_representation.append('b')
            else:
                board_representation.append('B')
        else:
            board_representation.append('_')
    print(" ".join(board_representation))

# Function to check if the game is over
def check_game_over(player_positions):
    return player_positions['A'] >= BOARD_LENGTH or player_positions['B'] >= BOARD_LENGTH

# Main function to play the game
def play_game():
    # Create the board
    board = create_board()
    
    # Initialize player positions and turn penalties
    player_positions = {'A': 1, 'B': 1}
    player_penalties = {'A': False, 'B': False}
    
    # Game loop
    while not check_game_over(player_positions):
        for player in ['A', 'B']:
            if player_penalties[player]:
                player_penalties[player] = False
                continue
            
            dice_roll = roll_dice()
            player_positions[player] += dice_roll
            
            if player_positions[player] >= BOARD_LENGTH:
                player_positions[player] = BOARD_LENGTH
                if check_game_over(player_positions):
                    break
            
            if board[player_positions[player]] == 'P':
                player_penalties[player] = True
        
        print_board(board, player_positions)
        
    # Final positions and board
    print("Game Over!")
    if player_positions['A'] >= BOARD_LENGTH and player_positions['B'] >= BOARD_LENGTH:
        print("Both players win!")
    elif player_positions['A'] >= BOARD_LENGTH:
        print("Player A wins!")
    elif player_positions['B'] >= BOARD_LENGTH:
        print("Player B wins!")
    
    # Print the board with penalty squares revealed
    final_board = []
    for i in range(1, BOARD_LENGTH + 1):
        if board[i] == 'P':
            final_board.append('P')
        else:
            final_board.append('_')
    print(" ".join(final_board))

# Run the game
play_game()

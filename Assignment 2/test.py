def create_board(NUM_ROWS,NUM_COLS):
    """
    Input: Input the number of rows and cols for the board/
    Output: A table that represents the 5x10 board with all the cells filled with a hyphen
     
    Note: For basic game you only need 50 square board.
    For example: 
    >>> board=create_board(NUM_ROWS,NUM_COLS)  #with 5 rows and 10 cols for basic implementation
    >>> board
    ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '']]
    """ 
    return [['' for i in range(NUM_COLS)] for j in range(NUM_ROWS)]

def print_board(board):
    """
    Input: The current status of the board 
    Output: Prints the current board to the screen

    For example: 
    >>> board = create_board(NUM_ROWS,NUM_COLS)
    >>> print_board(board)
   Snakes and Ladders Board:
   0   1   2   3   4   5   6   7   8   9
   ----------------------------------------
   0|   |   |   |   |   |   |   |   |   |   |
   -----------------------------------
   1|   |   |   |   |   |   |   |   |   |   |
   -----------------------------------
   2|   |   |   |   |   |   |   |   |   |   |
   -----------------------------------
   3|   |   |   |   |   |   |   |   |   |   |
   -----------------------------------
   4|   |   |   |   |   |   |   |   |   |   |
   -----------------------------------
   """
    print("Snakes and Ladders Board:")
    print("   ".join(str(i) for i in range(len(board[0]))))
    print("--" * (len(board[0]) * 2))

    for i in range(len(board)):
        # Concatenate the row number and the row content, then print
        row_content = " | ".join(board[i])
        print(str(i) + "| " + row_content + " |")
        print("--" * (len(board[0]) * 2))
    
    
    
def initialise_board(board, NUM_SQUARES):
    """
    Initialize the board with numbers from 1 to NUM_SQUARES in a zig-zag pattern.

    Parameters:
    board (list of lists): The game board to be initialized.
    NUM_SQUARES (int): The total number of squares on the board.
    """
    num = NUM_SQUARES
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i % 2 == 0:
                board[i][j] = str(num)
            else:
                board[i][len(board[i]) - j - 1] = str(num)
            num -= 1
    return board

#Task 4
import random
available_nodes_snake = []
def place_snakes(board,NUM_SQUARES,NUM_SNAKES):
    """
    Input: The current status of the board,number of sqaures and number of snakes.
    Output: A table that represents the 5x10 board with snakes placed at random places
    placed on the board in specific places.
    For example:
    >>> board = place_snakes(board,NUM_SQUARES,NUM_SNAKES)
    >>> print_board(board)
    Snakes and Ladders Board:
        0   1   2   3   4   5   6   7   8   9
    ----------------------------------------
    0| 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41S |
    -----------------------------------
    1| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39S | 40 |
    -----------------------------------
    2| 30 | 29 | 28S | 27 | 26 | 25 | 24 | 23 | 22 | 21 |
    -----------------------------------
    3| 11 | 12s | 13 | 14 | 15 | 16s | 17 | 18 | 19 | 20 |
    -----------------------------------
    4| 10s | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    -----------------------------------
    >>> 
    """
    available_squares = [(i, j) for i in range(NUM_ROWS) for j in range(NUM_COLS) if board[i][j].isdigit()]
    coordinates = random.sample(available_squares, NUM_SNAKES*2)
    coordinates.sort(reverse=False)
    for i in range(len(coordinates)//2):
        nested_list = []
        nested_list.append(coordinates[i])
        nested_list.append(coordinates[i+len(coordinates)//2])
        available_nodes_snake.append(nested_list)
    for i in range(len(available_nodes_snake)):
        board[available_nodes_snake[i][0][0]][available_nodes_snake[i][0][1]] += "S"
        board[available_nodes_snake[i][1][0]][available_nodes_snake[i][1][1]] += "s"
    return available_nodes_snake
    
available_nodes_ladder = []
def place_ladders(board,NUM_SQUARES,NUM_LADDERS):
    """
    Input: The current status of the board, number of sqaures and number of
    Output: A table that represents the 5x10 board with ladders placed randomly
    placed on the board in specific places.
    For example:
    >>> board = place_ladders(board,NUM_SQUARES,NUM_LADDERS)
    >>> print_board(board)
    Snakes and Ladders Board:
        0   1   2   3   4   5   6   7   8   9
    ----------------------------------------
    0| 50L | 49 | 48 | 47 | 46 | 45L | 44 | 43 | 42l | 41S |
    -----------------------------------
    1| 31 | 32 | 33 | 34 | 35 | 36L | 37 | 38 | 39S | 40 |
    -----------------------------------
    2| 30l | 29 | 28S | 27 | 26 | 25 | 24 | 23 | 22 | 21 |
    -----------------------------------
    3| 11 | 12s | 13 | 14 | 15 | 16s | 17 | 18 | 19 | 20 |
    -----------------------------------
    4| 10s | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    -----------------------------------
    """
    available_squares = [(i, j) for i in range(NUM_ROWS) for j in range(NUM_COLS) if board[i][j].isdigit()]
    coordinates = random.sample(available_squares, NUM_SNAKES*2)
    coordinates.sort(reverse=False)
    for i in range(len(coordinates)//2):
        nested_list = []
        nested_list.append(coordinates[i])
        nested_list.append(coordinates[i+len(coordinates)//2])
        available_nodes_ladder.append(nested_list)
    for i in range(len(available_nodes_ladder)):
        board[available_nodes_ladder[i][0][0]][available_nodes_ladder[i][0][1]] += "L"
        board[available_nodes_ladder[i][1][0]][available_nodes_ladder[i][1][1]] += "l"
    return available_nodes_ladder

# Task 5
def roll_dice():
    dice = random.randint(1, 6)
    return dice

def current_position():
    for i in range(row):
        for j in range(col):    
            if P1 in str(board[i][j]):
                position = board[i][j]

def update_player_position(player, position, board):
    """
    Input: The current status of the board, current player, current position of the player
    Output: A table that represents the 5x10 board with snakes and ladders
    placed on the board in specific places and both players.
    For example:
    >>> board = update_player_position(player, position, board)
    >>> print_board(board)
    Snakes and Ladders Board:
        0   1   2   3   4   5   6   7   8   9
    ----------------------------------------
    0| 50L | 49 | 48 | 47 | 46 | 45L | 44 | 43 | 42l | 41S |
    -----------------------------------
    1| 31 | 32 | 33 | 34 | 35 | 36L | 37 | 38 | 39S | 40 |
    -----------------------------------
    2| 30l | 29 | 28S | 27 | 26 | 25 | 24 | 23 | 22 | 21 |
    -----------------------------------
    3| 11 | 12s | 13 | 14 | 15 | 16s | 17 | 18 | 19 | 20 |
    -----------------------------------
    4| 10s | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1P1AI |
    -----
    """
    NUM_ROWS, NUM_COLS = len(board), len(board[0])
    dice_roll = roll_dice() 

    # Calculate the new position
    new_position = position + dice_roll
    if new_position > NUM_ROWS * NUM_COLS:
        new_position = NUM_ROWS * NUM_COLS  
        
    for i in range(len(board)):
        for j in range(len(board[i])):
            if str(new_position) in board[i][j]:
                row, col = i, j
    
    cell_content = board[row][col]
    # Check for snakes or ladders at the new position
    for i in range(len(available_nodes_snake)):
        if row == available_nodes_snake[i][0][0] and col == available_nodes_snake[i][0][1]:
            row = available_nodes_snake[i][1][0] 
            col = available_nodes_snake[i][1][1]
            
    for i in range(len(available_nodes_ladder)):
        if row == available_nodes_ladder[i][1][0] and col == available_nodes_ladder[i][1][1]:
            row = available_nodes_ladder[i][0][0] 
            col = available_nodes_ladder[i][0][1]
            
    # Update the board with the player's new position
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if player in board[i][j]:
                board[i][j] = board[i][j].replace(player, '')

    # Add player to new position
    board[row][col] += player
    return board

#Task 6
def check_game_over(currentPlayer,board,NUM_SQUARES):
    """
    Input: The current status of the board, current player and number of sqaures
    Output: A table that represents the 5x10 board with snakes and ladders
    placed on the board in specific places and both players updated position.
    For example:After player rolled a six and AI rolled a three on the dice.
    >>> board = update_player_position(player,position,board)
    >>> print_board(board)
    Snakes and Ladders Board:
      0   1   2   3   4   5   6   7   8   9
    ----------------------------------------
    0| 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 |
    -----------------------------------
    1| 31L | 32 | 33 | 34 | 35 | 36 | 37L | 38 | 39L | 40 |
    -----------------------------------
    2| 30 | 29 | 28S | 27 | 26 | 25 | 24s | 23 | 22 | 21S |
    -----------------------------------
    3| 11 | 12l | 13s | 14 | 15 | 16 | 17 | 18l | 19 | 20s |
    -----------------------------------
    4| 10 | 9 | 8 | 7P1 | 6 | 5 | 4AI | 3 | 2 | 1 |
    ----------------------------------- 
    """
    player1 = "P1"
    player2 = "P2"
    ai = "AI"
    
    print(board)
    update_player_position(player1, )

NUM_ROWS = 5
NUM_COLS = 10
NUM_SQUARES = NUM_ROWS * NUM_COLS
NUM_SNAKES = 5
NUM_LADDERS = NUM_SNAKES

board = create_board(NUM_ROWS, NUM_COLS)
initialise_board(board, NUM_SQUARES)
place_snakes(board, NUM_SQUARES, NUM_SNAKES)
place_ladders(board, NUM_SQUARES, NUM_LADDERS)
update_player_position("P1", 1, board)
print_board(board)    
    
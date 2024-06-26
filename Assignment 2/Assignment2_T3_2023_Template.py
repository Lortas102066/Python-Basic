#imports 
import random
# gloabl declarations as needed
# Task 1
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
    return [['' for i in range(NUM_COLS)] for j in range(NUM_ROWS)] #Create an empty nested list for numbers
    
# Task 2
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

    #This makes the board look like a table
    for i in range(len(board)):
        row_content = " | ".join(board[i])
        print(str(i) + "| " + row_content + " |")
        print("--" * (len(board[0]) * 2))

#Task 3
def initialise_board(board,NUM_SQUARES):
    """
    Input: The current status of the board and number of squares.
    Output: A table that represents the 5x10 board with values placed in squares showing a zig zag pattern.
    For example: 
    >>> board = initialise_board(board,NUM_SQUARES)
    >>> print_board(board)
    Snakes and Ladders Board:
        0   1   2   3   4   5   6   7   8   9
    ----------------------------------------
    0| 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 |
    -----------------------------------
    1| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
    -----------------------------------
    2| 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 |
    -----------------------------------
    3| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
    -----------------------------------
    4| 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    -----------------------------------
    """
    num = NUM_SQUARES
    #Input numbers into the nested list
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i % 2 == 0:
                board[i][j] = str(num)
            else:
                board[i][len(board[i]) - j - 1] = str(num)
            num -= 1
    return board
      
        
#Task 4
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
    # Create a list of available squares
    available_squares = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j].isdigit() and i != 4 and j != 9]
    # Create a list of random coordinates for snakes
    coordinates = random.sample(available_squares, NUM_SNAKES*2)
    # Sort the random coordinates
    coordinates.sort(reverse=False)
    
    #Stick the snake head and tail together
    for i in range(len(coordinates)//2):
        nested_list = []
        nested_list.append(coordinates[i])
        nested_list.append(coordinates[i+len(coordinates)//2])
        available_nodes_snake.append(nested_list)
    #Place the snake head and tail on the board
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
    # Check the avaible nodes for ladder
    available_squares = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j].isdigit() ]
    # Get samples from the available nodes
    coordinates = random.sample(available_squares, NUM_LADDERS*2)
    # Sort the coordinates
    coordinates.sort(reverse=False)
    #Stick the ladder head and tail together
    for i in range(len(coordinates)//2):
        nested_list = []
        nested_list.append(coordinates[i])
        nested_list.append(coordinates[i+len(coordinates)//2])
        available_nodes_ladder.append(nested_list)
    #Place the snake head and tail on the board
    for i in range(len(available_nodes_ladder)):
        board[available_nodes_ladder[i][0][0]][available_nodes_ladder[i][0][1]] += "L"
        board[available_nodes_ladder[i][1][0]][available_nodes_ladder[i][1][1]] += "l"
    return available_nodes_ladder


# Task 5
def update_player_position(player,position,board):
    """
    Input: The current status of the board, current player, current position of the player
    Output: A table that represents the 5x10 board with snakes and ladders
    placed on the board in specific places and both players.
    For example:
    >>> board = update_player_position(player,position,board)
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
    ----------------------------------- 
    """
    NUM_ROWS, NUM_COLS = len(board), len(board[0])
    dice_roll = roll_dice() 

    # Calculate the new position
    position = position + dice_roll
    if position > NUM_ROWS * NUM_COLS:
        position = NUM_ROWS * NUM_COLS  
        
    for i in range(len(board)):
        for j in range(len(board[i])):
            if str(position) in board[i][j]:
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
    numbers = ""
    for char in board[row][col]:
        if char.isdigit():
            numbers += char
    #make sure to use global player variable
    global players
    players[player_turn]["position"] = int(numbers)
    numbers = ""
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
    global players
    # If players position is equal to the number of squares, the game is over
    if players[player_turn]["position"] == NUM_SQUARES:
        return True
    else: 
        return False
         
# # Supporting function to swap players
def swap_players(currentPlayer):
    global player_turn
    global players
    # Different cases for different number of players
    #Condition for 1 or 2 players
    if len(players) == 2:
        if currentPlayer == 0:
            currentPlayer = 1
            player_turn = currentPlayer
        else: 
            currentPlayer = 0
            player_turn = currentPlayer
    #Condition for 3 players
    elif len(players) == 3:
        if currentPlayer == 0:
            currentPlayer = 1
            player_turn = currentPlayer
        elif currentPlayer == 1:
            currentPlayer = 2
            player_turn = currentPlayer
        else:
            currentPlayer = 0
            player_turn = currentPlayer
    #Condition for 4 players
    elif len(players) == 4:
        if currentPlayer == 0:
            currentPlayer = 1
            player_turn = currentPlayer
        elif currentPlayer == 1:
            currentPlayer = 2
            player_turn = currentPlayer
        elif currentPlayer == 2:
            currentPlayer = 3
            player_turn = currentPlayer
        else:
            currentPlayer = 0
            player_turn = currentPlayer
    

# Supporting function to roll the dice      
def roll_dice():
    dice = random.randint(1, 6)
    return dice

current_position = 1
players = []
player_turn = 0

#play snake and ladder
def play_game():
    """
    Input: The game start
    Output: A table that represents the 5x10 board with snakes and ladders
    placed on the board in specific places and both players updated position.
    For example:Enter the number of squares you want on the board: 50
    Enter the number of rows you want the board to have: 5
    Enter the number of cols you want the board to have: 10
    Enter the number of snakes you want the board to have: 3
    Enter the number of ladders you want the board to have: 3
    Enter the number of players you want to play the game with: 2
    Enter1players name such as P1,P2 for player one, two and so on and AI for computer: P1
    Enter2players name such as P1,P2 for player one, two and so on and AI for computer: AI
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
    4| 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1P1AI |
    -----------------------------------
    """
    #ask for information of the table
    NUM_SQUARES = int(input("Number of squares you want on the board: "))
    NUM_ROWS = int(input('Enter the number of rows you want the board to have: '))
    NUM_COLS = int(input('Enter the number of cols you want the board to have: '))
    NUM_SNAKES = int(input('Enter the number of snakes you want the board to have: '))
    NUM_LADDERS = int(input('Enter the number of ladders you want the board to have: '))
    number_of_players = int(input('Enter the number of players you want to play the game with: '))
    if number_of_players == 1: 
        player1 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player1 = {"name": player1, "position": 1}
        player2 = {"name": "AI", "position": 1}
    elif number_of_players == 2:
        player1 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player2 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player1 = {"name": player1, "position": 1}
        player2 = {"name": player2, "position": 1}
    elif number_of_players == 3:
        player1 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player2 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player3 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player1 = {"name": player1, "position": 1}
        player2 = {"name": player2, "position": 1}
        player3 = {"name": player3, "position": 1}
    elif number_of_players == 4:
        player1 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player2 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player3 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player4 = input("Enter1players name such as P1,P2 for player one, two and so on and AI for computer: ")
        player1 = {"name": player1, "position": 1}
        player2 = {"name": player2, "position": 1}
        player3 = {"name": player4, "position": 1}

    players.append(player1)
    players.append(player2)
    
    board = create_board(NUM_ROWS, NUM_COLS)
    initialise_board(board, NUM_SQUARES)
    place_snakes(board, NUM_SQUARES, NUM_SNAKES)
    place_ladders(board, NUM_SQUARES, NUM_LADDERS)
    #initialise the players position
    board[4][9] += player1["name"]
    board[4][9] += player2["name"]
    print_board(board)
        
    continue_playing = str(input("Enter r to roll the dice or q to quit the game: "))
    #Continues while the player is typing "r" and the player's position is less than the number of squares
    while continue_playing == "r" and player1["position"] < NUM_SQUARES and player2["position"] < NUM_SQUARES:
        print(f"{players[player_turn]['name']} is playing...")
        #Updating the player position
        update_player_position(players[player_turn]["name"], players[player_turn]["position"], board)
        #Display the position after the player rolled the dice
        print_board(board)
        check_game_over(players[player_turn]["name"],board,NUM_SQUARES)
        if check_game_over(players[player_turn]["name"],board,NUM_SQUARES) == True:
            print(f"{players[player_turn]['name']} is the winner!")
            ask_play_again = input('Do you want to play again? (y/n): ')
            if ask_play_again == 'y':
                play_game()
            else:
                print("Thank you for playing the game!")
                break
        else:
            swap_players(player_turn)
            continue_playing = str(input("Enter r to roll the dice or q to quit the game: "))
    if continue_playing == "q":
        print("You chose to leave the game! Thank you for playing the game!")
    
    
    
# Start the game
play_game()

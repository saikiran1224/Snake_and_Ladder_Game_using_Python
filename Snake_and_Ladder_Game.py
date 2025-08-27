import random as rd 

# Creating a dice method having 1 to 6 values - when function called dice gets rolled programatically
def roll_dice(): return (rd.randrange(1,6))

def play_player_1_game():

    # first player rolling dice 
    outcome = roll_dice() 

    # Adding them into their dice history
    player_1_dice_history.append(outcome)

    # For first roll, directly adding into position history list
    if len(player_1_pos_history) == 0: 
        player_1_pos_history.append(outcome)

    else: 
        # Take last position value and add it with the current outcome of the dice and add in the position list
        previous_pos_value = player_1_pos_history[-1]

        # Checking if the outcome + previous_pos_value is not exceeding the grid_size**2 final value 
        next_pos_value = previous_pos_value + outcome

        if next_pos_value > grid_size**2: 
            # preserving the last position and adding again in the position list
            player_1_pos_history.append(previous_pos_value)
        else: 
            # if the sum is not reaching the final position value then we are appending the sum of the outcome and the previous position value 
            player_1_pos_history.append(next_pos_value)

def play_player_2_game():

    # first player rolling dice 
    outcome = roll_dice() 

    # Adding them into their dice history
    player_2_dice_history.append(outcome)

    # For first roll, directly adding into position history list
    if len(player_2_pos_history) == 0: 
        player_2_pos_history.append(outcome)

    else: 
        # Take last position value and add it with the current outcome of the dice and add in the position list
        previous_pos_value = player_2_pos_history[-1]

        # Checking if the outcome + previous_pos_value is not exceeding the grid_size**2 final value 
        next_pos_value = previous_pos_value + outcome

        if next_pos_value > grid_size**2: 
            # preserving the last position and adding again in the position list
            player_2_pos_history.append(previous_pos_value)
        else: 
            # if the sum is not reaching the final position value then we are appending the sum of the outcome and the previous position value 
            player_2_pos_history.append(next_pos_value)

def play_player_3_game():

    # first player rolling dice 
    outcome = roll_dice() 

    # Adding them into their dice history
    player_3_dice_history.append(outcome)

    # For first roll, directly adding into position history list
    if len(player_3_pos_history) == 0: 
        player_3_pos_history.append(outcome)

    else: 
        # Take last position value and add it with the current outcome of the dice and add in the position list
        previous_pos_value = player_3_pos_history[-1]

        # Checking if the outcome + previous_pos_value is not exceeding the grid_size**2 final value 
        next_pos_value = previous_pos_value + outcome

        if next_pos_value > grid_size**2: 
            # preserving the last position and adding again in the position list
            player_3_pos_history.append(previous_pos_value)
        else: 
            # if the sum is not reaching the final position value then we are appending the sum of the outcome and the previous position value 
            player_3_pos_history.append(next_pos_value)

def play_player_4_game():

    # first player rolling dice 
    outcome = roll_dice() 

    # Adding them into their dice history
    player_4_dice_history.append(outcome)

    # For first roll, directly adding into position history list
    if len(player_4_pos_history) == 0: 
        player_4_pos_history.append(outcome)

    else: 
        # Take last position value and add it with the current outcome of the dice and add in the position list
        previous_pos_value = player_4_pos_history[-1]

        # Checking if the outcome + previous_pos_value is not exceeding the grid_size**2 final value 
        next_pos_value = previous_pos_value + outcome

        if next_pos_value > grid_size**2: 
            # preserving the last position and adding again in the position list
            player_4_pos_history.append(previous_pos_value)
        else: 
            # if the sum is not reaching the final position value then we are appending the sum of the outcome and the previous position value 
            player_4_pos_history.append(next_pos_value)

# Taking grid size as input from user 
grid_size = int(input("Please enter your grid size (x * x) in number\nE.g, Enter 4 if you need 4*4 grid size: "))

# Developing the game 
# ===================

# Preparing the game board - developing n*n matrix and initializing them with values sequentially from 1 to square(grid_size)
final_value = grid_size ** 2 
snake_board = []

# preparing a row with grid_len values and populating them sequentially starting from 1 
initial_num = 1
for _ in range(grid_size):
    row = [(initial_num+num) for num in range(0, grid_size)]
    initial_num = (row[-1]+1)

    # appending the row to snake board
    snake_board.append(row)

print("Snake board:\n")
# Printing the snake board 
for row in snake_board:
    print(row)
print("\n")

# Creating 4 players with the dice roll and position history 
player_1_dice_history, player_1_pos_history = [], []
player_2_dice_history, player_2_pos_history = [], []
player_3_dice_history, player_3_pos_history = [], []
player_4_dice_history, player_4_pos_history = [], []

# Run the while loop until any of the player pos_history list does not contain the grid_size**2 value
while True: 

    final_value = grid_size**2 

    if (final_value not in player_1_pos_history) and (final_value not in player_2_pos_history) and (final_value not in player_3_pos_history) and (final_value not in player_4_pos_history): 
        play_player_1_game()
    elif final_value in player_1_pos_history: 

        print("Player 1 won with Dice history: ",player_1_dice_history, "Position history:", player_1_pos_history)

        print("============================")
        print("Other players - 2, 3 and 4 Dice history:")
        print(player_2_dice_history, player_3_dice_history, player_4_dice_history, sep=" --- ")
        print("\n")
        print("Other players - 2,3 and 4 position history")
        print(player_2_pos_history, player_3_pos_history, player_4_pos_history, sep=" --- ")
        break

    if (final_value not in player_1_pos_history) and (final_value not in player_2_pos_history) and (final_value not in player_3_pos_history) and (final_value not in player_4_pos_history): 
        play_player_2_game()

    elif final_value in player_2_pos_history: 
        print("Player 2 won with Dice history: ",player_2_dice_history, "Position history:", player_2_pos_history)

        print("============================")
        print("Other players - 1, 3 and 4 Dice history:")
        print(player_1_dice_history, player_3_dice_history, player_4_dice_history, sep=" --- ")
        print("\n")
        print("Other players - 1,3 and 4 position history")
        print(player_1_pos_history, player_3_pos_history, player_4_pos_history, sep=" --- ")
        break

    if (final_value not in player_1_pos_history) and (final_value not in player_2_pos_history) and (final_value not in player_3_pos_history) and (final_value not in player_4_pos_history): 
        play_player_3_game()

    elif final_value in player_3_pos_history: 
        print("Player 3 won with Dice history: ",player_3_dice_history, "Position history:", player_3_pos_history)

        print("============================")
        print("Other players - 1, 2 and 4 Dice history:")
        print(player_1_dice_history, player_2_dice_history, player_4_dice_history, sep=" --- ")
        print("\n")
        print("Other players - 1, 2 and 4 position history")
        print(player_1_pos_history, player_2_pos_history, player_4_pos_history, sep=" --- ")
        break

    if (final_value not in player_1_pos_history) and (final_value not in player_2_pos_history) and (final_value not in player_3_pos_history) and (final_value not in player_4_pos_history): 
        play_player_4_game()
        
    elif final_value in player_4_pos_history: 
        print("Player 4 won with Dice history: ",player_4_dice_history, "Position history:", player_4_pos_history)

        print("============================")
        print("Other players - 1, 2 and 3 Dice history:")
        print(player_1_dice_history, player_2_dice_history, player_3_dice_history, sep=" --- ")
        print("\n")
        print("Other players - 1, 2 and 3 position history")
        print(player_1_pos_history, player_2_pos_history, player_3_pos_history, sep=" --- ")
        break

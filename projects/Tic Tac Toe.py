import random

def display_board(board):
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("———————————")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("———————————")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def player_decision():
    marker = input("Player 1, do you want to be X or O? ").upper()
    while marker != "X" and marker != "O":
        marker = input("Please pick X or O? ").upper()
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True

def next_position(board):
    while True:
        try:
            position = int(input("Pick your next position (1-9): "))
            if position in [1,2,3,4,5,6,7,8,9] and space_check(board, position):
                return position
            else:
                print("You must enter a position between 1-9 that's available.")
                print()
        except ValueError:
            print("Stop being silly.")
            print()

def replay():
    answer = input("Do you want to play again? Enter Yes or No: ").lower()
    while answer != "yes" and answer != "no":
        answer = input("Please enter Yes or No: ").lower()
    if answer == "yes":
        print()
        return True
    else:
        return False

print()
print("Welcome to Tic Tac Toe!")
print()

while True:
    the_board = [" "," "," "," "," "," "," "," "," "," "]
    player1_marker, player2_marker = player_decision()
    print()
    turn = choose_first()
    print(f"It has been decided that {turn} will go first.")
    start_game = input("Start game? Enter Yes or No: ").lower()
    while start_game != "yes" and start_game != "no":
        start_game = input("Please enter Yes or No: ").lower()
    if start_game == "yes":
        game_on = True
    else:
        print()
        print("Another time then.")
        game_on = False
        break
    while game_on:
        if turn == "Player 1":
            print()
            display_board(the_board)
            print()
            print("Player 1, it's your turn.")
            position = next_position(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                print()
                display_board(the_board)
                print()
                print("PLAYER 1 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    print()
                    display_board(the_board)
                    print("THIS GAME IS A TIE!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            print()
            display_board(the_board)
            print()
            print("Player 2, it's your turn.")
            position = next_position(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                print()
                display_board(the_board)
                print()
                print("PLAYER 2 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    print()
                    display_board(the_board)
                    print()
                    print("THIS GAME IS A TIE!")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        print()
        print("Bye, thanks for playing.")
        break
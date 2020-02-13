import random

game_input = ["Null",'x','o','x','o','x','o','x','o','x']

def board(game_input):
    print(game_input[7] + '|' + game_input[8] + '|' + game_input[9])
    print('-----')
    print(game_input[4] + '|' + game_input[5] + '|' + game_input[6])
    print('-----')
    print(game_input[1] + '|' + game_input[2] + '|' + game_input[3])

#board(input_game)
def player_input():
    marker=''
    while marker!='x' and marker!='o':
        marker = input('Player1: Please choose your marker: ')
        if marker=='x':
            return ('x','o')
        elif marker=='o':
            return ('o','x')

#player_1,player_2 = player_input()
#print(player_1 + ' is player 1 symbol')
#print(player_2 + ' is player 2 symbol')

def put_marker(game_input,marker,position):
    game_input[position] = marker

def win(game_input,marker):
    return ((game_input[1] == game_input[2] == game_input[3] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[7] == game_input[5] == game_input[3] == marker) or
            (game_input[1] == game_input[5] == game_input[9] == marker) or
            (game_input[1] == game_input[4] == game_input[7] == marker) or
            (game_input[2] == game_input[5] == game_input[8] == marker) or
            (game_input[3] == game_input[6] == game_input[9] == marker))

def chose_player():
    player = random.randint(1,2)
    if player == 1:
        return 'player 1'
    else:
        return 'player 2'

def space(game_input,position):
    return game_input[position] == ' '

def full_board_check(game_input):
    for i in range(1,10):
        if space(game_input,i):
            return False
    return True


def player_choice(game_input):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
        position = int(input('Please choose your position(1-9) on NumPad: '))
    return position

def play_again():
    choice = input('Would you like to play again [y/n]: ')
    return choice == 'y'


while True:

    the_board = [' ']*10
    player_1, player_2 = player_input()
    print(player_1 + ' is player 1 symbol')
    print(player_2 + ' is player 2 symbol')

    turn = chose_player()
    print(turn + ' will play first')

    play_game = input('Ready to play[y/n]: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player_1':
            board(the_board)
            position = player_choice(the_board)

            put_marker(the_board,player_1,position)

            if win(the_board,player_1):
                board(the_board)
                print(' ----------PLAYER 1 HAS WON , HURRAAAH! -----------')
                game_on = False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('GAME TIE')
                    game_on = False
                else:
                    turn = 'player_2'
        else:
            board(the_board)
            position = player_choice(the_board)

            put_marker(the_board, player_2, position)

            if win(the_board, player_2):
                board(the_board)
                print(' ---------- PLAYER 2 HAS WON , HURRAAAH! -----------')
                game_on = False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('----------- GAME TIE -----------')
                    game_on = False
                else:
                    turn = 'player_1'

    if not play_again():
        break


import random

game_tools = ['schere', 'stein', 'papier', 'echse', 'spock']
input_check = False


def tool_to_number(name):
    if name == 'stein':
        number = 0
    elif name == 'spock':
        number = 1
    elif name == 'papier':
        number = 2
    elif name == 'echse':
        number = 3
    elif name == 'schere':
        number = 4
    return number


def checks_input(user_input):
    return game_tools.__contains__(user_input)


def checks_winner(user_input, computer_input):
    difference = (tool_to_number(user_input) - tool_to_number(computer_input)) % 5
    if difference == 0:
        print('Unentschieden')
    if difference == 1:
        print('Gewonnen')
    if difference == 2:
        print('Gewonnen')
    if difference == 3:
        print('Verloren')
    if difference == 4:
        print('Verloren')


while input_check is False:
    print('Bitte Wählen Sie zwischen Schere, Stein, Papier, Echse, Spock')
    player_input = input('Deine wahl: ').lower()
    input_check = checks_input(player_input)
    random.shuffle(game_tools)

print('Computerwahl = '+game_tools[0])
checks_winner(player_input, game_tools[0])
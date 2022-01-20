import random
import dbManager
import window

game_tools = ['schere', 'stein', 'papier', 'echse', 'spock']
input_check = False
ok = False

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
    elif name == 'abbruch':
        ok = True
    return number


def checks_input(user_input):
    return game_tools.__contains__(user_input)


# Stein : 0, Spock = 1, Papier = 2, Echse = 3, Schere = 4

def checks_winner(user_input, computer_input):
    difference = (tool_to_number(user_input) - tool_to_number(computer_input)) % 5
    if difference == 0:
        dbManager.insert_stats(2, tool_to_number(user_input))
        return print('Unentschieden')
    if difference == 1:
        dbManager.insert_stats(1, tool_to_number(user_input))
        return print('Gewonnen')
    if difference == 2:
        dbManager.insert_stats(1, tool_to_number(user_input))
        return print('Gewonnen')
    if difference == 3:
        dbManager.insert_stats(0, tool_to_number(user_input))
        return print('Verloren')
    if difference == 4:
        dbManager.insert_stats(0, tool_to_number(user_input))
        return print('Verloren')





if __name__ == "__main__":
    dbManager.create_databse()
    dbManager.create_table()
   # while input_check is False:
    #    print('Bitte Wählen Sie zwischen Schere, Stein, Papier, Echse, Spock')
     #   player_input = input('Deine wahl: ').lower()
      #  input_check = checks_input(player_input)



    player_input = window.choosing_window()
    random.shuffle(game_tools)
    print('Computerwahl = ' + game_tools[0])
    checks_winner(player_input, game_tools[0])

    dbManager.get_game_stats()
    dbManager.count_player_moves()

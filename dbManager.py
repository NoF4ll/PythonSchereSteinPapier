import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="bichl601", database="scheresteinpapierstats")
cursor = mydb.cursor()


def create_databse():
    cursor.execute("create database if not exists SchereSteinPapierStats")


def create_table():
    #cursor.execute("use scheresteinpapierstats")
    sql = "create table if not exists stats (GameResult varchar(255), Move varchar(255))"
    cursor.execute(sql)


def insert_stats(game_result, move):
    #cursor.execute("use scheresteinpapierstats")
    sql = "insert into stats (GameResult, Move) values(%s, %s)"
    val = (game_result, move)
    cursor.execute(sql, val)
    mydb.commit()


def get_game_stats():
    sql_wins = "Select count('GameResult') from stats where gameResult = 'gewonnen';"
    sql_losses = "Select count('GameResult') from stats where gameResult = 'verloren';"

    cursor.execute(sql_wins)
    wins = cursor.fetchall()

    cursor.execute(sql_losses)
    losses = cursor.fetchall()

    print("Gewonnen: "+str(wins[0][0])+" Verloren: "+str(losses[0][0]))


def count_player_moves():
    count_scissor = "Select count('move') from stats where move = 'Schere';"
    count_rock = "Select count('move') from stats where move = 'Stein';"
    count_paper = "Select count('move') from stats where move = 'Papier';"
    count_lizard = "Select count('move') from stats where move = 'Echse';"
    count_spock = "Select count('move') from stats where move = 'Spock';"
    count_games_played = "Select count('move') from stats;"

    cursor.execute(count_scissor)
    number_scissor = cursor.fetchall()

    cursor.execute(count_rock)
    number_rock = cursor.fetchall()

    cursor.execute(count_paper)
    number_paper = cursor.fetchall()

    cursor.execute(count_spock)
    number_spock = cursor.fetchall()

    cursor.execute(count_lizard)
    number_lizard = cursor.fetchall()

    cursor.execute(count_games_played)
    games_played = cursor.fetchall()

    print("Anzahl der gewählten Spielfiguren:")
    print("Schere: "+str(number_scissor[0][0])+" Prozentanteil: "+str(round((number_scissor[0][0]/games_played[0][0])*100))+"%" +
          "\n Stein: "+str(number_rock[0][0]) +" Prozentanteil: "+str(round((number_rock[0][0]/games_played[0][0])*100))+"%" +
          "\n Papier: "+str(number_paper[0][0]) +" Prozentanteil: "+str(round((number_paper[0][0]/games_played[0][0])*100))+"%" +
          "\n Echse: "+str(number_lizard[0][0]) +" Prozentanteil: "+str(round((number_lizard[0][0]/games_played[0][0])*100))+"%" +
          "\n Spock: "+str(number_spock[0][0]) +" Prozentanteil: "+str(round((number_spock[0][0]/games_played[0][0])*100))+"%")
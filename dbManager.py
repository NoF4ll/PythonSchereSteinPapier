import mysql.connector
import apiHandler

mydb = mysql.connector.connect(host="localhost", user="root", password="hurensohn", database="scheresteinpapierstats")
cursor = mydb.cursor()


def create_databse():
    cursor.execute("create database if not exists SchereSteinPapierStats")


def create_table():
    #cursor.execute("use scheresteinpapierstats")
    sql = "create table if not exists game_stats (game_result int not null, move int not null)"
    cursor.execute(sql)


def insert_stats(game_result, move):
    #cursor.execute("use scheresteinpapierstats")
    sql = "insert into game_stats (Game_Result, Move) values(%s, %s)"
    val = (game_result, move)
    cursor.execute(sql, val)
    mydb.commit()


def get_game_stats():
    sql_wins = "Select count('Game_Result') from game_stats where game_Result = 1;"
    sql_losses = "Select count('Game_Result') from game_stats where game_Result = 0;"
    sql_draws = "Select count('Game_Result') from game_stats where game_Result = 2"

    cursor.execute(sql_wins)
    wins = cursor.fetchall()

    cursor.execute(sql_losses)
    losses = cursor.fetchall()

    cursor.execute(sql_draws)
    draws = cursor.fetchall()

    gamesplayed = wins[0][0] + losses[0][0] + draws[0][0]
    print("Spiele gespielt: "+str(gamesplayed))
    print("Gewonnen: "+str(wins[0][0])+" Verloren: "+str(losses[0][0])+" Unentschieden: "+str(draws[0][0]))


def count_player_moves():
    count_scissor = "Select count('move') from game_stats where move = 4;"
    count_rock = "Select count('move') from game_stats where move = 0;"
    count_paper = "Select count('move') from game_stats where move = 2;"
    count_lizard = "Select count('move') from game_stats where move = 3;"
    count_spock = "Select count('move') from game_stats where move = 1;"
    count_games_played = "Select count('move') from game_stats;"

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

    apiHandler.send_request("NoF4ll", number_scissor, number_rock, number_paper, number_spock, number_lizard)



    print("Anzahl der gewählten Spielfiguren:")
    print("Schere: "+str(number_scissor[0][0])+" Prozentanteil: "+str(round((number_scissor[0][0]/games_played[0][0])*100))+"%" +
          "\n Stein: "+str(number_rock[0][0]) +" Prozentanteil: "+str(round((number_rock[0][0]/games_played[0][0])*100))+"%" +
          "\n Papier: "+str(number_paper[0][0]) +" Prozentanteil: "+str(round((number_paper[0][0]/games_played[0][0])*100))+"%" +
          "\n Echse: "+str(number_lizard[0][0]) +" Prozentanteil: "+str(round((number_lizard[0][0]/games_played[0][0])*100))+"%" +
          "\n Spock: "+str(number_spock[0][0]) +" Prozentanteil: "+str(round((number_spock[0][0]/games_played[0][0])*100))+"%")
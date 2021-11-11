import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="bichl601")
cursor = mydb.cursor()


def create_databse():
    cursor.execute("create database if not exists SchereSteinPapierStats")


def create_table():
    cursor.execute("use scheresteinpapierstats")
    create_string = "create table stats (winner varchar(255), move varchar(255))"
    cursor.execute(create_string)
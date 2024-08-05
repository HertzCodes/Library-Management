import datetime
import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


class Database:
    _instance = None

    def __new__(cls):  # THERE CAN ONLY BE ONCE INSTANCE OF Database. (SINGLETON PATTERN)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.__localhost_connect = None
        self.__dbcursor = None
        self.__connect_to_database()

    def __connect_to_database(self):
        load_dotenv()  # LOADS .ENV FILE VARIABLES
        try:
            self.__localhost_connect = mysql.connector.connect(
                host="localhost",
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                database="library"
            )
            self.__dbcursor = self.__localhost_connect.cursor()
            self.__create_table_if_not_exists()
        except Error as errormessage:
            with open('database_logs.txt', 'a') as log:
                log.write(
                    f"{datetime.datetime.now()}\nDATABASE_ERROR: {errormessage}\n------------------------------------------------")

    def __create_table_if_not_exists(self):
        query_books = """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(150),
                author VARCHAR(150),
                summary VARCHAR(255) ,
                genre VARCHAR(150),
                date_added DATE,
                is_borrowed BIT(1),
                borrowed_by VARCHAR(150),
                stock INT
            )
        """
        query_users = """
            CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255),
            phone_number VARCHAR(255),
            creation_date DATE,
            borrowed_books VARCHAR(255),
            permission INT
                       )"""
        try:
            self.__dbcursor.execute(query_books)
            self.__dbcursor.execute(query_users)
            self.__localhost_connect.commit()  # COMMITS THE CHANGES TO DATABASE TO REFRESH THE DATA
        except Error as errormessage:
            with open('database_logs.txt', 'a') as log:
                log.write(
                    f"{datetime.datetime.now()}\nTABLE_ERROR: {errormessage}\n------------------------------------------------")

    def run_query(self, query, values= ''):
        try:
            self.__dbcursor.execute(query, values)
            if query.startswith("SELECT"):
                return self.__dbcursor.fetchall()

            self.__localhost_connect.commit()
            with open('database_logs.txt', 'a') as log:
                log.write(
                    f"{datetime.datetime.now()}\nQUERY: {query}\n------------------------------------------------\n")
        except Error as errormessage:
            with open('database_logs.txt', 'a') as log:
                log.write(
                    f"{datetime.datetime.now()}\nQUERY_ERROR: {errormessage}\n------------------------------------------------\n")
        os.chdir('..')



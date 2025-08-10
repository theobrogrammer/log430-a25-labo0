"""
Application example
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
import mysql.connector

class Calculator:
    def hello(self):
        return "Allo"

    def create_mysql_connection(self):
        try:
            load_dotenv(dotenv_path="../.env")
            db_host = os.getenv("DB_HOST")
            db_name = os.getenv("DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")     
            mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name).close()
            return "OK"
        except FileNotFoundError as e:
            print(e)
            return "Attention : Veuillez créer un fichier .env" 
        except Exception as e:
            return "Erreur : " + str(e)

        return "Connexion établie avec succès !"

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if (y != 0):
            return x / y
        else:
            return "Erreur : division par zéro"

if __name__ == "__main__":
    my_calculator = Calculator()
    message = my_calculator.hello()
    connection_status = my_calculator.create_mysql_connection()

    if connection_status != "OK":
        print(connection_status)
        quit()

    result = my_calculator.addition(1, 1)
    print(message)
    print('Résultat :', result)

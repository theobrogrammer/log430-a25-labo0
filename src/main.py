"""
Application example
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import json
import mysql.connector

def hello():
    return "Allo"

def create_mysql_connection():
    try:
        with open("../env.json") as file:
            env_vars = json.load(file)          
        mysql.connector.connect(host=env_vars['host'], user=env_vars['username'], password=env_vars['password'], database=env_vars['database']).close()
        return "OK"
    except FileNotFoundError as e:
        return "Attention : Veuillez créer un fichier env.json" 
    except Exception as e:
        return "Erreur : " + str(e)

    return "Connexion établie avec succès !"

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if (y != 0):
        return x / y
    else:
        return "Erreur : division par zéro"

if __name__ == "__main__":
    message = hello()
    connection_status = create_mysql_connection()

    if connection_status != "OK":
        print(connection_status)
        quit()

    result = addition(1, 1)
    print(message)
    print('Résultat :', result)

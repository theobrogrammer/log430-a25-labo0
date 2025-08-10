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

    with open("../env.json") as file:
        env_vars = json.load(file)

    try:
        mysql.connector.connect(host=env_vars['host'], user=env_vars['username'], password=env_vars['password'], database=env_vars['database']).close()
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
    create_mysql_connection()
    result = addition(1, 1)
    print(message)
    print('Résultat :', result)

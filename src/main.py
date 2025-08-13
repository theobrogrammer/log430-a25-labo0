"""
Application example
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os

class Calculator:
    def hello(self):
        return "Allo Calculatrice"

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
    result = my_calculator.addition(1, 1)
    print(message)
    print('Résultat :', result)

"""
Application example
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
class Calculator:
    def __init__(self):
        self.last_result = 0

    def get_hello_message(self):
        return "Calculatrice"

    def addition(self, v1, v2):
        self.last_result = v1 + v2
        return self.last_result

    def subtraction(self, v1, v2):
        self.last_result = v1 - v2
        return self.last_result

    def multiplication(self, v1, v2):
        self.last_result = v1 * v2
        return self.last_result

    def division(self, v1, v2):
        if (v2 != 0):
            self.last_result = v1 / v2
            return self.last_result
        else:
            self.last_result = "Error"
            return "Erreur : division par zéro"

if __name__ == "__main__":
    my_calculator = Calculator()
    message = my_calculator.get_hello_message()
    print(message)

    print("== Addition ==")
    val_x = input("Saisissez la valeur 1 : ")
    val_y = input("Saisissez la valeur 2 : ")
    my_calculator.addition(int(val_x), int(val_y))
    print('V1 + V2 =', my_calculator.last_result)
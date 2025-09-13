"""
Calculator app
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import time
import argparse
class Calculator:
    def __init__(self):
        self.last_result = 0

    def get_hello_message(self):
        """ Show welcome message """
        return "== Calculatrice v1.0 =="

    def addition(self, v1, v2):
        """ Add 2 values """
        self.last_result = v1 + v2
        return self.last_result

    def subtraction(self, v1, v2):
        """ Subtract 2 values """
        self.last_result = v1 - v2
        return self.last_result

    def multiplication(self, v1, v2):
        """ Multiply 2 values. """
        self.last_result = v1 * v2
        return self.last_result

    def division(self, v1, v2):
        """ Divide 2 values. Show an error if V2 is zero. """
        if (v2 != 0):
            self.last_result = v1 / v2
            return self.last_result
        else:
            self.last_result = "Error"
            return "Erreur : division par zéro"














   #  OUTSIDE the class
def run_interactive():
    is_running = 1
    my_calculator = Calculator()
    print(my_calculator.get_hello_message())

    while is_running == 1:
        print("Operation : additionner deux valeurs")
        val_x = input("Saisissez la valeur 1 : ")
        val_y = input("Saisissez la valeur 2 : ")
        my_calculator.addition(int(val_x), int(val_y))
        print('V1 + V2 =', my_calculator.last_result)
        is_running = int(input("Voulez-vous faire une autre addition ? [1 = Oui | 2 = Non] : "))

    print("Au revoir :)")


def run_service():
    import os, time
    calc = Calculator()
    print(calc.get_hello_message())
    print("[service] démarré. PID:", os.getpid(), flush=True)
    while True:
        calc.addition(2, 3)
        print(f"[service] heartbeat, last_result={calc.last_result}", flush=True)
        time.sleep(30)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["interactive", "service"], default="interactive")
    args = parser.parse_args()

    if args.mode == "service":
        run_service()
    else:
        run_interactive()
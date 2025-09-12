"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # ajoute src au PYTHONPATH
from calculator import Calculator


def test_app():
    my_calculator = Calculator()
    # Le message exact de la méthode est "== Calculatrice v1.0 =="
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="


def test_addition():
    my_calculator = Calculator()
    result = my_calculator.addition(2, 3)
    assert result == 5
    assert my_calculator.last_result == 5


def test_subtraction():
    my_calculator = Calculator()
    result = my_calculator.subtraction(10, 4)
    assert result == 6
    assert my_calculator.last_result == 6


def test_multiplication():
    my_calculator = Calculator()
    result = my_calculator.multiplication(7, 3)
    assert result == 21
    assert my_calculator.last_result == 21


def test_division_normal():
    my_calculator = Calculator()
    result = my_calculator.division(8, 2)
    assert result == 4.0  # Python retourne un float
    assert my_calculator.last_result == 4.0


def test_division_float_result():
    my_calculator = Calculator()
    result = my_calculator.division(7, 2)
    assert result == 3.5
    assert my_calculator.last_result == 3.5


def test_division_by_zero():
    my_calculator = Calculator()
    result = my_calculator.division(10, 0)
    # La méthode retourne une chaîne en français
    assert result == "Erreur : division par zéro"
    # Mais elle met last_result à "Error"
    assert my_calculator.last_result == "Error"
    
def test_division_by_zero_error():
    my_calculator = Calculator()
    result = my_calculator.division(10, 0)
    
    assert isinstance(result, float)
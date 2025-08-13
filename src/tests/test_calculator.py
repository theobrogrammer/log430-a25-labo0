from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.hello() == "Allo Calculatrice"

# TODO: ajoutez les tests
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "Calculatrice"

# TODO: ajoutez les tests
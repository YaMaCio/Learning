import pytest
class Calculator:
    def add(self, first, second):
        return first + second
    def sub(self, first, second):
        return first - second
    def multiple(self, first, second):
        return first * second
    def divide(self, first, second):
        return first / second
        
@pytest.fixture
def ret_calc():
    return Calculator()
    
def test_addition(ret_calc):
    assert ret_calc.add(2, 3) == 5
    
def test_substraction(ret_calc):
    assert ret_calc.sub(3, 2) == 1
    
def test_multiple(ret_calc):
    assert ret_calc.multiple(2, 3) == 6
    
def test_divide(ret_calc):
    assert ret_calc.divide(6, 3) == 2
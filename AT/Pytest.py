import pytest
from math import sqrt
def square_eq_solver(a, b, c):
    result = []
    discriminant = b * b - 4 * a * c
    if discriminant == 0:
        result.append(-b / (2 * a))
    else:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))
    return result
def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index+1} дорівнює {value:.02f}')
    else:
        print('Рівняння із заданими параметрами не має коренів')
    
class TestStringMethods():
    def test_one(self):
        result = square_eq_solver(10,0,0)
        assert result[0] == 0
    def test_two(self):
        result = square_eq_solver(2,5,-3)
        assert result[0] == 0.5
        assert result[1] == 3
    def test_three(self):
        result = square_eq_solver(10,0,2)
        assert result[0] == 0
        assert result[1] == 0
        
if __name__ == '__main__':
    TestStringMethods()

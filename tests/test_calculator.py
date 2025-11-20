"""
Калькулятор тесттері
"""

import pytest
import sys
import os

# Бағдарлама кодына жол қосу
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.calculator import Calculator


class TestCalculator:
    """Calculator класының тесттері"""
    
    def setup_method(self):
        """Әр тест алдында орындалатын әдіс"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Оң сандарды қосу"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 5) == 15
    
    def test_add_negative_numbers(self):
        """Теріс сандарды қосу"""
        assert self.calc.add(-1, -1) == -2
        assert self.calc.add(-5, 10) == 5
    
    def test_subtract_numbers(self):
        """Сандарды азайту"""
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 5) == 0
    
    def test_multiply_numbers(self):
        """Сандарды көбейту"""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide_numbers(self):
        """Сандарды бөлу"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        """Нөлге бөлу қатесі"""
        with pytest.raises(ValueError, match="Нөлге бөлуге болмайды"):
            self.calc.divide(10, 0)
    
    def test_power_operation(self):
        """Дәрежеге шығару"""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
    
    def test_integration_multiple_operations(self):
        """Бірнеше операцияларды бірге қолдану"""
        result = self.calc.add(
            self.calc.multiply(2, 3),
            self.calc.subtract(10, 4)
        )
        assert result == 12


def test_calculator_instance():
    """Calculator данасын тексеру"""
    calc = Calculator()
    assert calc is not None
    assert isinstance(calc, Calculator)


@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add_parametrized(a, b, expected):
    """Параметрленген қосу тесті"""
    calc = Calculator()
    assert calc.add(a, b) == expected

"""
Қарапайым калькулятор класы
"""

class Calculator:
    """Математикалық операцияларды орындайтын клас"""
    
    def add(self, a, b):
        """Екі санды қосу"""
        return a + b
    
    def subtract(self, a, b):
        """Екі санды азайту"""
        return a - b
    
    def multiply(self, a, b):
        """Екі санды көбейту"""
        return a * b
    
    def divide(self, a, b):
        """Екі санды бөлу"""
        if b == 0:
            raise ValueError("Нөлге бөлуге болмайды")
        return a / b
    
    def power(self, a, b):
        """Дәрежеге шығару"""
        return a ** b


def main():
    """Негізгі функция"""
    calc = Calculator()
    print("Калькуляторға қош келдіңіз!")
    
    # Тестілеу мысалы
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")
    print(f"3 * 4 = {calc.multiply(3, 4)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")


if __name__ == "__main__":
    main()

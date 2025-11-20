"""
Негізгі бағдарлама файлы
CI/CD жүйесін тексеру үшін
"""

from app.calculator import Calculator, main as calc_main


def run_demo():
    """Демонстрациялық функция"""
    print("=== Python CI/CD Demo ===")
    print()
    
    calc = Calculator()
    
    # Әр операцияны көрсету
    operations = [
        ("Қосу", "2 + 3", calc.add(2, 3)),
        ("Азайту", "5 - 2", calc.subtract(5, 2)),
        ("Көбейту", "3 * 4", calc.multiply(3, 4)),
        ("Бөлу", "10 / 2", calc.divide(10, 2)),
        ("Дәреже", "2 ** 3", calc.power(2, 3))
    ]
    
    for name, expression, result in operations:
        print(f"{name}: {expression} = {result}")
    
    print()
    print("Нөлге бөлу қатесін тексеру:")
    try:
        calc.divide(5, 0)
    except ValueError as e:
        print(f"Қате: {e}")


if __name__ == "__main__":
    run_demo()
    print()
    calc_main()

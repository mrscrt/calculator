def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль недопустимо"

def power(a, b):
    return a ** b

def main():
    print("Простой калькулятор")
    print("===================")

    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("0. Выход")

        choice = input("Введите номер операции: ")

        if choice == "0":
            print("До свидания!")
            break

        if choice in ("1", "2", "3", "4", "5"):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == "1":
                print("Результат:", add(num1, num2))
            elif choice == "2":
                print("Результат:", subtract(num1, num2))
            elif choice == "3":
                print("Результат:", multiply(num1, num2))
            elif choice == "4":
                print("Результат:", divide(num1, num2))
            elif choice == "5":
                print("Результат:", power(num1, num2))
        else:
            print("Ошибка: неверный выбор операции. Повторите попытку.")

if __name__ == "__main__":
    main()

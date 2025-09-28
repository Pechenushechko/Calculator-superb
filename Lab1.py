while True:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("Какую операцию вы хотите выполнить?")
    print("1.Сложение\n2.Вычитание\n3.Умножение\n4.Деление\n5.Выход")
    c = input("Введите номер операции (1/2/3/4/5): ")

    if c == "1":
        print(f"Сумма: {a + b}")
    elif c == "2":
        print(f"Разность: {a - b}")
    elif c == "3":
        print(f"Произведение: {a * b}")
    elif c == "4":
        if b != 0:
            print(f"Частное: {a / b}")
        else:
            print("Ошибка: Деление на ноль!")

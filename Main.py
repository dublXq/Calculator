import BackendMath

BM = BackendMath.BackendMath()

def formated_user(a, b, c):
    if c == "1":
        print(f"Сумма двух чисел {a} и {b} равна = {BM.add(int(a),int( b))}")
    elif c == "2":
        print(f"Вычитание двух чисел {a} и {b} равна = {BM.subtract(int(a),int(b))}")
    elif c == "3":
        print(f"Умножение двух чисел {a} и {b} равна = {BM.multiply(int(a),int( b))}")
    elif c == "4":
       print(f"Деление двух чисел {a} и {b} равна = {BM.divide(int(a),int(b))}")


class Main:
    if __name__ == '__main__':

        print(
            "\nЗдравствуйте.(👉ﾟヮﾟ)👉)\n\nЯ Калькулятор, который поможет посчитать любое выражение.\n"
            "\nЯ умею:\n1. Слаживать числа\n"
            "2. Вычитать числа\n"
            "3. Умножать числа\n"
            "4. Делить числа\n"
            "\nЧтобы начать, введите цифру -> 1. Для выхода, введите цифру -> 2.\n\nСоздатель --> https://github.com/dublXq\n")

        while True:
            val = input("1. Начать\n2. Выход\nВвод: ")
            if val == "1":
                a = input("Введите первое число: ")
                b = input("Введите второе число: ")
                c = input("Введите действие:\n"
                          "1. Сложение (+)\n"
                          "2. Вычитание (-)\n"
                          "3. Умножение(*)\n"
                          "4. Деление(/)\n"
                          "Ввод: ")
                if a.isdigit() and b.isdigit() and c.isdigit():
                    formated_user(a, b, c)
                    break
                else:
                    print("Вы в процессе, ввели что-то не то. Проверьте пожалуйста, и повторите попытку")
            elif val == "2":
                break
            else:
                print("Вы ввели что-то не то, повторите пожалуйста еще раз :) ")

def calculator_decorator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль неможливе!"
        except SyntaxError:
            return "Помилка: Некоректний синтаксис виразу!"
        except NameError:
            return "Помилка: Вираз містить недопустимі символи або букви!"
        except Exception as e:
            return f"Помилка виконання: {e}"

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)



print(calculate("2 + 2 * 2"))
print(calculate("10 / 0"))
print(calculate("2 + "))
print(calculate("раз + 2 + три + 4 +п'ять вийшов зайчик погулять"))
print(calculate(int(1 + 2 + 3 + 4 +5)))
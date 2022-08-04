"""Створіть декоратор expected(), який перевіряє, чи те, що повертає декорована
функція, має очікуваний тип.UnexpectedTypeException має бути викликано,
якщо тип, повернутий декорованою функцією, не відповідає очікуваним"""

"""Вимоги:
        expected() має приймати tuple (кортеж) багатьох типів, тобто валідація повинна 
     бути як для строки так і для інтеджера, якщо я передаю їх :)
        UnexpectedTypeException має бути викликано, якщо декорована функція 
    повертає об’єкт типу, який не було визначено в аргументах декоратора expected() 
    (ви повинні реалізувати цей клас помилки самостійно)"""


class UnexpectedTypeException(Exception):
    def __init__(self, message):
        super().__init__(message)


def expected(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            res_type = type(result)
            if not (res_type in types):
                return UnexpectedTypeException("Type of entry is unexpected, please use allowed options"
                                               " string or integer")
            else:
                return result

        return wrapper

    return decorator


@expected(types=(str, int))
def func():
    return 1.5


print(func())

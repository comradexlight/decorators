import datetime
import os


# 1.Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

def log_decorator(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open(f'{old_function.__name__}.log', 'a') as log:
            log.write(
                f'{datetime.datetime.now().isoformat(sep=",", timespec="minutes")}, {old_function.__name__}, {args, kwargs}, {result}\n')

        return result

    return new_function


# 2. Написать декоратор из п.1, но с параметром – путь к логам.

def log_decorator_with_path(path_to_log):
    def log_decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            os.makedirs(path_to_log, exist_ok=True)
            with open(f'{path_to_log}{os.sep}{old_function.__name__}.log', 'a') as log:
                log.write(
                    f'{datetime.datetime.now().isoformat(sep=",", timespec="minutes")}, {old_function.__name__}, {args, kwargs}, {result}\n')

            return result

        return new_function

    return log_decorator


# 3. Применить написанный логгер к приложению из любого предыдущего д/з.
if __name__ == '__main__':
    @log_decorator
    def calculate_salary(employee_name, payment_per_hour, hours):
        print(
            f'сотрудник {employee_name} заработал {payment_per_hour * hours} денег за {hours} часов \nсотрудник {employee_name} молодец')
        return payment_per_hour * hours


    calculate_salary('username', 200, 8)


    @log_decorator_with_path('/home/cxl/PycharmProjects/decorators/folder_with_log')
    def calculate_salary(employee_name, payment_per_hour, hours):
        print(
            f'сотрудник {employee_name} заработал {payment_per_hour * hours} денег за {hours} часов \nсотрудник {employee_name} молодец')
        return payment_per_hour * hours


    calculate_salary('second_username', 250, 8)

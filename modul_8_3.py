class Car:
    
    def __init__(self, model, __vin, __numbers: str):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(self)
        self.__is_valid_numbers(self)

    def __is_valid_vin(self, vin_number):
        vin_number = self.__vin
        if type(vin_number) is not int:
            raise IncorrectVinNumber(IncorrectVinNumber.exception_2(self))
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(IncorrectVinNumber.exception_1(self))
        else:
            return True

    def __is_valid_numbers(self, numbers):
        numbers = self.__numbers
        if type(numbers) is not str:
            raise IncorrectCarNumbers(IncorrectCarNumbers.exception_2(self))
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(IncorrectCarNumbers.exception_1(self))
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

    def exception_1(self):
        print('Неверный диапазон для vin номера')

    def exception_2(self):
        print('Некорректный тип vin номер')


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

    def exception_1(self):
        self.message = 'Неверная длина номера'
        print(self.message)

    def exception_2(self):
        self.message = 'Некорректный тип данных для номеров'
        print(self.message)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

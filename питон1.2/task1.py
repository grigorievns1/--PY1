# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:

    def __init__(self, fuel_consumption: float, tank_volume: int, fullness_tank: float):
        """
        Создание и подготовка к работе объекта "Машина"
        :param fuel_consumption: расход топлива на 100 км
        :param tank_volume: объем бака
        :param fullness_tank: заполненность бака
        Примеры:
        >>> car = Car(9.5, 40, 25)  # инициализация экземпляра класса
        """
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")
        self.fuel_consumption = fuel_consumption

        if not isinstance(tank_volume, (int)):
            raise TypeError("Объем бака должен быть int")
        if tank_volume < 0:
            raise ValueError("Объем бака не может быть отрицательным числом")
        self.tank_volume = tank_volume

        if not isinstance(fullness_tank, (int, float)):
            raise TypeError("Заполненность бака должна быть int или float")
        if fullness_tank < 0:
            raise ValueError("Заполненность бака не может быть отрицательным числом")
        self.fullness_tank = fullness_tank

    def distance(self) -> float:
        """
        Функция которая находит растояние, на которое хватит топлива
        :return: Растояние
        Примеры:
        >>> car = Car(9.5, 40, 25)
        >>> car.distance()
        """
        ...

    def empty_tank(self) -> float:
        """
        Функция которая расчитывает количество топлива, которое можно влить дополнительно,
        чтобы бак был полный
        :return: Количество топлива
        Примеры:
        >>> car = Car(9.5, 40, 25)
        >>> car.empty_tank()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()



class Contribution:

    def __init__(self, summa: float, prozent: float, month: int):
        """
        Создание и подготовка к работе объекта "Вклад"
        :param summa: первоначальная сумма вклада
        :param prozent: месячный процент
        :param month: количество месяцев
        Примеры:
        >>> contribution = Contribution(9000, 4, 25)  # инициализация экземпляра класса
        """
        if not isinstance(summa, (int, float)):
            raise TypeError("Сумма вклада должена быть int или float")
        if summa <= 0:
            raise ValueError("Сумма вклада должена быть положительным числом")
        self.summa = summa

        if not isinstance(prozent, (int, float)):
            raise TypeError("Процент должен быть int или float")
        self.prozent = prozent

        if not isinstance(month, (int)):
            raise TypeError("Количество месяцев должно быть int")
        if month < 0:
            raise ValueError("Количество месяцев не может быть отрицательным числом")
        self.month = month

    def grand_total(self) -> float:
        """
        Функция которая находит сумму вклада в конце срока
        :return: Сумма вклада
        Примеры:
        >>> contribution = Contribution(9000, 4, 25)
        >>> contribution.grand_total()
        """
        ...

    def benefit_monthly_capitalization(self) -> float:
        """
        Функция которая расчитывает выгоду от держания денег на вкладе с ежемесячной капитализацией
        в сравнении с grand_total()
        :return: Выгода
        Примеры:
        >>> contribution = Contribution(9000, 4, 25)
        >>> contribution.benefit_monthly_capitalization()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()


class Pair:

    def __init__(self, men: dict, woman: dict):
        """
        Создание и подготовка к работе объекта "пара"
        :param men: словарь, где ключи это возраст, а значения имена мужчин
        :param woman: словарь, где ключи это возраст, а значения имена женщин
        Примеры:
        >>> pair = Pair({19:"Иван", 26:"Сергей"}, {21:"Маша", 34:"Катя"})  # инициализация экземпляра класса
        """
        if not isinstance(men, (dict)):
            raise TypeError("должен быть dict")
        if men == {}:
            raise ValueError("словарь должен быть не пустым")

        if not isinstance(woman, (dict)):
            raise TypeError("должен быть dict")
        if woman == {}:
            raise ValueError("словарь должен быть не пустым")

        if len(men) != len(woman):
            raise ValueError("в словарях должно находиться одинаковое количество людей")

        self.men = men
        self.woman = woman

    def pair_m_and_w(self) -> list:
        """
        Функция которая составляет пары мужчина-женщина
        :return: список пар
        Примеры:
        >>> pair = Pair({19:"Иван", 26:"Сергей"}, {21:"Маша", 34:"Катя"})
        >>> pair.pair_m_and_w()
        """
        ...

    def average_age(self) -> list:
        """
        Функция которая расчитывает средний возраст пары
        :return: список словарей, где ключ-средний возраст, а значение-пара
        Примеры:
        >>> pair = Pair({19:"Иван", 26:"Сергей"}, {21:"Маша", 34:"Катя"})
        >>> pair.average_age()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
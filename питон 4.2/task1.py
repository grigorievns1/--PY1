import doctest
class Phone:
    """ Базовый класс телефон. """
    def __init__(self, firm: str, color: str):
        self.firm = firm
        self.color = color
        #self.power()
        """
        Создание и подготовка к работе объекта "Телефон"
        :param firm: название фирмы
        :param color: цвет телефона
        Примеры:
        >>> phone1 = Phone('Asus', 'Black')  # инициализация экземпляра класса
        """

    def turn_on(self) -> None:
        """
        Функция которая включает телефон.
        :return: None
        Примеры:
        >>> phone1 = Phone('Asus', 'Black')
        >>> phone1.turn_on()
        """
        pass

    def power(self) -> str:
        """
        Зарядка телефона - постоянное подключение к электросети.
        :return: Телефон подключен к электросети
        Примеры:
        >>> phone1 = Phone('Asus', 'Black')
        >>> phone1.power()
        """
        return f"Телефон подключен к электросети"

    def __str__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса для пользователей
        :return: f"Телефон фирмы {self.firm}. Цвет {self.color}"
        Примеры:
        >>> phone1 = Phone('Asus', 'Black')
        >>> print(str(phone1))
        """
        return f"Телефон фирмы {self.firm}. Цвет {self.color}"

    def __repr__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса в режиме отладки
        :return: f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r})"
        Примеры:
        >>> phone1 = Phone('Asus', 'Black')
        >>> print(repr(phone1))
        """
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r})"


class MobilePhone(Phone):
    """Дочерний класс мобильный телефон."""
    def __init__(self, firm: str, color: str, functions: list, adapter: dict):
        super().__init__(firm, color)
        self.functions = functions
        self.adapter = adapter
        self.power()
        """
        Создание и подготовка к работе объекта "Mобильный телефон"
        super().__init__(firm, color) перегружаем метод инициализации родительского класса Phone
        :param function: список функций телефона
        :param adapter: зарядное устройство
        Примеры:
        >>> phone2 = MobilePhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'})  # инициализация экземпляра класса
        >>> phone2.adapter
        >>> phone2.functions
        """
    @property
    def functions(self) -> list:
        """Возвращает список функций телефона."""
        return self._functions

    @functions.setter
    def functions(self, functions: list) -> None:
        """Устанавливает список функций телефона."""
        if not isinstance(functions, list):
            raise TypeError("Список функций должен быть типа list.")
        self._functions = functions

    def power(self) -> str:
        """
        Зарядка мобильного телефона - подключение к электросети при помощи адаптера.
        :return: Телефон подключен к электросети \
        f"Для зарядки мобильного телефона используется адаптер {self.adapter}"
        Примеры:
        >>> phone2 = MobilePhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'})  # инициализация экземпляра класса
        >>> phone2.power()
        """
        super().power()
        return f"Для зарядки мобильного телефона используется адаптер {self.adapter}"

    def __str__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса для пользователей
        :return: f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}"
        Примеры:
        >>> phone2 = MobilePhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'})
        >>> print(str(phone2))
        """
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}"

    def __repr__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса в режиме отладки
        :return: f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}, functions={self.functions!r})
        Примеры:
        >>> phone2 = MobilePhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'})
        >>> print(repr(phone2))
        """
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}, functions={self.functions!r})"

class SmartPhone(MobilePhone):
    """Дочерний класс смартфон."""
    def __init__(self, firm: str, color: str, functions: list, adapter: dict, internet: bool, wireless_charger: dict):
        super().__init__(firm, color, functions, adapter)
        self.internet = internet
        self.wireless_charger = wireless_charger
        self.power()
    """
    Создание и подготовка к работе объекта "Cмартфон"
    super().__init__(firm, color, function, adapter) перегружаем метод инициализации родительского класса MobilePhone
    :param internet: наличие или отсутствие интернета
    :param wireless_charger: беспроводное зарядное устройство
    Примеры:
    >>> phone3 = SmartPhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'}, True, {'I': '3A', 'W': '10V'})  # инициализация экземпляра класса
    >>> phone3.internet
    >>> phone3.wireless_charger
    """

    """Зарядка смартфона - подключение к электросети при помощи адаптера или беспроводной зарядки."""
    def power(self) -> str:
        """
        Зарядка мобильного телефона - подключение к электросети при помощи адаптера с возможностью
        беспроводной зарядки.
        :return: Телефон подключен к электросети \
        f"Для зарядки мобильного телефона используется адаптер {self.adapter}" \
        f"Для зарядки смартфона можно использовать беспроводную зарядку {self.wireless_charger}"
        Примеры:
        >>> phone3 = SmartPhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'}, True, {'I': '3A', 'W': '10V'})
        >>> phone3.power()
        """
        super().power()
        return f"Для зарядки смартфона можно использовать беспроводную зарядку {self.wireless_charger}"

    def __str__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса для пользователей
        :return: f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}. Интернет {self.internet}."
        Примеры:
        >>> phone3 = SmartPhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'}, True, {'I': '3A', 'W': '10V'})
        >>> print(str(phone3))
        """
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}. Интернет {self.internet}."

    def __repr__(self) -> str:
        """
        Mагический метод для отображения информации об объекте класса в режиме отладки
        :return: f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}," \
               f" functions={self.functions!r}, internet={self.internet!r})"
        Примеры:
        >>> phone3 = SmartPhone('Asus', 'Black', ['SMS'], {'I': '1A', 'W': '5V'}, True, {'I': '3A', 'W': '10V'})
        >>> print(repr(phone3))
        """
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}," \
               f" functions={self.functions!r}, internet={self.internet!r})"

if __name__ == "__main__":
    
    doctest.testmod()

    #phone1 = Phone('Pus', 'Pus')
    #phone2 = MobilePhone('qq', 'ww', ['aa', 1], {1: 'j'})
    #phone3 = SmartPhone('asd', 'qwerv', ['wwr'], {1:'pp'}, True, {1:'wrr'})
#print(phone1)
#print(Phone.count_)
#print(phone2)
    #print(phone2)
    #print(phone2.power())

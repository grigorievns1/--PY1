if __name__ == "__main__":
    # Write your solution here
    pass

class Phone:
    """ Базовый класс телефон. """
    phone_count = 0 # Количество телефонов
    def __init__(self, firm: str, color: str):
        self.firm = firm
        self.color = color
        self.count_()
        self.power()
    """Считаем количество телефонов введенных пользователем."""
    @classmethod
    def count_(cls) -> None:
        cls.phone_count += 1

    """Зарядка телефона - постоянное подключение к электросети."""
    def power(self) -> None:
        ...

    def __str__(self) -> str:
        return f"Телефон фирмы {self.firm}. Цвет {self.color}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r})"


class MobilePhone(Phone):
    """Дочерний класс мобильный телефон."""
    def __init__(self, firm: str, color: str, functions: list, adapter: dict):
        super().__init__(firm, color)
        self.functions = functions
        self.adapter = adapter
        self.power()

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

    """Зарядка мобильного телефона - периодическое подключение к электросети при помощи адаптера. 
    Адаптер в виде словаря, где указана техническая информация"""
    def power(self) -> None:
        ...
    def __str__(self) -> str:
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}, functions={self.functions!r})"

class SmartPhone(MobilePhone):
    def __init__(self, firm: str, color: str, functions: list, adapter: dict, internet: bool, wireless_charger: dict):
        super().__init__(firm, color, functions, adapter)
        self.internet = internet
        self.wireless_charger = wireless_charger
        self.power()

#class SmartPhone(Phone):
    #def __init__(self, firm: str, color: str, functions: list, adapter: dict, internet: bool, wireless_charger: dict):
        #super().__init__(firm, color)
        #self.adapter = adapter
        #self.function = function
        #self.internet = internet
        #self.wireless_charger = wireless_charger
        #self.power()

    """Зарядка смартфона - периодическое подключение к электросети при помощи адаптера. 
    Адаптер в виде словаря, где указана техническая информация. А так же беспроводная зарядка."""
    def power(self) -> None:
        ...

    def __str__(self) -> str:
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}. Интернет {self.internet}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}, functions={self.functions!r}, internet={self.internet!r})"

phone1 = Phone('Pus', 'Pus')
#phone2 = MobilePhone('qq', 'ww', ['aa', 1], {1: 'wee'})
phone3 = SmartPhone('asd', 'qwerv', ['wwr'], {1:'pp'}, True, {1:'wrr'})
#print(phone1)
#print(Phone.count_)
#print(phone2)
print(phone3)
#print(Phone.count_)
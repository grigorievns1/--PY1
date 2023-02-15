
class Phone:
    """ Базовый класс телефон. """
    def __init__(self, firm: str, color: str):
        self.firm = firm
        self.color = color
        #self.power()

    """Включить телефон."""
    def turn_on(self) -> None:
        pass

    """Зарядка телефона - постоянное подключение к электросети."""
    def power(self) -> str:
        return f"Телефон подключен к электросети"

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

    """Зарядка мобильного телефона - подключение к электросети при помощи адаптера. 
    Адаптер в виде словаря, где указана техническая информация"""
    def power(self) -> str:
        super().power()
        return f"Для зарядки мобильного телефона используется адаптер {self.adapter}"

    def __str__(self) -> str:
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}, functions={self.functions!r})"

class SmartPhone(MobilePhone):
    """Дочерний класс смартфон."""
    def __init__(self, firm: str, color: str, functions: list, adapter: dict, internet: bool, wireless_charger: dict):
        super().__init__(firm, color, functions, adapter)
        self.internet = internet
        self.wireless_charger = wireless_charger
        self.power()

    """Зарядка смартфона - подключение к электросети при помощи адаптера или беспроводной зарядки."""
    def power(self) -> str:
        super().power()
        return f"Для зарядки смартфона можно использовать беспроводную зарядку {self.wireless_charger}"

    def __str__(self) -> str:
        return f"Телефон фирмы {self.firm}. Цвет {self.color}. Функции {self.functions}. Интернет {self.internet}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(firm={self.firm!r}, color={self.color!r}," \
               f" functions={self.functions!r}, internet={self.internet!r})"

if __name__ == "__main__":

    #phone1 = Phone('Pus', 'Pus')
    phone2 = MobilePhone('qq', 'ww', ['aa', 1], {1: 'j'})
    #phone3 = SmartPhone('asd', 'qwerv', ['wwr'], {1:'pp'}, True, {1:'wrr'})
#print(phone1)
#print(Phone.count_)
#print(phone2)
    print(phone2)
    print(phone2.power())

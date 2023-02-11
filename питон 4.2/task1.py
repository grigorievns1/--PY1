if __name__ == "__main__":
    # Write your solution here
    pass

class Book:
    """ Базовый класс книги. """
    library_count = 0 # Количество напечатанных книг
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
        self.library()
        self.library_add = []
    """Считаем количество книг введенных пользователем."""
    @classmethod
    def library(cls) -> None:
        cls.library_count += 1

    """Добавляем книгу в библиотеку с указанием автора и названия книги."""
    def library_add(self) -> None:
        self.library_add.append({'name': self.name, 'author': self.author})

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс бумажные книги."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
        self.library_add = []

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = pages

    """Добавляем книгу в библиотеку с указанием автора, названия книги и количества страниц."""
    def library_add(self) -> None:
        self.library_add.append({'name': self.name, 'author': self.author, 'pages': self.pages})

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
        self.library_add = []

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, duration: int) -> None:
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float.")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом.")
        self._duration = duration

    """Добавляем книгу в библиотеку с указанием автора, названия книги и ее продолжительности."""
    def library_add(self) -> None:
        self.library_add.append({'name': self.name, 'author': self.author, 'duration': self.duration})

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

#book1 = AudioBook('Pus', 'Pus', 1.0)
#print(book1.library_add)
#print(book1)
book2 = Book('Pus', 'Pus')
book3 = Book('A', 'v')
book4 = Book('q', 'w')
print(Book.library_add)
print(Book.library_count)
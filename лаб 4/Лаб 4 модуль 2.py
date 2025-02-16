if __name__ == "__main__":
    # Write your solution here
    class Publication:
        """
            Базовый класс для публикаций:

            Атрибуты:
            title: название публикации
            author: автор публикации
            year: год публикации
            """

        def __init__(self, title: str, author: str, year: int):
            self.title = title
            self.author = author
            self.year = year

        def __str__(self):
            return f'Название: {self.title}, автор: {self.author}, год выпуска: {self.year}'

        def __repr__(self):
            return f'Название: (title={self.title!r}, автор ={self.author!r}, год={self.year!r})'


    class Book(Publication):
        """
           Класс Book, наследуется от Publication
           Атрибуты:
           genre: жанр книги
           pages: количество страниц
           """

        def __init__(self, title: str, author: str, genre: str, year: int, pages: int):
            super().__init__(title, author, year)
            self.__genre = genre
            self.__pages = pages

        def __str__(self):
            return f'{super().__str__(),}, жанр:{self.__genre}, количество страниц - {self.__pages}'

        def __repr__(self):
            return (f"Book(Название = {self.title!r}, автор ={self.author!r}, год ={self.year!r}, "
                    f"жанр ={self.__genre!r}, количество страниц={self.__pages!r})")

        def read_book(self, pages_read: int):
            """
                    Метод для чтения книги:
                     pages_read: Количество прочитанных страниц
                     return: Сообщение о прочитанных страницах
                    """
            if pages_read > self.__pages:
                raise ValueError(
                    'Количество прочитанных страниц не может быть больше общего количества страниц в книге')
            return f'Вы прочитали {pages_read} в книге {self.title}'


    # Примеры использования
    publication = Publication('Квантовая физика: основные законы', 'И.Е. Иродов', 2010)
    print(publication)

    book_1 = Book('Белые ночи', 'Ф.М. Достоевский', 'повесть', 1848, 57)
    print(book_1)
    print(book_1.read_book(40))

    book_2 = Book('451 градус по Фаренгейту', 'Рей Бредбери', 'антиутопия', 1953, 289)
    print(book_2)
    print(book_2.read_book(295))

    pass

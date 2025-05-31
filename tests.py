
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()
        assert collector.get_book_genre("Гарри Поттер") == ''

    def test_add_new_book_rejects_long_name(self):
        collector = BooksCollector()
        long_name = "а" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_does_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга1")
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_does_not_add_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    @pytest.mark.parametrize("genre", ['Фантастика', 'Ужасы', 'Детективы'])
    def test_set_book_genre_sets_if_valid(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", genre)
        assert collector.get_book_genre("Книга2") == genre

    def test_set_book_genre_ignores_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Неизвестный жанр")
        assert collector.get_book_genre("Книга3") == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Фантастика1")
        collector.set_book_genre("Фантастика1", "Фантастика")
        collector.add_new_book("Ужасы1")
        collector.set_book_genre("Ужасы1", "Ужасы")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == ["Фантастика1"]

    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Комедия1")
        collector.set_book_genre("Комедия1", "Комедии")
        collector.add_new_book("Ужасы1")
        collector.set_book_genre("Ужасы1", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Комедия1" in children_books
        assert "Ужасы1" not in children_books

    def test_add_book_in_favorites_adds_only_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга4")
        collector.add_book_in_favorites("Книга4")
        assert "Книга4" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_does_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Книга5")
        collector.add_book_in_favorites("Книга5")
        collector.add_book_in_favorites("Книга5")
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count("Книга5") == 1

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга6")
        collector.add_book_in_favorites("Книга6")
        collector.delete_book_from_favorites("Книга6")
        assert "Книга6" not in collector.get_list_of_favorites_books()
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


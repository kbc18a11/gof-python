from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Iterator(ABC):
    @abstractmethod
    def HasNext(self) -> bool: ...
    @abstractmethod
    def Next(self) -> any: ...


class Aggregate(ABC):
    def Iterator(self) -> Iterator: ...


@dataclass
class Book:
    name: str


@dataclass
class BookSheif(Aggregate):
    books: list[Book] = field(default_factory=list)

    def Iterator(self) -> Iterator:
        """booksをスキャンするためのBookSheifIteratorインスタンスを返す

        Returns:
            Iterator: BookSheifIteratorインスタンス
        """
        return BookSheifIterator(self)


@dataclass
class BookSheifIterator(Iterator):
    book_sheif: BookSheif
    index: int = 0

    def HasNext(self) -> bool:
        """次の本が存在しているか確認する

        Returns:
            bool: True -> 存在している, False -> 存在していない
        """
        return True if self.index < len(self.book_sheif.books) else False

    def Next(self) -> any:
        """次の本を返す

        Note:
            本を見つけた後にindexをインクリメントする

        Returns:
            any: 次の本
        """
        book = self.book_sheif.books[self.index]
        self.index += 1
        return book


def main():
    book_sheif = BookSheif()
    book_sheif.books.append(Book("a"))
    book_sheif.books.append(Book("b"))
    book_sheif.books.append(Book("c"))
    book_sheif.books.append(Book("d"))
    it = book_sheif.Iterator()
    while it.HasNext():
        book: Book = it.Next()
        print(book.name)
    book_sheif.books.append(Book("Z"))
    it = book_sheif.Iterator()
    while it.HasNext():
        book: Book = it.Next()
        print(book.name)


if __name__ == "__main__":
    main()

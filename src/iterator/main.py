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
    last: int
    _books: list[Book] = field(default_factory=list)

    def AddBook(self, book: Book):
        """本を追加する

        Args:
            book (Book): 追加する本

        Raises:
            Exception: 本棚がに入れられないなら投げる
        """
        if self.last >= len(self._books):
            self._books.append(book)
        else:
            raise Exception()

    def FindBook(self, index: int) -> Book:
        """指定された位置の本を返す

        Args:
            index (int): 指定位置

        Returns:
            Book: 指定された位置の本
        """
        return self._books[index]

    def Iterator(self) -> Iterator:
        """booksをスキャンするためのBookSheifIteratorインスタンスを返す

        Returns:
            Iterator: BookSheifIteratorインスタンス
        """
        return BookSheifIterator(self)

    def getLength(self) -> int:
        """本棚にある本の数を返す

        Returns:
            int: 本棚にある本の数
        """
        return len(self._books)


@dataclass
class BookSheifIterator(Iterator):
    book_sheif: BookSheif
    index: int = 0

    def HasNext(self) -> bool:
        """次の本が存在しているか確認する

        Returns:
            bool: True -> 存在している, False -> 存在していない
        """
        return True if self.index < self.book_sheif.last else False

    def Next(self) -> any:
        """次の本を返す

        Note:
            本を見つけた後にindexをインクリメントする

        Returns:
            any: 次の本
        """
        book = self.book_sheif.FindBook(self.index)
        self.index += 1
        return book


def main():
    book_sheif = BookSheif(4)
    book_sheif.AddBook(Book("a"))
    book_sheif.AddBook(Book("b"))
    book_sheif.AddBook(Book("c"))
    book_sheif.AddBook(Book("d"))
    it = book_sheif.Iterator()
    while it.HasNext():
        book: Book = it.Next()
        print(book.name)


if __name__ == "__main__":
    main()

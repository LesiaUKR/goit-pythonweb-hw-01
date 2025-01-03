from abc import ABC, abstractmethod
from colorama import Fore, Style
from typing import List


# SRP(Single responsibility):
# Class for representing a book
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP(Interface segregation):
# Interface for library operations
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# LSP(Liskov substitution):
# Library class implementing the LibraryInterface
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def get_books(self) -> List[Book]:
        return self.books


# OCP(opened/closed):
# Extension for new functionality - filtering books by year
class FilterableLibrary(Library):
    def get_books_by_year(self, year: int) -> List[Book]:
        return [book for book in self.books if book.year == year]


# DIP(Dependency inversion):
# LibraryManager depends on an abstraction (LibraryInterface)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(
            Fore.GREEN +
            f"Book '{title}' added successfully!"
            + Style.RESET_ALL
        )

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        print(
            Fore.YELLOW +
            f"Book '{title}' removed successfully!" +
            Style.RESET_ALL
        )

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            print(Fore.RED + "No books in the library." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Books in the library:" + Style.RESET_ALL)
            for book in books:
                print(Fore.BLUE + str(book) + Style.RESET_ALL)


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = (input(
            "Enter command (add, remove, show, exit): ")
                   .strip().
                   lower()
                   )

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print(
                    Fore.MAGENTA +
                    "Exiting the program. Goodbye!" +
                    Style.RESET_ALL
                )
                break
            case _:
                print(
                    Fore.RED +
                    "Invalid command. Please try again." +
                    Style.RESET_ALL
                )


if __name__ == "__main__":
    main()

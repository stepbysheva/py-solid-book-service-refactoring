from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC


class Book(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, *args, **kwargs):
        pass


class Serializer(Book):
    def __init__(self, title: str, content: str):
        super().__init__(title, content)

    def display(self, serialize_type):
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Print(Book):
    def __init__(self, title: str, content: str):
        super().__init__(title, content)

    def display(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Display(Book):
    def __init__(self, title: str, content: str):
        super().__init__(title, content)

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book = Display(book.title, book.content)
            book.display(method_type)
        elif cmd == "print":
            book = Print(book.title, book.content)
            book.display(method_type)
        elif cmd == "serialize":
            book = Serializer(book.title, book.content)
            return book.display(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))

from typing import List, Any

class Book:
    def __init__(self, title:str, authors: List[str], publisher: str, isbn: str, price: float)-> None:
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return """Ttile: {}
Authors : {}
Publisher: {}
ISBN : {}
Price: ${}""".format(self.title, ','.join(self.authors), self.publisher, self.isbn, self.price)

    def __eq__(self, other:Any)-> bool:
        return isinstance(other, Book) and self.isbn == other.isbn

    def num_authors(self)->int:
        return len(self.authors)


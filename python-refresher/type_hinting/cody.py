from typing import List # , Tuple, Set, etc...


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

        
class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."




def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

#Assignment1:Designing my own class
# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  
        self.current_page = 1

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self._pages} pages)"

    def read_page(self):
        if self.current_page < self._pages:
            self.current_page += 1
            return f"Reading page {self.current_page} of '{self.title}'."
        else:
            return f"You’ve finished reading '{self.title}'!"

    def bookmark(self):
        return f"Bookmarked page {self.current_page} of '{self.title}'."


# Subclass 1 - Ebook
class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read_page(self):
        return f"[E-Book] Page {self.current_page} of '{self.title}' glows on your screen."


# Subclass 2 - Audiobook
class AudioBook(Book):
    def __init__(self, title, author, pages, narrator):
        super().__init__(title, author, pages)
        self.narrator = narrator

    def read_page(self):
        return f"[Audiobook] {self.narrator} narrates page {self.current_page} of '{self.title}'."



if __name__ == "__main__":
    physical = Book("2001", "Akoko", 328)
    kindle = Ebook("Dune", "Frank Herbert", 688, 5.2)
    audible = AudioBook("Kifo kisimani", "Ken Walibora", 448, "Ken Walibora")

    print(physical)
    print(physical.read_page())
    print(physical.bookmark())

    print(kindle)
    print(kindle.read_page())

    print(audible)
    print(audible.read_page())
    
    #Activity 2:Polymorphism
    # Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving "


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying "


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing "


class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling "


if __name__ == "__main__":
    vehicles = [
        Car("Audi"),
        Plane("Boeing 747"),
        Boat("Titanic"),
        Bicycle("Mountain Bike")
    ]

    for v in vehicles:
        print(v.move())

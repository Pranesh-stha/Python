from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.__title = title
        self.__item_id = item_id

    @abstractmethod
    def display_details(self):
        pass

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_item_id(self):
        return self.__item_id

    def set_item_id(self, item_id):
        self.__item_id = item_id


class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn, publication_year):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def display_details(self):
        print(f"Book: {self.get_title()}, ID: {self.get_item_id()}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.publication_year}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publisher):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_details(self):
        print(f"Magazine: {self.get_title()}, ID: {self.get_item_id()}, Issue: {self.issue_number}, Publisher: {self.publisher}")


class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_items = []

    def borrow_item(self, item):
        if item not in self.__borrowed_items:
            self.__borrowed_items.append(item)
            print(f"{self.__name} borrowed '{item.get_title()}'")
        else:
            print(f"{self.__name} has already borrowed '{item.get_title()}'")

    def return_item(self, item):
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)
            print(f"{self.__name} returned '{item.get_title()}'")
        else:
            print(f"{self.__name} has not borrowed '{item.get_title()}'")

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_borrowed_items(self):
        return self.__borrowed_items


items = {
    "B001": Book("1984", "B001", "George Orwell", "9780451524935", 1949),
    "M001": Magazine("Tech Weekly", "M001", 34, "TechMedia")
}

member1 = LibraryMember("P001", "Pranesh")
member2 = LibraryMember("L002", "Libisha")

member1.borrow_item(items["B001"])
member1.borrow_item(items["M001"])
member1.return_item(items["B001"])
member2.return_item(items["M001"])  

print("\nLibrary Items:")
for item in items.values():
    item.display_details()

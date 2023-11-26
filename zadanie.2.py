

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}\nOpen hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\nAddress: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublished: {self.publication_date}\nPages: {self.number_of_pages}\nBelongs to: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"\t{book}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student.first_name} {self.student.last_name}\nOrder date: {self.order_date}\nBooks:\n{book_list}"


library1 = Library("Paris", "Oli street", "12345", "9:00 AM - 5:00 PM", "123-456-7890")
library2 = Library("Gdansk", "Mer Street", "54321", "10:00 AM - 6:00 PM", "987-654-3210")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "Warsaw", "St", "12345", "111-222-3333")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "Wroclaw", "Post Street", "12345", "444-555-6666")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-10", "Poznan", "Love Street", "54321", "777-888-9999")

book1 = Book(library1, "2021-01-01", "Max", "Shrink", 220)
book2 = Book(library1, "2022-02-02", "Alex", "Dread", 250)
book3 = Book(library1, "2020-03-03", "Jessie", "James", 2540)
book4 = Book(library2, "2023-04-04", "Stun", "Smith", 300)
book5 = Book(library2, "2021-05-05", "Katrine", "Powder", 260)

student1 = Employee("Alice", "Johnson", "2022-01-15", "2000-10-05", "Katowice", "Great Street", "12345", "999-000-1111")
student2 = Employee("Bob", "Miller", "2022-02-20", "1998-12-15", "New York", "", "54321", "222-333-4444")
student3 = Employee("Charlie", "Brown", "2022-03-25", "2001-06-20", "Berlin", "Long Street", "12345", "555-666-7777")

order1 = Order(employee1, student1, [book1, book2], "2023-01-10")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-02-15")

print(order1)
print("\n------------------------\n")
print(order2)

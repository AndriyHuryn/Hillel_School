"""
Завдання 1
Реалізуйте клас «Car». Необхідно зберігати в полях класу: назву моделі,
рік випуску, виробника, об'єм двигуна, колір машини, ціну.
Реалізуйте методи класу для введення даних, виводу даних, реалізуйте
 доступ до окремих полів через методи класу."""


class Car:
    def __init__(self, model, prod_date, manufacture, engine_size, color, price):
        self.model = model
        self.prod_date = prod_date
        self.manufacture = manufacture
        self.engine_size = engine_size
        self.color = color
        self.price = price

    def print_description(self):
        print(f"Model:{self.model}, Year-{self.prod_date}, Country:{self.manufacture}, Engine size:{self.engine_size}, "
              f"Color:{self.color}, Price:{self.price}")

    def get_price(self):
        print(f"Car {self.model}\nhas this price:{self.price}")

    def get_engine(self):
        print(f"The {self.model}\nhas engine size of {self.engine_size}")

    def set_price(self, price):
        if price > 0:
            self.price = price
            print(f" {self.model} cost {price}")
        else:
            print("Invalid price!!!")



VW = Car(model="CC", prod_date=2015, manufacture="Germany", engine_size=2.0, color="Blue", price=10000)
Jeep = Car(model="Patriot", prod_date=2017, manufacture="USA", engine_size=4.0, color="White", price=20000)
Lanos = Car(model="Sens", prod_date=2016, manufacture="Ukraine", engine_size=1.6, color="Black", price=5000)

VW.set_price(100)

if __name__ == "__main__":
    cars = [VW, Jeep, Lanos]
    options = "View-(full details), Engine-(engine size), Price-(Price Range), Exit:"

    while True:
        filtered_option = input(f"Choose what would you like to do by typing following options\n {options}")
        if filtered_option == "View":
            for car in cars:
                car.print_description()
        elif filtered_option == "Engine":
            for car in cars:
                car.get_engine()
        elif filtered_option == "Price":
            for car in cars:
                car.get_price()
        elif filtered_option == "Exit":
            print("Bye bye......")
            break
        else:
            print(f"PLease choose one of the following options {options}")

VW.set_price(100)

"""Реалізуйте клас «Book». Необхідно зберігати в полях класу: назву книги,
рік випуску, видавництва, жанр, автора, ціну. Реалізуйте методи класу для введення даних, 
виведення даних, реалізуйте доступ до окремих полів через методи класу."""


"""---------------------------"""
#I have tried to get it by price but I gave up
#Everythign else is working, couldn;t figure it out by price
"""---------------------------"""
# class Book:
#     def __init__(self, name, year, publisher, genre, author, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def print_full_details(self):
#         print(f"The famous {self.name} was written by {self.author}, and first published in {self.publisher}"
#               f"in {self.year},\nit is easy to read as genre is '{self.genre}' and you can get it for {self.price}")
#
#     def get_name(self):
#         print(f"The name of the book is: '{self.name}'")
#
#     def get_price(self):
#         print(f"Price is running around ${self.price} for a book")
#
# Pinocchio = Book(name="Pinocchio", year=1883, publisher="Italy", genre="Kids", author="Carlo Collodi", price=10)
# MobyDick = Book(name="Moby Dick", year=1851, publisher="USA", genre="Adventure", author="Herman Melville", price=15)
# Potter = Book(name="Potter", year=1965, publisher="UK", genre="Fantasy", author="Joane Rowling", price=25)
#
# Pinocchio.print_full_details()
# MobyDick.get_name()
# Potter.get_price()
# if __name__ == "__main__":
#     bookshop = [Pinocchio, MobyDick, Potter]
#     options = "Yes/No"
#     filter_list = []
#     while True:
#         inputting = "YES" #input(f"would youliek to find Price Range:{options}:")
#         if inputting == "YES":
#             print("Enter Price Range:")
#             min = float(input('Enter min price: '))
#             max = float(input("Enter max price: "))
#             filter_list = filter_list(bookshop, lambda x: x.price > min and x. price < max)
#         elif input == "NO":
#             Pinocchio.print_full_details()
#             MobyDick.print_full_details()
#             Potter.print_full_details()
#         else:
#             print(f"Invalid entry, please choose {options}")
#     def func_filter(book):
#         return book.price > min and book.price<max
#
#
#
# """Завдання 3
#
# Реалізуйте клас «Stadium». Необхідно зберігати в полях класу: назву стадіону,
# дату відкриття, країну, місто, розміщення. Реалізуйте методи класу для введення даних,
# виведення даних, реалізуйте доступ до окремих полів через методи класу."""
#
# class Stadium:
#     def __init__(self, name, date, country, city, location):
#         self.name = name
#         self.date = date
#         self.country = country
#         self.city = city
#         self.location = location
#
#     def full_print(self):
#         print(f"The {self.name} is located in {self.city},{self.country} and was built in {self.date} to get there"
#               f" please google {self.location}")
#     def get_names(self):
#         print(f"Those name of the stadium  is: {self.name}")
#
# Hard_Rock_Arena = Stadium(name="Hard Rock Arena", date=1987, country="USA", city="Miami",location="Miami Gardens" )
# Michigan_stadium = Stadium(name="Michigan Football Stadium", date=1927, country="USA", city="Michigan",location="Ann Arbor" )
#
# Hard_Rock_Arena.full_print()
# Michigan_stadium.get_names()


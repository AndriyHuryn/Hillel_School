"""Додати поле "discount" в клас Product.
Додати метод get_price(),який вираховує ціну та повертає float на основі множення з полем discount
Розширити клас Laptop наступними полями motherboard_type material
Laptop має власний розширений show_details()"""

class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount} | {self.discount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}, ")

    def get_price(self):
        price = self.price * self.discount
        price = self.price - price
        print(f"Price for {self.name}, after given discount of {self.discount} is ${price}")

class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False):
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional
        return message

    def show_description(self):
        if self.lte is True:
            additional = "LTE"
        else:
            additional = ""
        additional = "LTE" if self.lte else ""
        print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    def __init__(self, motherboard_type, material, name, color, price, amount, discount):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    def show_description(self):
        if self.motherboard_type and self.material is True:
            addon = f"{self.motherboard_type}{self.material}"
            message = super().show_description()
            message += addon
        else:
            addon = ""
        print(f"Description: {self.name} : {self.color}, ${self.price} have only {self.amount} on hand, "
              f"based on {self.motherboard_type} motherboard and made of {self.material}")



iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=0.15)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True, discount=0.30)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount=0.40,
                motherboard_type="MSI", material="Aluminium")

iphone13.show_description()
lenovo.show_description()
iphone7.show_description()
iphone13.get_product_description()
lenovo.get_price()
lenovo.get_product_description()

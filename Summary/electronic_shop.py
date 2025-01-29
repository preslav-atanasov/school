class Electronic:
    def __init__(self, name: str, brand: str, price: float, quantity: int, discount: float = 0):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.__discount = discount  # Private attribute

    def set_discount(self, value: float):
        self.__discount = value  # Update discount value

    def get_discount(self):
        return self.__discount  # Getter method for discount

    def __repr__(self):
        return f"Product: {self.name}, Brand: {self.brand}, Cost: {self.price}, Quantity in Stock: {self.quantity}"


class Laptop(Electronic):
    def __init__(self, name: str, brand: str, price: float, quantity: int, processor: str):
        super().__init__(name, brand, price, quantity, discount=0)
        self.processor = processor

    def calc_price(self):
        return self.price * (1 - self.get_discount())


class Smartphone(Electronic):
    def __init__(self, name: str, brand: str, price: float, quantity: int, displaysize: str):
        super().__init__(name, brand, price, quantity, discount=0)
        self.displaysize = displaysize

    def calc_price(self):
        return self.price * (1 - self.get_discount())


# Create objects
electronic1 = Laptop("Laptop", "Dell", 1200, 2, "Qualcomm 3")
electronic2 = Smartphone("Smartphone", "Samsung", 800, 10, "10x3")

# Display initial product details
print(f"{electronic1}\n")
print(electronic2)

# Apply discounts
electronic1.set_discount(0.10)  # 10% discount
electronic2.set_discount(0.10)  # 10% discount

# Display final prices
print(f"Final price for {electronic1.brand + ' ' + electronic1.name} = {electronic1.calc_price():.2f}")
print(f"Final price for {electronic2.brand + ' ' + electronic2.name} = {electronic2.calc_price():.2f}")

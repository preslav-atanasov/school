class Class:

    def __init__(self, name):
        self.product_name = name
        self.products = []
        self.prices = []

    def add_product(self, name: str, product_price: float):
        self.products.append(name)
        self.prices.append(product_price)

    def remove_product(self, name: str, product_price: float):
        if name in self.products and product_price in self.prices:
            index = self.products.index(name)
            if self.prices[index] == product_price:
                self.products.pop(index)
                self.prices.pop(index)
                print(f"Продуктът {name} е премахнат.")
            else:
                print("Цената на продукта не съответства.")
        else:
            print("Продуктът не е намерен в количката.")

    def prices_sum(self):
        prices_sum = sum(self.prices)
        return prices_sum

    def __repr__(self):
        products = ", ".join(self.products)
        print(f"Продуктите в количката са: {products}. Обща цена: {self.prices_sum()}")


cart = Class("Количка")
while True:
    action = input("Изберете действие ('add' за добавяне, 'remove' за премахване, 'full' за край): ")

    if action == "full":
        cart.__repr__()
        break

    elif action == "add":
        product = input("Въведете марка/вид на продукта: ")
        price = float(input("Въведете цена на продукта: "))
        if 0.00 <= price:
            cart.add_product(product, price)
        else:
            print("Моля въведете продукт с действителна цена.")

    elif action == "remove":
        product = input("Въведете марка/вид на продукта за премахване: ")
        price = float(input("Въведете цена на продукта за премахване: "))
        cart.remove_product(product, price)

    else:
        print("Невалидно действие. Моля, опитайте отново.")

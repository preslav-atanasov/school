from Projects.project.products.base_product import BaseProduct
from Projects.project.products.chair import Chair
from Projects.project.products.hobby_horse import HobbyHorse
from Projects.project.stores.base_store import BaseStore
from Projects.project.stores.furniture_store import FurnitureStore
from Projects.project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCT_TYPES:
            raise Exception("Invalid product type!")

        product_class = self.VALID_PRODUCT_TYPES[product_type]
        product = product_class(model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store_class = self.VALID_STORE_TYPES[store_type]
        store = store_class(name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        valid_sub_type = "Furniture" if isinstance(store, FurnitureStore) else "Toys"

        sold_products = []
        for product in products:
            if product.sub_type == valid_sub_type:
                sold_products.append(product)
                store.products.append(product)
                self.products.remove(product)
                store.capacity -= 1
                self.income += product.price

        if sold_products:
            return f"Store {store.name} successfully purchased {len(sold_products)} items."
        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store_to_remove = next((store for store in self.stores if store.name == store_name), None)
        if not store_to_remove:
            raise Exception("No such store!")

        if store_to_remove.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store_to_remove)
        return f"Successfully unregistered store {store_to_remove.name}, location: {store_to_remove.location}."

    def discount_products(self, product_model: str):
        discounted_count = 0
        for product in self.products:
            if product.model == product_model:
                if product.sub_type == "Furniture":
                    product.discount(0.10)
                elif product.sub_type == "Toys":
                    product.discount(0.20)
                discounted_count += 1
        return f"Discount applied to {discounted_count} products with model: {product_model}"

    def statistics(self):
        unsold_products_count = len(self.products)
        total_net_price = sum(product.price for product in self.products)

        product_model_count = {}
        for product in self.products:
            product_model_count[product.model] = product_model_count.get(product.model, 0) + 1

        sorted_models = sorted(product_model_count.items())

        sorted_stores = sorted(store.name for store in self.stores)

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {unsold_products_count}. Total net price: {total_net_price:.2f}"
        ]

        for model, count in sorted_models:
            result.append(f"{model}: {count}")

        result.append(f"***Partner Stores: {len(self.stores)}***")
        for store_name in sorted_stores:
            result.append(store_name)

        return "\n".join(result)

    def request_store_stats(self, store_name: str):
        store = next((store for store in self.stores if store.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

from base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str, capacity=50, products: list = None):
        super().__init__(name, location, capacity, products)

    @property
    def store_type(self):
        return f"Furniture Store"

    def store_stats(self):
        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"
                f"Estimated future profit for {len(self.products)} products is {self.get_estimated_profit()}"
                f"**Furniture for sale:"
                f"")
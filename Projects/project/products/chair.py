from base_product import BaseProduct


class Chair(BaseProduct):
    def __init__(self, model: str, price: float, material="Wood", sub_type="Furniture"):
        super().__init__(model, price, material="Wood", sub_type="Furniture")
        self.material = material
        self.sub_type = sub_type

    def discount(self, discount: 0.10):
        self.price = self.price - self.price * discount
        return self.price




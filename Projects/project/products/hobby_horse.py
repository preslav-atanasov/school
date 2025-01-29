from base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model: str, price: float, material="Wood/Plastic", sub_type="Toys"):
        super().__init__(model, price, material="Wood/Plastic", sub_type="Toys")
        self.material = material
        self.sub_type = sub_type

    def discount(self, discount: 0.20):
        self.price = self.price - self.price * discount
        return self.price




class BaseProduct:
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    def discount(self, discount: float):
        pass

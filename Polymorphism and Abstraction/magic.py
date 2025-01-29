class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        new_name = f"{self.product_name}, {other.product_name}"
        new_cost = self.cost + other.cost
        return new_name, new_cost

purchase1 = Purchase("Sofa", 500)
purchase2 = Purchase("table", 300)
combined = purchase1 + purchase2
print(combined.product_name, combined.cost) # Sofa, Table

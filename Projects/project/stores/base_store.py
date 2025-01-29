class BaseStore:
    def __init__(self, name:str, location:str, capacity:int, products:list):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = products

    def get_estimated_profit(self):
        profit = sum(self.products) * 0.10
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    def store_type(self):
        return f"Base store"

    def store_stats(self):
        pass
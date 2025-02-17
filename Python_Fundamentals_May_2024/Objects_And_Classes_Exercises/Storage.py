class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if 1 + len(self.storage) <= self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

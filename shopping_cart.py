class Listing:
    def __init__(self, name, location, price, stock):
        self.name = name
        self.location = location
        self.price = price
        self.stock = stock
    def shipping_cost(self):
        return 0
    def headline(self):
        return "This is Headline"
    def update_stock(self):
        return self.stock + 1
    
class Shoppingcart:
    def __init__(self, items, checkout_time, total_price):
        self.items = items
        self.checkout_time = checkout_time
        self.total_price = total_price
    def add_items(self):
        return self.items + 1
    def remove_items(self):
        return self.items - 1
    
class Shoppingcart2:
    def __init__(self, items, checkout_time, total_price):
        self.items = items
        self.checkout_time = checkout_time
        self.total_price = total_price
    def add_items(self):
        return self.items + 1
    def remove_items(self):
        return self.items - 1
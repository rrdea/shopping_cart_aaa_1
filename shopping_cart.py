class Listing:

    def __init__(self, name, location, price, stock):
        self.name = name
        self.location = location
        self.price = price
        self.stock = stock

    def shipping_cost(self):
        return 1

    def headline(self):
        return f'{self.name} dari {self.location}' \
            f'(ongkir: Rp.{self.shipping_cost()} dengan harga Rp.{self.price}' \
            f'(stok tersedia {self.stock})'

    def update_stock(self, new_value):
        self.stock = new_value

    def __repr__(self):
        return self.name
    
class Shoppingcart:

    items = {}
    price = 0

    def __init__(self):
        return

    def add_items(self, item, count):
        if item.stock >= count:
            if self.items.__contains__(item):
                self.items[item] += count
            else:
                self.items[item] = count

            price = count * item.price
            self.price += price
            item.stock -= count
        else:
            print('stok tidak cukup')

    def remove_items(self, item, count):
        if self.items.__contains__(item):
            if self.items[item] >= count:
                self.items[item] -= count
                item.stock += count
                price = count * item.price
                self.price -= price
            else :
                print('barang yang akan dihapus melebihi stok')
        else:
            print('tidak ada barang')

    def get_total_price(self):
        total_price = self.price
        for item in self.items.keys():
            total_price += item.shipping_cost()
        return total_price


b1      = Listing('barang1', 'malang', 1000, 10)
b2      = Listing('barang2', 'malang', 1000, 10)

shop    = Shoppingcart()
shop.add_items(b1, 10)
shop.add_items(b2, 1)

print(shop.get_total_price())

shop.remove_items(b2, 1)

print(shop.get_total_price())
class Listing:

    def __init__(self, name, location, price, stock):
        self.name = name
        self.location = location
        self.price = price
        self.stock = stock

    def shipping_cost(self):
        if self.location == 'jawa':
            return 2000
        else:
            return 5000

    def headline(self):
        return f'{self.name} dari warehouse pulau {self.location}' \
            f'(ongkir: Rp.{self.shipping_cost()} dengan harga Rp.{self.price}' \
            f'(stok tersedia {self.stock})'

    def update_stock(self, new_value):
        self.stock = new_value

    def __repr__(self):
        return self.name
    
class Shoppingcart:

    items_jawa = []
    items_non_jawa = []
    price = 0

    def __init__(self):
        return

    def add_items(self, item):
        if item.location == 'jawa':
            self.items_jawa.append(item)
        else:
            self.items_non_jawa.append(item)
        self.price += item.price
        item.stock -= 1

    def remove_items(self, item):
        if(item in self.items_jawa):
            self.items_jawa.remove(item)
            self.price -= item.price
            item.stock += 1
        if (item in self.items_non_jawa):
            self.items_non_jawa.remove(item)
            self.price -= item.price
            item.stock += 1

    def get_total_price(self):
        total_price = self.price
        if self.items_jawa:
            total_price += 2000
        if self.items_non_jawa:
            total_price += 5000

        return total_price

mixer   = Listing('mixer', 'jawa', 50000, 20)
blender = Listing('blender', 'kalimantan', 30000, 20)
tas     = Listing('tas murah kw1', 'kalimantan', 15000, 2)

shop    = Shoppingcart()
shop.add_items(mixer)
shop.add_items(blender)
shop.add_items(tas)

print(shop.items_jawa)
print(shop.items_non_jawa)
print(shop.price)
print(shop.get_total_price())

shop.remove_items(tas)

print(shop.items_jawa)
print(shop.items_non_jawa)
print(shop.price)
print(shop.get_total_price())

'''
Input lokasi  : jawa dan luar jawa
jawa          : 2000
luar jawa     : 5000
consumer      : dari jawa

pengembangan :
1. bisa menentukan berapa byk yg ditambah dan hapus

tes 
'''
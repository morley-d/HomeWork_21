from classes.store import Store


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def __repr__(self):
        return f"{self.get_items(), self.get_capacity()}"

    def add(self, name, count):
        if name not in self.get_item_keys() \
                and self.get_unique_items_count() >= 5:
            print("Нельзя хранить более 5 разных товаров")
            return False
        else:
            if self.get_free_space() >= count:
                if name in self.get_item_keys():
                    self.get_items()[name] += count
                else:
                    self.get_items()[name] = count
                return True
            else:
                print("Недостаточно места")
                return False


shop_1 = Shop({"Phone": 5, "Macbook": 5})
shop_1.add("POCO F3", 3)
shop_1.add("Wash mashine", 2)
print(shop_1.get_free_space())
print(shop_1.get_unique_items_count())
shop_1.add("Xiaomi Mi12 Pro", 3)
print(shop_1.get_unique_items_count())
shop_1.add("Grill", 1)
print(shop_1.get_free_space())
shop_1.add("Wash mashine", 2)
print(shop_1.get_free_space())

print(shop_1.get_items())
shop_1.remove("Wash mashine", 4)
print(shop_1.get_free_space())
print(shop_1.get_unique_items_count())
print(shop_1.get_items())
shop_1.remove("POCO F3", 3)
print(shop_1.get_free_space())
print(shop_1.get_unique_items_count())
print(shop_1.get_items())

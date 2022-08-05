from classes.store import Store


MAX_UNIQUE_ITEMS = 5

class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def __repr__(self):
        return f"{self.get_items(), self.get_capacity()}"

    # увеличивает запас items с учетом лимита capacity и макс количества видов товара
    def add(self, name, count):
        if name not in self.get_item_keys() \
                and self.get_unique_items_count() >= MAX_UNIQUE_ITEMS:
            print(f"Нельзя хранить более {MAX_UNIQUE_ITEMS} разных товаров")
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

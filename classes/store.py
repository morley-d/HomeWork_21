from classes.storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def __repr__(self):
        return f"{self.__items, self.__capacity}"

    #  возвращает вместимость склада
    def get_capacity(self):
        return self.__capacity

    # возвращает список наименований товара
    def get_item_keys(self):
        return self.__items

    # увеличивает запас items с учетом лимита capacity
    def add(self, name, count):
        if self.get_free_space() >= count:
            if name in self.__items.keys():
                self.__items[name] += count
            else:
                self.__items[name] = count
            return True
        else:
            print("Недостаточно места")
            return False

    #  уменьшает запас items но не ниже 0
    def remove(self, name, count):
        if name not in self.__items.keys():
            print("Такого товара нет на складе")
            return False
        if self.__items[name] >= count:
            self.__items[name] -= count
            if self.__items[name] == 0:
                del self.__items[name]
            return True
        else:
            print("Недостаточно товара на складе")
            return False

    # возвращает количество свободных мест
    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    #  возвращает содержание склада в словаре {товар: количество}
    def get_items(self):
        return self.__items

    # возвращает количество уникальных товаров.
    def get_unique_items_count(self):
        return len(self.__items.keys())

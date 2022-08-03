from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    # увеличивает запас items с учетом лимита capacity
    def add(self, name, count):
        if self.get_free_space() >= count:
            if name in self.__items.keys():
                self.__items[name] += count
            else:
                self.__items[name] = count
        else:
            return "Недостаточно места на складе"

    #  уменьшает запас items но не ниже 0
    def remove(self, name, count):
        if self.__items[name] >= count:
            self.__items[name] -= count
        else:
            return "Недостаточно товара на складе"

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

from classes import Store, Shop, Request

# Пример запроса:
# Доставить 3 Магнитофон из склад_1 в магазин

print("Добро пожаловать в наш логистический сервис!")

storage_1 = Store(items={"Магнитофон": 5, "Патефон": 6, "Ксилофон": 7})
storage_2 = Store(items={"Телефон": 4, "Грамофон": 5, "Микрофон": 6})
shop_1 = Shop(items={"Телефон": 1, "Грамофон": 2, "Микрофон": 3})
storages = {"склад_1": storage_1, "склад_2": storage_2, "магазин": shop_1}

while True:
    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
            request = Request(storages, user_text)
            request.move_product()
            print("Текущяя заполненость объектов:")
            print(f"storage_1: {storage_1}")
            print(f"storage_2: {storage_2}")
            print(f"shop_1: {shop_1}")
        except Exception as e:
            print(f"Произошла ошибка: {e}\n Попробуйте ещё раз.")

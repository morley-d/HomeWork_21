from classes import Store, Shop, Request

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
        # print(storage_1)
        # print(storage_2)
        # print(shop_1)
        try:
            request = Request(storages, user_text)
            request.move_product()
        except Exception as e:
            print(f"Произощла ошибка: {e}\n Попробуйте ещё раз.")
        # print(f"storage_1: {storage_1}")
        # print(f"storage_2: {storage_2}")
        # print(f"shop_1: {shop_1}")


from classes.storage import Storage


class Request:

    # Доставить 3 Магнитофон из склад_1 в магазин

    storages = None

    def __init__(self, storages: dict, request_str: str):
        Request.storages = storages
        req_list = request_str.split()
        self.amount = int(req_list[1])
        self.product = req_list[2]
        self.fromm = req_list[4]
        self.to = req_list[6]

    def move_product(self):
        contragent1: Storage = Request.storages[self.fromm]
        if not contragent1.remove(self.product, self.amount):
            return False
        contragent2: Storage = Request.storages[self.to]
        if not contragent2.add(self.product, self.amount):
            contragent1.add(self.product, self.amount)

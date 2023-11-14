import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to receive the arguments
        assert price >= 0, f"Price {price} is a wrong value"
        assert quantity >= 0, f"Quantity {quantity} is a wrong value"

        # print(f"An instance was created :{name}")

        # Assign self to object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate

    def apply_increment(self, inc_value):
        self.__price = self.__price + self.__price * inc_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        print(self.__price * self.quantity)


    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("__price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
                Hello someone.
                We have {self.name} {self.quantity} times.
                """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()


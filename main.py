import datetime


class Transaction:
    __description: str = None
    __amount: float = None
    __important: bool = None
    __date: datetime.datetime = None

    def __init__(self, amount, description="Untitled Transaction", important=False):
        self.__amount = amount
        self.__description = description
        self.__important = important
        self.__date = datetime.datetime.now()

    def get_time(self) -> datetime.datetime:
        return self.__date

    def is_important(self) -> bool:
        return self.__important

    def set_important(self, important: bool = not __important):
        self.__important = important

    def get_description(self) -> str:
        return self.__description

    def get_amount(self, absolute: bool = False) -> float:
        return abs(self.__amount) if absolute else self.__amount

    def set_amount(self, amount: float):
        self.__amount = amount

    def set_description(self, description: str):
        self.__description = description

    def set_time(self, date: datetime.datetime):
        self.__date = date


class PersonalFinanceManager:
    __transactions: list[Transaction] = None
    currency: str = None

    def __init__(self, currency: str = '₹'):
        self.__transactions = []
        self.currency = currency

    def set_currency(self, currency: str):
        self.currency = currency

    def get_balance(self) -> float:
        balance: float = 0.0
        for transaction in self.__transactions:
            balance += transaction.get_amount()
        return balance

    def add_transaction(self, description: str, amount: float):
        transaction: Transaction = Transaction(amount, description)
        self.__transactions.append(transaction)
        print("Added transaction with ID:", len(self.__transactions) - 1)

    def add(self, transaction: Transaction):
        self.__transactions.append(transaction)

    def remove(self, index: int):
        self.__transactions.pop(index)

    def display_transactions(self):
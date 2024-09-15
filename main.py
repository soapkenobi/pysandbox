class Transaction:
    __description: str = None
    __amount: float = None
    __isImportant: bool = None

    def __init__(self, amount, description = "Untitled Transaction", isImportant = False):
        self.__amount = amount
        self.__description = description
        self.__isImportant = isImportant

    def get_amount(self, absolute = False):
        pass
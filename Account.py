class Account:
    def __init__(self, balance, number, agency, client, history):
        self._balance = balance
        self._number = number
        self._agency = agency
        self._client = client
        self._history = history

    def balance(self):
        return self._balance

    def new_account(self):
        # TODO: Implement method
        pass

    def withdraw(self, value) -> bool:
        # TODO: Implement method
        pass

    def deposit(self, value) -> bool:
        # TODO: Implement method
        pass
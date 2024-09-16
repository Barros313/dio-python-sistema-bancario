from models.transaction.History import History


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, value):
        balance = self.balance

        balance_exceeded = value > balance
        invalid_value = value <= 0

        if (invalid_value):
            print("### Falha na operação, valor inválido. ###")
            return False

        if (balance_exceeded):
            print("### Falha na operação, saldo insuficiente. ###")
            return False
        
        self._balance -= value
        print("--- Valor sacado com sucesso! ---")

        return True

    def deposit(self, value):
        invalid_value = value <= 0

        if (invalid_value):
            print("### Falha na operação, valor inválido. ###")
            return False
        
        print("--- Valor depositado com sucesso! ---")
        self._balance += value

        return True
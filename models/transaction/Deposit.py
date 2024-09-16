from models.transaction.ITransaction import ITransaction


class Deposit(ITransaction):
    def __init__(self, value):
        self._value = value


    @property
    def value(self):
        return self._value


    def register(self, account):
        transaction_success = account.deposit(self._value)

        if transaction_success:
            account.history.add_transaction(self)
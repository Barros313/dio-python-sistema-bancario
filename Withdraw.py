from ITransaction import ITransaction


class Withdraw(ITransaction):
    def __init__(self, value):
        self._value = value


    @property
    def value(self):
        return self._value


    def register(self, account):
        transaction_success = account.withdraw(self.value)

        if (transaction_success):
            account.history.add_transaction(self)
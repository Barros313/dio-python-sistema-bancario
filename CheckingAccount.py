class CheckingAccount:
    def __init__(self, limit, withdraw_limit):
        self._limit = limit
        self._withdraw_limit = withdraw_limit
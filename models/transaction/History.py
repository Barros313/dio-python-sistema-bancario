from datetime import datetime


class History:
    def __init__(self):
        self._transactions = list()

        
    @property
    def transactions(self):
        return self._transactions
    

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
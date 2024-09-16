from Account import Account
from Withdraw import Withdraw


class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, withdraw_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit


    def withdraw(self, value):
        withdraw_count = len(
            [transaction for transaction in self.history.transactions 
             if transaction["type"] == Withdraw.__name__])
        
        limit_exceeded = value > self.limit
        count_exceeded = withdraw_count >= self.withdraw_limit

        if (limit_exceeded):
            print("### Falha na operação, valor de saque superior ao limite permitido. ###")
            return False
        
        if (count_exceeded):
            print("### Falha na operação, quantidade de saque excedida. ###")
            return False
        
        return super().withdraw(value)
    
    def __str__(self):
        return f'''
    \n---------------------------------------------------
Agência: {self.agency}
Número Conta: {self.number}
Titular: {self.client.name}
---------------------------------------------------\n
'''
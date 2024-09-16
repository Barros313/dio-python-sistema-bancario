class Client:
    # Client attributes
    def __init__(self, address):
        self.address = address
        self.accounts = list()

    # Register transaction
    def make_transaction(self, account, transaction):
        transaction.register(account)

    # Add account
    def add_account(self, account):
        self.accounts.append(account)
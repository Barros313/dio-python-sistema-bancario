from models.account.CheckingAccount import CheckingAccount
from models.transaction.Deposit import Deposit
from models.person.Person import Person
from models.transaction.Withdraw import Withdraw

def main():
    clients = list()
    accounts = list()

    while True:
        option = menu()

        match option:
            case "d":
                deposit(clients)

            case "s":
                withdraw(clients)

            case "e":
                show_bank_statement(clients)

            case "nu":
                create_client(clients)

            case "nc":
                account_number = len(accounts) + 1
                create_account(account_number, clients, accounts)

            case "lc":
                fetch_accounts(accounts)

            case "q":
                break

            case _:
                print("### Operação inválida, por favor tente novamente. ###")

    return None


def menu():
    # Menu string template
    MENU = """\n
    ================ MENU ================
    [d] -  Depositar
    [s] -  Sacar
    [e] -  Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuário
    [q] -  Sair
    => """

    # Return user input
    return input(MENU)


def find_client(cpf, clients):
    client_filter = [client for client in clients if client.cpf == cpf]

    return client_filter[0] if client_filter else None


def get_client_account(client):
    if not client.accounts:
        print("### O cliente não possui conta! ###")
        return
    
    # FIXME: Client unable to choose account
    return client.accounts[0]


def deposit(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("### Cliente não existe! ###")
        return
    
    value = get_float("Informe o valor do depósito: ")
    transaction = Deposit(value)

    account = get_client_account(client)

    if not account:
        return
    
    client.make_transaction(account, transaction)


def withdraw(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("### Cliente não existe! ###")
        return
    
    value = get_float("Informe o valor do saque: ")
    transaction = Withdraw(value)

    account = get_client_account(client)

    if not account:
        return
    
    client.make_transaction(account, transaction)


def show_bank_statement(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("### Cliente não existe! ###")
        return

    account = get_client_account(client)
    if not account:
        return
    
    print("\n================ EXTRATO ================")
    transactions = account.history.transactions

    bank_statement = ""

    if not transactions:
        bank_statement = "Não foram realizadas movimentações"
    else:
        for transaction in transactions:
            bank_statement += f"\n{transaction['type']}: \n R$ {transaction['value']:.2f}"
    
    print(bank_statement)
    print(f"\n Saldo: R$ {account.balance:.2f}")
    print("==========================================")


def create_client(clients):
    cpf = input("Informe o CPF de cadastro (apenas números): ")
    cliente = find_client(cpf, clients)

    if cliente:
        print("### Cliente já cadastrado! ###")
        return
    
    name = input("Informe o nome completo do cliente: ")
    birthdate = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    client = Person(name=name, birthdate=birthdate, cpf=cpf, address=address)

    clients.append(client)

    print("--- Cliente cadastrado com sucesso! ---")

def create_account(account_number, clients, accounts):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("### Cliente não existe, encerrando criação de conta ###")
        return


    account = CheckingAccount.new_account(client=client, number=account_number)

    accounts.append(account)

    client.accounts.append(account)

    print("--- Conta criada com sucesso! ---")


def fetch_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(str(account))


def get_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Valor inválido. Digite um valor numérico!")
    


if __name__ == "__main__":
    main()
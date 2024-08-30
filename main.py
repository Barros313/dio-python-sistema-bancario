def main():
    # Define limits
    WITHDRAW_COUNT_LIMIT = 3
    WITHDRAW_VALUE_LIMIT = 500

    # Define account values
    balance = 0
    withdraw_counter = 0

    # Define users
    users = []

    # Bank statement string
    bank_statement = ""

    # Loop through interface until quit
    while True:
        # Get option input from menu
        option = menu()

        # Choose operation based on option input
        match option:
            case "d":
                # Get deposit value
                value = get_float("Insira o valor a ser depositado: ")

                # Deposit and update variable values
                balance, bank_statement = deposit(balance, value, bank_statement)

            case "s":
                # Get withdraw value
                value = get_float("Insira o valor a ser sacado: ")

                # Withdraw and update variables
                balance, bank_statement = withdraw(balance=balance, 
                                                   value=value, 
                                                   bank_statement=bank_statement, 
                                                   value_limit=WITHDRAW_VALUE_LIMIT, 
                                                   withdraw_counter=withdraw_counter, 
                                                   count_limit=WITHDRAW_COUNT_LIMIT
                )

            case "e":
                show_bank_statement(balance, bank_statement=bank_statement)
                                    
            case "nu":
                create_user(users)

            case "lc":
                fetch_users(users)

            case "q":
                break
            
            case _:
                print("Opção invalida, tente novamente.")

    # End of program
    return None


def menu():
    # Menu string template
    MENU = """
    ========== MENU ==========
    [d]   Depositar
    [s]   Sacar
    [e]   Extrato
    [nc]  Nova Conta
    [lc]  Listar contas
    [nu]  Novo usuário
    [q]   Sair

    =>"""

    # Return user input
    return input(MENU)


def withdraw(*, balance, value, bank_statement, value_limit, withdraw_counter, count_limit):
    # Define errors
    valid_input = (value > 0)
    valid_limit = (value <= value_limit)
    valid_counter = (withdraw_counter < count_limit)
    available_balance = (value < balance)

    # Print error if negative input
    if (not valid_input):
        print("### Valor inválido. ###")
        return None

    # Print error if surpassed withdraw value 
    if (not valid_limit):
        print(f"### Valor solicitado acima do permitido: {format_currency(value_limit)} ###")
        return None
    
    # Print error and exit if withdraw limit reached
    if (not valid_counter):
        print(f"### Limite diário de {count_limit} saques atingido ###")
        return None

    # Print error if insufficient funds
    if (not available_balance):
        print("### Saldo insuficiente. ###")
        return None

    # Update balance
    balance -= value

    # Increment withdraw counter
    withdraw_counter += 1

    # Insert transaction into bank statement
    bank_statement += f"Saque: {format_currency(value)}\n"
    
    # Print success message
    print("--- Valor sacado com sucesso! ---")

    # Return
    return balance, bank_statement


def deposit(balance, value, bank_statement, /):
    # Handle negative value
    if (value <= 0):
        # Print error
        print("### Valor de depósito inválido. ###")
        
        # Return unchaged values
        return balance, bank_statement

    # Update balance
    balance += value

    # Insert transaction into bank statement
    bank_statement += f"Depósito: {format_currency(value)}\n"

    # Print success message
    print("--- Valor depositado com sucesso! ---")

    # Return updated values
    return balance, bank_statement


def format_currency(value):
    # Return formated string
    return f"R${value:.2f}"


def get_float(message):
    # Loop until correct value
    while True:
        try:
            # Return float value
            return float(input(message))
        except ValueError:
            print("Not a valid number")


def create_user(users):
    # Get user cpf
    cpf = input("Informe CPF do usuário (apenas números): ")

    # Check if user is already registered
    current_user = find_user(cpf, users)
    if current_user:
        # Print error message and return
        print(f"### Usuário de CPF {cpf} já cadastrado. ###")
        return None
    
    # Create user dictionary
    user = dict()

    # Feed dicionary with input
    user["cpf"] = cpf
    user["name"] = input("Informe o nome completo do usuário: ")
    user["birthdate"] = input("Informe a data de nascimento do usuário (dd-mm-aaaa): ")
    user["address"] = input("Informe o endereço do usuário (logradouro, nro - bairro - cidade/uf): ")

    # Append to list
    users.append(user)

    # Print success message
    print("--- Usuário cadastrado com sucesso -- ")

    # Return
    return None


def find_user(cpf, users):
    # Return user if found else return None
    return [user for user in users if user["cpf"] == cpf]


def show_bank_statement(balance, /, *, bank_statement):
    print(
f'''
    \n========== Extrato ==========
{("Não foram realizadas transações") if not bank_statement else bank_statement}
Saldo: {format_currency(balance)}
'''
)

    return None


def create_account():
    return None


def fetch_users(users):
    for user in users:
        print(user)

    return None


if __name__ == "__main__":
    main()
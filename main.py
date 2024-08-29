# Define limits
WITHDRAW_COUNT_LIMIT = 3
WITHDRAW_VALUE_LIMIT = 500



def main():
    # Define account values
    balance = 0
    withdraw_counter = 0

    # Bank statement string
    bank_statement = ""

    # Loop through interface until quit
    while True:
        # Get option input from menu
        option = input()

        # Choose operation based on option input
        match option:
            case "d":
                value = get_float("Insira o valor a ser depositado: ")

                balance, bank_statement = deposit(balance, value, bank_statement)

                deposit()
            case "s":
                withdraw()
            case "e":
                print(bank_statement)
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

    print(MENU)



def withdraw():
    # Get global variables
    global balance, withdraw_counter, bank_statement

    # Get withdraw value
    value = get_float("Insira valor a ser sacado: ")

    # Print error if negative input
    if (value <= 0):
        print("Valor inválido.")
        return None

    # Print error if surpassed withdraw value 
    if (value > WITHDRAW_VALUE_LIMIT):
        print(f"Valor solicitado acima do permitido: {format_currency(WITHDRAW_VALUE_LIMIT)}")
        return None
    
    # Print error and exit if withdraw limit reached
    if (withdraw_counter > WITHDRAW_COUNT_LIMIT):
        print(f"Limite diário de {WITHDRAW_COUNT_LIMIT} saques atingido")
        return None

    # Print error if insufficient funds
    if (value > balance):
        print("Saldo insuficiente.")
        return None

    # Update balance
    balance -= value

    # Increment withdraw counter
    withdraw_counter += 1

    # Insert transaction into bank statement
    bank_statement += f"Saque: {format_currency(value)}\n"

    # Return
    return None


def deposit(balance, value, bank_statement, /):

    # Handle negative value
    if (value <= 0):
        # Print error
        print("Valor de depósito inválido.")
        
        # Return unchaged values
        return balance, bank_statement

    # Update balance
    balance += value

    # Insert transaction into bank statement
    bank_statement += f"Depósito: {format_currency(value)}\n"

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


def create_user():
    return None


def find_user():
    return None


def create_account():
    return None


def fetch_users():
    return None

if __name__ == "__main__":
    main()
# Define limits
WITHDRAW_COUNT_LIMIT = 3
WITHDRAW_VALUE_LIMIT = 500

# Define account values
balance = 0
withdraw_counter = 0

# Bank statement string
bank_statement = ""

# Menu string template
MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

def main():

    # Loop through interface until quit
    while True:
        # Get option input from menu
        option = input(MENU)

        # Choose operation based on option input
        match option:
            case "d":
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


def withdraw():
    # Get global variables
    global balance, withdraw_counter, bank_statement

    # Get withdraw value
    value = get_float("Insira valor a ser sacado: ")

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

    bank_statement += f"- {format_currency(value)}\n"

    return None


def deposit():
    # Get deposit value
    value = get_float("Insira valor a ser depositado: ")

    if (value <= 0):
        print("Valor de depósito inválido.")
        return None

    # Update balance
    global balance
    balance += value

    # Insert transaction into bank statement
    global bank_statement
    bank_statement += f"Depósito: {format_currency(value)}\n"

    # Return
    return None


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


if __name__ == "__main__":
    main()
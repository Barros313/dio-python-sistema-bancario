# Define limits
WITHDRAW_COUNT_LIMITE = 3
WITHDRAW_VALUE_LIMIT = 500

# Define account values
balance = 0
withdraw_counter = 0

# Bank statement string
bank_statement = ""


def main():
    # Menu string template
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=>"""

    # Loop through interface until quit
    while True:
        # Get option input from menu
        option = input(menu)

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

    # End of program
    return None


def withdraw():
    return None


def deposit():
    # Get deposit value
    value = get_float("Insira valor a ser depositado: ")

    # Update balance
    global balance
    balance += value

    # Insert transaction into bank statement
    global bank_statement
    bank_statement += f"+ {format_currency(value)}"

    # Return
    return None


""" def print_bank_statement():
    return None """


def format_currency(value):
    # Return formated string
    return f"R${value:.2f}"

def get_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Not a valid number")


if __name__ == "__main__":
    main()
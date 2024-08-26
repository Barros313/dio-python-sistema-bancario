# Account variables
balance = 0
limit = 500
bank_statement = ""
withdraw_counter = 0
WITHDRAW_LIMITE = 3


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
                print_bank_statement()
            case "q":
                break

    # End of program
    return None


def withdraw():
    return None


def deposit():
    return None


def print_bank_statement():
    return None


if __name__ == "__main__":
    main()
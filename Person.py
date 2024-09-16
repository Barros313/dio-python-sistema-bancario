from Client import Client


class Person(Client):
    # Person attributes
    def __init__(self, cpf, name, birthdate, address):
        super().__init__(address)
        self.name = name
        self.birthdate = birthdate
        self.cpf = cpf
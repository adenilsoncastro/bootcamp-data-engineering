import datetime
import math


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome} tem {self.idade} anos'


adenilson = Pessoa(nome='Adenilson', sobrenome='Castro',
                   data_de_nascimento=datetime.date(1996, 8, 27))
print(adenilson)
print(adenilson.nome)
print(adenilson.sobrenome)

print(adenilson.idade)

import datetime
import math
from typing import List


#
# Aqui a 'Pessoa' é definida
#
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

#
# Um 'Curricuo' recebe como atributo uma 'Pessoa', o que permite acessar os métodos
# e atributos da classe 'Pessoa'
#


class Curriculo():
    def __init__(self, pessoa: Pessoa, experiencias: List[str]) -> None:
        self.experiencias = experiencias
        self.pessoa = pessoa

    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)

    @property
    def cargo_atual(self) -> str:
        return self.experiencias[-1]

    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self) -> str:
        return f'{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos, já trabalhou' \
            f' em {self.quantidade_de_experiencias} empresas e atualmente trabalha na empresa {self.cargo_atual}'


adenilson = Pessoa(nome='Adenilson', sobrenome='Castro',
                   data_de_nascimento=datetime.date(1996, 8, 27))

curriculo_adenilson = Curriculo(
    pessoa=adenilson, experiencias=['Volvo', 'CINQ', 'MM'])

print(curriculo_adenilson.pessoa)

curriculo_adenilson.adiciona_experiencia('freela')
print(curriculo_adenilson)


#
# A classe 'Vivente' possui características inerentes a qualquer ser vivo
#
class Vivente:
    def __init__(self, nome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def emite_ruido(self, ruido: str):
        print(f'{self.nome} fez ruido: {ruido}')

#
# Uma 'Pessoa', por se tratar de um ser vivo, herda os métodos e atributos da
# classe 'Vivente
#


class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f'{self.nome} tem {self.idade} anos'

    def falar(self, frase: str):
        return self.emite_ruido(frase)


adenilson2 = PessoaHeranca(
    nome='adenilson', data_de_nascimento=datetime.date(1996, 8, 27))

print(adenilson2)
adenilson2.falar('Estou falando!')

#
# O mesmo é válido para o 'Cachorro'
#


class Cachorro(Vivente):
    def __init__(self, nome: str, data_de_nascimento: datetime.date, raca: str) -> None:
        super().__init__(nome, data_de_nascimento)
        self.raca = raca

    def __str__(self) -> str:
        return f'{self.nome} é da raca {self.raca} e tem {self.idade} anos'

    def latir(self):
        return self.emite_ruido('au au')


scooby = Cachorro(
    nome='scooby', data_de_nascimento=datetime.date(2010, 1, 1), raca='vira lata')

print(scooby)
scooby.latir()

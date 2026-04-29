from datetime import date

from pydantic import BaseModel


class Funcionario(BaseModel):
    nome: str
    data_nascimento: str
    salario: float
    nivel: str

    def idade(self) -> int:
        ano_nascimento = int(self.data_nascimento.split("/")[-1])
        return date.today().year - ano_nascimento

    def retornar_sobrenome(self) -> str:
        return self.nome.strip().split(" ")[-1]

    def calcular_bonus(self) -> float:
        valor = self.salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber bônus")
        return 0 if valor > 1000 else valor

    def calcular_decrescimo(self) -> None:
        FATOR = 0.9
        if self.salario == 100000:
            self.salario *= FATOR
        print(f"Novo salário é de: {self.salario}")

    def __str__(self) -> str:
        return f"Funcionario({self.nome}, {self.data_nascimento}, {self.salario})"

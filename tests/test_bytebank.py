from pytest import fixture, mark, raises

from bytebank import Funcionario


class TestFuncionario:
    @fixture
    def funcionario(self) -> Funcionario:
        nome = 'John Doe'
        data_nascimento = '01/10/1995'
        salario = 10000
        nivel = 'Diretor'
        return Funcionario(nome=nome, data_nascimento=data_nascimento, salario=salario, nivel=nivel)

    def test_quando_salario_superior_a_100000_decrescimo_deve_ser_de_10_porcento(self, funcionario: Funcionario):
        # arrange - input
        salario = 100000

        # arrange - output
        expected = 90000

        # act
        funcionario.salario = salario
        funcionario.calcular_decrescimo()

        # assert
        assert funcionario.salario == expected

    def test_quando_salario_recebe_1000_deve_retornar_1000(self, funcionario: Funcionario):
        # arrange - input
        salario = 1000

        # arrange - output
        expected = 1000

        # act
        funcionario.salario = salario

        # assert
        assert funcionario.salario == expected

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # arrange
        nome = 'John Doe'
        data_nascimento = '01/10/2000'
        salario = 1000
        nivel = 'Diretor'

        # act
        funcionario = Funcionario(
            nome=nome, data_nascimento=data_nascimento, salario=salario, nivel=nivel)
        resultado = funcionario.idade()

        # Then
        esperado = 26
        assert resultado == esperado

    def test_quando_sobrenome_recebe_john_doe_deve_retornar_doe(self):
        # arrange - input
        nome = 'John Doe'
        data_nascimento = '15/06/1992'
        salario = 10000.0
        nivel = 'Diretor'

        # arrange - output
        expected = 'Doe'

        # act
        funcionario = Funcionario(
            nome=nome, data_nascimento=data_nascimento, salario=salario, nivel=nivel)
        result = funcionario.retornar_sobrenome()

        # assert
        assert result == expected

    @mark.calcular_bonus
    def teste_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with raises(Exception):
            # arrange
            salario = 1000000  # entrada

            # act
            funcionario = Funcionario(
                nome='John Doe', data_nascimento='15/06/1992', salario=salario, nivel='Senior'
            )
            resultado = funcionario.calcular_bonus()

            # assert
            assert resultado

from bytebank import Funcionario


# john = Funcionario('John Doe', '15/06/1992', 1000.0)

# print(john.idade())

def test_idade():
    funcionario_teste = Funcionario('teste', '15/06/1992', 1111.0)
    print(f'Teste = {funcionario_teste.idade()}')


test_idade()

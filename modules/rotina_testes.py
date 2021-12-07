from modules.clientes import Cliente
from modules.produtos import Produto
from modules.vendas import Venda
from modules.funcionarios import Funcionario

class Testes:
    """Entendi que a ideia da rotina era receber uma lista fazer todo o ciclo e comparar que a saída era condizente com o esperado.
    pode subistituir as listas de exemplos dadas no main, se tiverem no mesmo formato (ordem das informações) vai dar certo.
    TO-DO: Organizar e documentar os métodos
    """

    def teste(produtos, clientes, funcionarios, vendas):        
        #instanciando os produtos
        produtos_cadastrados = []
        produt = produtos        
        for produto in produt:
            lista = []
            prod = Produto(produto[0], produto[1])            
            lista.append(prod.get_Descricao())
            lista.append(prod.get_Estoque())
            produtos_cadastrados.append(lista)
        print(produtos_cadastrados)

        #instanciando os clientes
        clientes_cadastrados = []
        clientes = clientes        
        for cliente in clientes:
            lista = []
            clie = Cliente(cliente[0], cliente[1])            
            lista.append(clie.get_nome())
            lista.append(clie.get_cpf())
            clientes_cadastrados.append(lista)
        print(clientes_cadastrados)

        #instanciando os funcionarios
        funcionarios_cadastrados = []
        funcionarios = funcionarios        
        for funcionario in funcionarios:
            lista = []
            func = Funcionario(funcionario[1], funcionario[0])
            func.nome = funcionario[0]
            func.id_func = funcionario[1]
            lista.append(func.get_nome())
            lista.append(func.get_id_func())
            funcionarios_cadastrados.append(lista)
        print(funcionarios_cadastrados)


        lista_vendas = vendas                  
        vendas_cadastradas = []
        for venda in lista_vendas:
            lista = []
            venda1 = Venda()
            venda1.nome = venda[0]
            venda1.produto = venda[1]
            venda1.id_func = venda[2]
            venda1.quantidade = venda[3]
            lista.append(venda1.nome)
            lista.append(venda1.produto)
            lista.append(venda1.id_func)
            lista.append(venda1.quantidade)
            vendas_cadastradas.append(lista)
        for produto in produtos_cadastrados:
            for venda in vendas_cadastradas:
                if venda[1] == produto[0]:
                    produto[1] -= venda[3]
        
        print(vendas_cadastradas)
        print(produtos_cadastrados)
            
        

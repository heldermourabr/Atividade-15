from modules.clientes import Cliente
from modules.produtos import Produto
from modules.funcionarios import Funcionario
from modules.vendas import Venda
from modules.rotina_testes import Testes


if __name__ == "__main__":
    """Sistema de cadastro de produtos, clientes, funcionarios e vendas com gestão de estoque.

    TO-DO - Fazer a rotina de verificação de cliente e funcionario cadastrados no ato da venda.
    """
    produtos_cadastrados = []
    clientes_cadastrados = []
    funcionarios_cadastrados = []
    vendas_cadastradas = []
    while True:
        print("", "Menu", "[1] - Cadastrar produtos", "[2] - Cadastrar Clientes", "[3] - Cadastrar Funcionários", "[4] - Fazer Venda", "[5] - Rodar testes", "[0] - Encerrar", sep = "\n")
        selecao = input("Digite a Opção: ")

        if selecao == "1":
            lista_produtos = Produto.cadastro_produto()
            produtos_cadastrados += lista_produtos
            print(produtos_cadastrados)

        elif selecao == "2":
            lista_clientes = Cliente.cadastro_cliente()
            clientes_cadastrados += lista_clientes
        
        elif selecao == "3":
            lista_funcionarios = Funcionario.cadastro_funcionarios()
            funcionarios_cadastrados += lista_funcionarios
        
        elif selecao == "4":         
            print(produtos_cadastrados)
            lista_vendas, produtos_cadastrados = Venda.cadastrar_venda(produtos_cadastrados)       
            vendas_cadastradas += lista_vendas
            print(produtos_cadastrados)  
                    
        elif selecao == "5":
            produtos = [["Arroz", 20], ["Feijão", 30], ["Macarrão", 15], ["Nescafé", 25]]
            clientes = [["Helder", "12345678910"], ["Maria", "98765432111"], ["José", "65412398720"], ["Luiza", "96325874131"]]
            funcionarios = [["Marta", "FUN01"], ["Carlos", "FUN02"], ["Mariana", "FUN03"], ["Karine", "FUN04"]]
            vendas = [["Helder", "Feijão", "FUN02", 4], ["Helder", "Arroz", "FUN02", 5], ["José", "Nescafé", "FUN01", 5], ["Luiza", "Macarrão", "FUN03", 3]]       
            
            Testes.teste(produtos, clientes, funcionarios, vendas)

        elif selecao == "0":
            print("Finalizando!")
            break

        else:
            print("opção inválida")
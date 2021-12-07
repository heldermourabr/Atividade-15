from modules.clientes import Cliente
from modules.produtos import Produto
from modules.funcionarios import Funcionario


class Venda():
    nome, descricao, id_func, quantidade = "", "", "", 0

    # def __init__(self, nome, descricao, id_func, quantidade):
    #     self.quantidade = quantidade
    #     super().__init__(nome)
    #     super().__init__(descricao)
    #     super().__init__(id_func)

        
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_Descricao(self, descricao):
        self.descricao = descricao
    
    def set_id_func(self, id_func):
        self.id_func = id_func

    def get_quantidade(self):
        return self.quantidade

    def get_nome(self):
        return self.nome
    
    def get_Descricao(self):
        return self.descricao
    
    def get_id_func(self):
        return self.id_func

    def cadastrar_venda(produtos):
        """Cadastro de produtos

        Args:
            produtos (Lista de listas): Recebe a lista de produtos para tratar os estoques

        Returns:
            [Lista de listas]: Retorna para o main uma lista de listas com as informações dos vendas cadastradas e dos produtos com estoque atualizados
        """

        lista_produtos = produtos        
    
        lista_vendas = []
        while True:
            escolha = input("Deseja fazr nova venda? S/N ")
            if escolha in "sS":
                venda = []
                venda1 = Venda()
                venda1.set_nome(input("Nome do cliente: ").title())
                venda1.set_Descricao(input("Descricao do produto: ").title())
                venda1.set_id_func(input("Id do vendedor: ").upper())
                venda1.set_quantidade(int(input("Quantidade vendida: ")))
                venda.append(venda1.get_nome())
                venda.append(venda1.get_Descricao())
                venda.append(venda1.get_id_func())
                venda.append(venda1.get_quantidade())
                lista_vendas.append(venda)
                for produto in lista_produtos:
                    if venda1.get_Descricao() == produto[0]:
                        produto[1] -= venda1.get_quantidade()
                    else:
                        continue
            elif escolha in "nN":
                return lista_vendas, lista_produtos                
                break

      
    


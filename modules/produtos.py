class Produto:
    descricao, estoque = "",0

    def __init__(self, descricao, estoque): 
        self.descricao = descricao    
        self.estoque = estoque
    
    
    def set_Descricao(self, descricao):
        self.descricao = descricao
          
    def set_Estoque(self, estoque):
        self.estoque = estoque
           
    def get_Descricao(self):
        return self.descricao
    
    def get_Estoque(self):
        return self.estoque
    
    def cadastro_produto():
        """Cadastro dos produtos

        Returns:
            [Lista de listas]: Retorna para o main uma lista de listas com as informações dos produtos cadastrados
        """
        lista_produtos = []
        escolha = "S"
        while True:
            # escolha = input("Deseja Cadastrar novo produto? S/N")
            if escolha in "sS":
                prod = []
                produto = Produto(input("Insira o nome do produto: ").title(), int(input("Quantidade em estoque: ")))
                prod.append(produto.get_Descricao())
                prod.append(produto.get_Estoque())
                lista_produtos.append(prod)
            elif escolha in "nN":
                return lista_produtos
            
                
            else:
                print("Opção inválida!")

            escolha = input("Deseja Cadastrar novo produto? S/N ")
            

    
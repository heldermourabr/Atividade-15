class Cliente:
    nome, cpf = "", ""

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def set_nome(self, nome):
        self.nome = nome
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf

    def cadastro_cliente():
        """Cadastro individual de cliente no banco

        Returns:
            [Lista de listas]: Retorna para o main uma lista de listas com as informações dos clientes cadastrados
        """
        lista_cliente = []
        while True:
            escolha = input("Deseja Cadastrar novo cliente? S/N: ")
            if escolha in "sS":
                clie = []
                cliente = Cliente(input("Insira o nome do cliente: ").title(), input("CPF: "))
                clie.append(cliente.get_nome())
                clie.append(cliente.get_cpf())
                lista_cliente.append(clie)
            elif escolha in "nN":
                return lista_cliente
                
            else:
                print("Opção inválida!")
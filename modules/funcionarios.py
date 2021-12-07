class Funcionario:
    id_func, nome = "", ""

    def __init__(self, id_func, nome):
        self.id_func = id_func
        self.nome = nome
    

    def set_id_func(self, id_func):
        self.id_func = id_func
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_id_func(self):
        return self.id_func
    
    def get_nome(self):
        return self.nome

    def cadastro_funcionarios():
        """Cadastro de funcionarios

        Returns:
            [Lista de listas]: Retorna para o main uma lista de listas com as informações dos funcionários cadastrados
        """
        lista_funcionarios = []
        while True:
            escolha = input("Deseja Cadastrar novo funcionario? S/N: ")
            if escolha in "sS":
                func = []
                funcionarios = Funcionario(input("Insira ID do funcionario: ").upper(), input("Insira o nome do funcionarios: ").title())                
                func.append(funcionarios.get_nome())
                func.append(funcionarios.get_id_func())
                lista_funcionarios.append(func)
            elif escolha in "nN":
                return lista_funcionarios
                
            else:
                print("Opção inválida!")

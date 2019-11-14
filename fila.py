class Fila:
    def __init__(self):
        self.dados = []

    def inserir(self, novoDado):
        self.dados.append(novoDado)

    def retirar(self):
        if self.dados: #verifica se contém dados a serem retirados, para evitar erro de interpretação do código
            return self.dados.pop(0)

    def estaVazio(self):
        if len(self.dados)==0: return True

    def visualizar(self):
        print(self.dados)

       
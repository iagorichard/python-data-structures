class Pilha:
    def __init__(self):
        self.dados = []

    def empilhar(self, novoDado):
        self.dados.append(novoDado)

    def desempilhar(self):
        if self.dados:
            return self.dados.pop(len(self.dados)-1)

    def estaVazio(self):
        return self.dados == []

    def visualizar(self):
        print(self.dados)
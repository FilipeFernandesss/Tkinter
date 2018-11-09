#Classe Item_Compra
class Item_Compra():
    #Método Construtor
    def __init__(self, nome, qtd):
        #Atributos
        self.nome = nome
        self.qtd = qtd

    #Método que converte a classe em texto
    def to_string(self):
        return self.nome + ';' + str(self.qtd)

    def get_nome(self):
        return self.nome

    def get_qtd(self):
        return self.qtd
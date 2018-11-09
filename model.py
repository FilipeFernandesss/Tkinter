#Classe de modelo
class Model:
    #Método construtor
    def __init__(self):
        self.lista_compras = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}
        self.control = None

    #Guarda a control associada
    def set_control(self, control):
        self.control = control

    #Método que recupera a lista
    def get_lista_compras(self):
        return self.lista_compras

    #Método para add item
    def add_item(self, item, qtd):

        if item in self.get_lista_compras():
            print("O item já pertencia a lista.")
            self.atualizar_quantidade(item, qtd)

        else:
            self.lista_compras[item] = qtd



    #Método para excluir item
    def exluir(self, item):
        if item in self.get_lista_compras():
            del self.get_lista_compras()[item]
        else:
            print("O item não está presente na lista")


    #Método para atualizar a quantidade
    def atualizar_quantidade(self, item, qtd):
        self.control.atualizar_quantidade(item, qtd)

    #Método para add a quantidade
    def add_quantidade(self, item, qtd):
        self.get_lista_compras()[item] = self.get_lista_compras()[item] + qtd



# Classe de controle
class Control:
    #Método construtor
    def __init__(self, view, model):
        #Atributos
        self.view = view
        self.model = model

    #Método para exibir menu
    def exibir_menu(self):
        #Acionar o método da classe View
        self.view.exibir_menu()

    #Método para recuperar lista de compras
    def get_lista_compras(self):
        #Acionar o método da classe Model
        return self.model.get_lista_compras()

    #Método para incluir item
    def incluir_item(self, item, qtd):
        self.model.add_item(item, qtd)

    #Método para excluir item
    def excluir(self, item):
        self.model.exluir(item)

    #Método para atualizar a quantidade
    def atualizar_quantidade(self, item, qtd):
        self.view.atualizar_quantidade(item, qtd)


    def add_quantidade(self,item, qtd):
        self.model.add_quantidade(item,qtd)

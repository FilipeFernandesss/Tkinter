#Classe BD_Simulado
#Importando classe
from item_compra import Item_Compra


class BD_Simulado():
    #Método Construtor
    def __init__(self):
        #Atributos
        self.lista_compras = []
        self.carregar_lista_compras()

    def carregar_lista_compras(self):
        '''#Colocar aqui código para abrir arquivo
        #Cada linha do arquivo separar nome e qtd split(';')
        #Cada linha do arquivo criar um objeto de Item_Compra
        #Inserir o objeto na llista de compra

        #ex: item1 = Item_Compra('tomate',10)
        #self.lista_compra.append(item1)'''

    def gravar_lista_compras(self):
        #Abrir o arquivo para gravação(apagar o conteudo)
        #percorrer a lsta
        #para cada item da lista converter em string
        #salvar no arquivo

        #Remover esta parte
        for item in self.lista_compras:
            print(item.to_string())
        #Remover ate aqui

    #Método para retornar um Item_Compra de acordo com o seu nome
    def get_item_compra(self, nome):
        #Percorrer a lista
        for item in self.lista_compras:
            #Se o nome for igual
            if (item.get_nome() == nome):
                return item

        #Se não encontrar
        return None

    #Método para retornar lista de compras
    def get_lista_compras(self):
        return self.lista_compras
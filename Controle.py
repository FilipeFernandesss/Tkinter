#Classe Controle
#Importando a classe
from Janela import Janela_principal
from bd_simulado import BD_Simulado


class Controle():
    #Método construtor
    def __init__(self):
        #Atributos
        self.bd = BD_Simulado()
        self.jnl = Janela_principal(self)
        self.jnl.mainloop()

    #Método para retornar a lista de compra
    def get_lista_compras(self):
        return self.bd.get_lista_compras()
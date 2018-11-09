from tkinter import *
from tkinter import messagebox
from control import Control
from segunda_janela import Segunda_Janela
from terceira_janela import Terceira_Janela
from quarta_janela import Quarta_Janela

class Janela_principal(Tk):
    def __init__(self, controle):
        super().__init__()
        #self.view = view
        self.control = controle

        #Ajustar o tamanho
        self.geometry('300x300+200+200')
        self.title('Menu')

        self.teste = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}

        #Widgets
        self.btn_exibir = Button(self ,width=10, text='Exibir itens', command=self.criar_segunda_janela)
        self.btn_incluir = Button(self, width=10, text='Incluir itens', command=self.criar_terceira_janela)
        self.btn_excluir = Button(self, width=10, text='Excluir itens', command=self.criar_quarta_janela)
        self.btn_sair = Button(self, width=10, text='Sair', command=self.destroy)


        #Posicionamento dos Widgets
        self.btn_exibir.place(x=110, y= 50)
        self.btn_incluir.place(x=110, y=100)
        self.btn_excluir.place(x=110, y=150)
        self.btn_sair.place(x=110, y=200)

    #Método para fechar a janela
    def destroy(self):
        #Janela de confirmaçao
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    def criar_segunda_janela(self):
        Segunda_Janela(self)

    def criar_terceira_janela(self):
        Terceira_Janela(self)

    def criar_quarta_janela(self):
        Quarta_Janela(self)

    #Método para o btn_on_click
    def btn_on_click(self):
        #Recuperar a lista de compras
        lista_compras = self.controle.get_lista_compras()
        #Percorrer a lista
        for item in lista_compras:
            messagebox.showinfo('Item', item.to_string())
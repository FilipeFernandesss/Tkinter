#Segunda janela(exibir itens)
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from model import Model

class Segunda_Janela(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('250x250+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()

        self.dicionario = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}
        self.lista = []
        for chave, valor in self.dicionario.items():
            self.messa = Label(self, text=f'{chave}: {valor}')
            print(self.messa["text"])


            #self.btn = Button(self, width=10,text='Itens', command= self.lbl)

            self.messa.place(x=100, y=50)
            self.lista.append(self.messa["text"])

        self.test = Message(self, text=self.lista)
        self.test.place(x=100, y=75)
    def teste(self):
        di = ['sdf', 'gfre', 'gvfeg']
        self.lbl = Treeview(self, text='hgfhgf')







#Segunda janela(exibir itens)
from tkinter import *
from tkinter import messagebox
from model import Model

class Segunda_Janela(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('20x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()

        self.btn = Button(self, width=10,text='Itens', command= self.teste)

        self.btn.place(x=150, y=150)

    def teste(self):
        di = ['sdf', 'gfre', 'gvfeg']
        return di





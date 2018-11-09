# Quarta janela(incluir itens)
from tkinter import *
from tkinter import messagebox
from terceira_janela import Terceira_Janela

class Quarta_Janela(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('250x250+200+200')
        self.title('Deletar Itens')
        self.transient(parent)
        self.grab_set()


        #Widget

        self.ent = Entry(self)
        self.ent.place(x=75, y=75)

        self.btn = Button(self, width=10, text='OK', command=self.bt_click)
        self.btn.place(x=75,y=100)

        self.lbl = Label(self, text='Item que será deletado:')
        self.lbl.place(x=75,y=50)

    def destroy(self):
        #Janela de confirmaçao
        if messagebox.askokcancel('Confirmação', 'Deseja realmente excluir o item?'):
            super().destroy()

    def bt_click(self):
        print(self.ent.get())

        self.destroy()

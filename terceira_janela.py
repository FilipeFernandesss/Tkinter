# Terceira janela(incluir itens)
from tkinter import *

class Terceira_Janela(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('250x250+200+200')
        self.title('Adicionar Itens')
        self.transient(parent)
        self.grab_set()

        #Widget

        self.ent = Entry(self)
        self.ent.place(x=75, y=80)

        self.btn = Button(self, width=10, text='OK', command=self.bt_click)
        self.btn.place(x=100,y=100)

        self.lbl = Label(self, text='Digite o Item:')
        self.lbl.place(x=75,y=50)

    def bt_click(self):
        print(self.ent.get())
        self.destroy()
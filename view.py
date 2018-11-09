#Classe de visualização
from Janela import Janela_principal

class View:

    #Método construtor
    def __init__(self):
        self.control = None


    # Guarda a Control associada
    def set_control(self, control):
        self.control = control

    #Método de exibição do menu
    def exibir_menu(self):
        self.jnl = Janela_principal(View)
        self.jnl.mainloop()
        resposta = True
        #Exibir menu
        while resposta:
            print('''
            1. Exibir lista
            2. Incluir item
            3. Excluir lista
            4. Sair
            ''')
            #Solicitar opcao
            resposta = input('Digite um número:')

            #Verificando a resposta
            if resposta == '1':
                print('\n Lista de itens')
                self.exibir_lista_compras(self.control.get_lista_compras())
            elif resposta == '2':
                self.incluir_item()
                print('\n Item incluído')
            elif resposta == '3':
                self.exluir()
                print('\n Item excluído')
            elif resposta == '4':
                print('\n Tchau!')
                resposta = False
            else:
                print('\n Valor incorreto!')

    #Método para exibir a lista de compras
    def exibir_lista_compras(self, lista_compras):
        #A lista de compras é um dicionário
        #Percorrer um dicionario
        for chave, valor in lista_compras.items():
            print(f'- {chave} : {valor}')

    #Método para incluir item
    def incluir_item(self):
        item = input("Digite o item:\n")
        qtd = int(input("Digite  a quantidade:\n"))
        self.control.incluir_item(item, qtd)
        #self.atualizar_quantidade(item, qtd)


    #Excluir item
    def exluir(self):
        item = input("Digite o item que será exluido:\n")
        self.control.excluir(item)

    #Att quantidade
    def atualizar_quantidade(self, item, qtd):
            resposta = input("""
            1. Atualizar a quantidadde de itens.
            2. Retonar ao menu principal.""")

            if resposta == '1':
                self.control.add_quantidade(item, qtd)
            elif resposta == '2':
                print("Menu Principal")
            else:
                print("fdg")

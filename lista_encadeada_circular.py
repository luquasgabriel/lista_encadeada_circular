from membro import Membro

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None
        self.atual = None

    def adicionar_membro(self, membro):
        if not self.head:
            self.head = membro
            membro.proximo = self.head
            self.atual = membro
        else:
            membro.proximo = self.head
            temp = self.head
            # Para encontrar o último membro
            while temp.proximo != self.head:  
                temp = temp.proximo
            #O último membro aponta para o novo membro
            temp.proximo = membro  

    def proximo_responsavel(self):
        if not self.head:
            print("A lista está vazia.")
            return None
        print(f"Próximo responsável: {self.atual.nome}")
        self.atual = self.atual.proximo


    def remover_membro(self, nome):
        if not self.head:
            print("A lista está vazia.")
            return

        atual = self.head
        anterior = None

        # Caso o seja o head que sera removido
        if atual.nome == nome:
            if atual.proximo == self.head: 
                self.head = None
            else:
                while atual.proximo != self.head: 
                    atual = atual.proximo
                atual.proximo = self.head.proximo
                self.head = self.head.proximo
            print(f"Membro '{nome}' removido.")
            return

        # Percorre a lista ate encontrar o membro
        while True:
            anterior = atual
            atual = atual.proximo
            if atual == self.head:
                print(f"Membro '{nome}' não encontrado.")
                return
            if atual.nome == nome:
                anterior.proximo = atual.proximo 
                print(f"Membro '{nome}' removido.")
                return


    def mostrar_lista(self):
        if not self.head:
            print("A lista está vazia.")
            return
        membros = []
        atual = self.head
        while True:
            membros.append(atual.nome)
            atual = atual.proximo
            if atual == self.head:
                break
        print("Lista de membros:", " >>> ".join(membros))

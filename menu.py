from lista_encadeada_circular import ListaEncadeadaCircular
from membro import Membro

def menu_principal():
    lista_membros = ListaEncadeadaCircular()

    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("         Menu Principal             ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1 - Gerenciar Membros")
        print("2 - Encerrar")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_gerenciar_membros(lista_membros)
        elif opcao == '2':
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_gerenciar_membros(lista):
    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("         Gerenciar Membros         ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1 - Adicionar membro")
        print("2 - Remover membro")
        print("3 - Mostrar lista de membros")
        print("4 - Próximo responsável")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do membro: ")
            membro = Membro(nome)
            lista.adicionar_membro(membro)
            print(f"Membro {nome} adicionado com sucesso.")

        elif opcao == '2':
            nome = input("Digite o nome do membro a ser removido: ")
            lista.remover_membro(nome)

        elif opcao == '3':
            lista.mostrar_lista()

        elif opcao == '4':
            lista.proximo_responsavel()

        elif opcao == '5':
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_principal()

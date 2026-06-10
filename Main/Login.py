


def login():
    print("\nSISTEMA DE LOGIN")

    nome = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("USUÁRIO LOGADO")
            escolher_menu()
            return

    print("USUÁRIO OU SENHA INCORRETA")


def cadastro():
    print("\nSISTEMA DE CADASTRO")

    nome = input("Digite o nome de usuário: ")

    for u in usuarios:
        if u["nome"] == nome:
            print("USUÁRIO JÁ CADASTRADO")
            return

    senha = input("Digite sua senha: ")
    usuarios.append({"nome": nome, "senha": senha})
    print("Cadastro realizado!")


def sair():
    print("SAINDO...")


def MenuCadastro():
        while True:
            print("\n==== MENU DE CADASTRO ====\n")

            escolha = int(input("1 - LOGIN\n2 - CADASTRO\n3 - SAIR\nEscolha: "
                 ))

            if escolha == 1:
                login()
                input("\nPressione ENTER para voltar ao menu...")

            elif escolha == 2:
                cadastro()
                input("\nPressione ENTER para voltar ao menu...")

            elif escolha == 3:
                sair()
                break

            else:
                print("Opção inválida")
                input("\nPressione ENTER para voltar ao menu...")